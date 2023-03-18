import json
import execjs
import random
import time
import hashlib
import requests


class ICNet:
    def __init__(self):
        self.session = requests.session()

    def get_nonce(self):
        n = []
        t = "0123456789abcdef"
        for r in range(36):
            n.append(t[random.randint(0, 15)])
        n[14] = "4"
        n[19] = t[(int(n[19], 16) & 3) | 8]
        n[8] = n[13] = n[18] = n[23] = "-"
        return ''.join(n)

    def get_timestamp(self):
        return str(time.time()).replace('.', '')[:10]

    def get_sign_IC(self, IC_Method, nonce, timestamp):
        t = 'IC_Method{}nonce{}timestamp{}'.format(IC_Method, nonce, timestamp) + '2qpohxsfm8a0'
        t = str(hashlib.md5((t).encode()).hexdigest())[::-1]
        t = hashlib.md5(t.encode()).hexdigest()
        return t

    def get_sign_ICPI(self, ICPI_Method, key_word, nonce, select_date, timestamp):
        t = 'ICPI_Method{}key{}nonce{}select_date{}timestamp{}'.format(ICPI_Method, key_word, nonce, select_date,
                                                                       timestamp) + '2qpohxsfm8a0'
        t = str(hashlib.md5((t).encode()).hexdigest())[::-1]
        t = hashlib.md5(t.encode()).hexdigest()
        return t

    def get_js_from_file(self, file_name):
        try:
            with open(file_name, 'r', encoding='UTF-8') as file:
                result = file.read()
            return result
        except:
            input('hex1.js文件不存')
            exit()

    def get_serial(self, sct, rind, rnns):
        context = execjs.compile(self.get_js_from_file(file_name='hex1.js'))
        encrypt_hex1_result = context.call('get_hex_1', sct, rind, rnns)
        return hashlib.sha1(encrypt_hex1_result.encode('utf-8')).hexdigest()

    # 有请求 后续需加代理
    def get_sct_rind_rnns(self):
        headers = {
            'APPID': 'UNI-APP-M',
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Authorization': '',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Origin': 'https://m.ic.net.cn',
            'Pragma': 'no-cache',
            'Referer': 'https://m.ic.net.cn/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36',
            'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
        }
        tp = self.get_timestamp()
        nc = self.get_nonce()
        params = {
            'IC_Method': 'getOneNewsInfo',
            'timestamp': tp,
            'nonce': nc,
            'sign': self.get_sign_IC(IC_Method='getOneNewsInfo', timestamp=tp, nonce=nc),
        }
        response = self.session.get('https://max.ic.net.cn/asyncCall/news.asy.php', params=params, headers=headers)
        content = response.text
        content = content[content.index('jbnxtdm();') + 10:].replace('pageInitialize();', '')

        # print(content)
        if len(content) > 1500:
            # print('歇菜了,再来一次把')
            time.sleep(1)
            return False
        else:
            content = content + "function get_par(){return sct+'|'+rind+'|'+rnns+'|'+torc}"
            context = execjs.compile(content)
            sct_rind_rnns = str(context.call('get_par')).split('|')
            return sct_rind_rnns
    # 以上为加密用

    # 有请求 后续需加代理
    def login(self, user_phone:str, user_pwd:str)->dict:
        """
        登录 成功会返回authorization
        :param user_phone: 账号
        :param user_pwd: 密码
        :return: {'status': True, 'msg': '成功', 'data': '网站接口返回的数据（authorization）'}
        """
        headers = {
            'Host': 'max.ic.net.cn',
            'Connection': 'keep-alive',
            'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
            'Content-Type': 'application/x-www-form-urlencoded',
            'APPID': 'UNI-APP-M',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
            'sec-ch-ua-platform': '"Windows"',
            'Accept': '*/*',
            'Origin': 'https://m.ic.net.cn',
            'Sec-Fetch-Site': 'same-site',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://m.ic.net.cn/',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }
        tp = self.get_timestamp()
        nc = self.get_nonce()
        sign = self.get_sign_IC(IC_Method='userlogin', nonce=nc, timestamp=tp)
        data = {
            'IC_Method': 'userlogin',
            'UserName': user_phone,
            'Pwd': user_pwd,
            'timestamp': tp,
            'nonce': nc,
            'sign': sign,
        }

        response = requests.post('https://max.ic.net.cn/asyncCall/login.asy.php', headers=headers, data=data)
        result = json.loads(response.text)
        if result['error'] == '':
            return {'status': True, 'msg': '成功', 'data': result}
        else:
            return {'status': False, 'msg': '失败', 'data': result}
    # 有请求 后续需加代理
    def search(self, authorization:str, user_phone:str, key_word:str, page:int)->dict:
        """
        需求文档中的接口1 搜索功能
        :param authorization: login()函数返回
        :param user_phone: 账号
        :param key_word: 搜索的关键词
        :param page: 页码
        :return: {'status': True, 'msg': '成功', 'data': '网站接口返回的数据'}
        """
        headers = {
            'APPID': 'UNI-APP-M',
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Authorization': authorization,
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Origin': 'https://m.ic.net.cn',
            'Pragma': 'no-cache',
            'Referer': 'https://m.ic.net.cn/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36',
            'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
        }

        res = False
        while not res:
            # sct rind rnns torc
            res = self.get_sct_rind_rnns()
        # print(res)
        tp = self.get_timestamp()
        nc = self.get_nonce()
        sign = self.get_sign_IC(IC_Method='getstockdata', nonce=nc, timestamp=tp)

        params = {
            'IC_Method': 'getstockdata',
            'key': key_word,
            'Serial': self.get_serial(sct=res[0], rind=res[1], rnns=res[2]),
            'TimeStamp': res[3],
            'userName': user_phone,
            'page': str(page),
            'area': '0',
            'market': '',
            'sort': '',
            'timestamp': tp,
            'nonce': nc,
            'sign': sign,
        }

        response = self.session.get('https://max.ic.net.cn/asyncCall/search.asy.php', params=params, headers=headers)
        result = json.loads(response.text)
        if result['error'] == '':
            return {'status': True, 'msg': '成功', 'data': result}
        else:
            return {'status': False, 'msg': '失败', 'data': result}
    # 有请求 后续需加代理
    def get_week_search_inedex_detail(self, authorization:str, key_word:str, select_date:str)->dict:
        """
        需求文档里的接口2 接口3 实际共用此接口 获取搜索指数 库存等
        :param authorization: login()函数返回
        :param key_word: 搜索的关键词
        :param select_date: 选择的日期
        :return: {'status': True, 'msg': '成功', 'data': '网站接口返回的数据'}
        """
        headers = {
            'Host': 'max.ic.net.cn',
            'Connection': 'keep-alive',
            'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
            'sec-ch-ua-mobile': '?0',
            'Authorization': authorization,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
            'sec-ch-ua-platform': '"Windows"',
            'Accept': '*/*',
            'Origin': 'https://m.ic.net.cn',
            'Sec-Fetch-Site': 'same-site',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://m.ic.net.cn/',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }
        tp = self.get_timestamp()
        nc = self.get_nonce()
        sign = self.get_sign_ICPI(ICPI_Method='getWeek', key_word=key_word, nonce=nc, select_date=select_date,
                                  timestamp=tp)
        params = {
            'ICPI_Method': 'getWeek',
            'key': key_word,
            'select_date': select_date,
            'timestamp': tp,
            'nonce': nc,
            'sign': sign,
        }

        response = requests.get('https://max.ic.net.cn/icpi/asyncCall/detail.asy.php', params=params, headers=headers)
        result = json.loads(response.text)
        if result['error'] == '':
            return {'status': True, 'msg': '成功', 'data': result}
        else:
            return {'status': False, 'msg': '失败', 'data': result}


if __name__ == '__main__':
    user_phone = '账号'
    user_pwd = '密码'
    ic = ICNet()
    res = ic.login(user_phone=user_phone, user_pwd=user_pwd)
    print('登录返回:', res)
    time.sleep(5)
    if res['status']:
        authorization = res['data']['token']
        res = ic.search(authorization=authorization, user_phone=user_phone, key_word='被搜索的关键词', page=1)
        print('搜索返回:', res)
        time.sleep(5)
        res = ic.get_week_search_inedex_detail(authorization=authorization, key_word='被搜索的关键词',
                                               select_date='日期，格式为:2023-03-16')
        print('详细数据返回:', res)

