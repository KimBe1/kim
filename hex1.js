var rind,rnns;
var __Oxda344 = ["", "\x6C\x65\x6E\x67\x74\x68", "\x63\x6F\x6E\x63\x61\x74", "\x63\x68\x61\x72\x43\x6F\x64\x65\x41\x74", "\x66\x72\x6F\x6D\x43\x68\x61\x72\x43\x6F\x64\x65", "\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x41\x42\x43\x44\x45\x46", "\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x61\x62\x63\x64\x65\x66", "\x63\x68\x61\x72\x41\x74", "\x73\x75\x62\x73\x74\x72\x69\x6E\x67", "\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4A\x4B\x4C\x4D\x4E\x4F\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5A\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6A\x6B\x6C\x6D\x6E\x6F\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7A\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x2B\x2F", "\x75\x6E\x64\x65\x66\x69\x6E\x65\x64", "\x6C\x6F\x67", "\u5220\u9664", "\u7248\u672C\u53F7\uFF0C\x6A\x73\u4F1A\u5B9A", "\u671F\u5F39\u7A97\uFF0C", "\u8FD8\u8BF7\u652F\u6301\u6211\u4EEC\u7684\u5DE5\u4F5C", "\x6A\x73\x6A\x69\x61", "\x6D\x69\x2E\x63\x6F\x6D"];
var chrsz = 8;
function hex_1(A) {
    return binl2hex(core_m32(str2binl(A), A[__Oxda344[0x1]] * chrsz))
}
function core_m32(A, B) {
    A[B >> 5] |= 0x80 << ((B) % 32);
    A[(((B + 64) >>> 9) << 4) + 14] = B;
    var C = 1732584193;
    var D = -271733879;
    var E = -1732584194;
    var F = 271733878;
    for (var G = 0; G < A[__Oxda344[0x1]]; G += 16) {
        var H = C;
        var I = D;
        var J = E;
        var K = F;
        C = mee336_ff(C, D, E, F, A[G + 0], 7, -680876936);
        F = mee336_ff(F, C, D, E, A[G + 1], 12, -389564586);
        E = mee336_ff(E, F, C, D, A[G + 2], 17, 606105819);
        D = mee336_ff(D, E, F, C, A[G + 3], 22, -1044525330);
        C = mee336_ff(C, D, E, F, A[G + 4], 7, -176418897);
        F = mee336_ff(F, C, D, E, A[G + 5], 12, 1200080426);
        E = mee336_ff(E, F, C, D, A[G + 6], 17, -1473231341);
        D = mee336_ff(D, E, F, C, A[G + 7], 22, -45705983);
        C = mee336_ff(C, D, E, F, A[G + 8], 7, 1770035416);
        F = mee336_ff(F, C, D, E, A[G + 9], 12, -1958414417);
        E = mee336_ff(E, F, C, D, A[G + 10], 17, -42063);
        D = mee336_ff(D, E, F, C, A[G + 11], 22, -1990404162);
        C = mee336_ff(C, D, E, F, A[G + 12], 7, 1804603682);
        F = mee336_ff(F, C, D, E, A[G + 13], 12, -40341101);
        E = mee336_ff(E, F, C, D, A[G + 14], 17, -1502002290);
        D = mee336_ff(D, E, F, C, A[G + 15], 22, 1236535329);
        C = ddf2_gg(C, D, E, F, A[G + 1], 5, -165796510);
        F = ddf2_gg(F, C, D, E, A[G + 6], 9, -1069501632);
        E = ddf2_gg(E, F, C, D, A[G + 11], 14, 643717713);
        D = ddf2_gg(D, E, F, C, A[G + 0], 20, -373897302);
        C = ddf2_gg(C, D, E, F, A[G + 5], 5, -701558691);
        F = ddf2_gg(F, C, D, E, A[G + 10], 9, 38016083);
        E = ddf2_gg(E, F, C, D, A[G + 15], 14, -660478335);
        D = ddf2_gg(D, E, F, C, A[G + 4], 20, -405537848);
        C = ddf2_gg(C, D, E, F, A[G + 9], 5, 568446438);
        F = ddf2_gg(F, C, D, E, A[G + 14], 9, -1019803690);
        E = ddf2_gg(E, F, C, D, A[G + 3], 14, -187363961);
        D = ddf2_gg(D, E, F, C, A[G + 8], 20, 1163531501);
        C = ddf2_gg(C, D, E, F, A[G + 13], 5, -1444681467);
        F = ddf2_gg(F, C, D, E, A[G + 2], 9, -51403784);
        E = ddf2_gg(E, F, C, D, A[G + 7], 14, 1735328473);
        D = ddf2_gg(D, E, F, C, A[G + 12], 20, -1926607734);
        C = md5_hh(C, D, E, F, A[G + 5], 4, -378558);
        F = md5_hh(F, C, D, E, A[G + 8], 11, -2022574463);
        E = md5_hh(E, F, C, D, A[G + 11], 16, 1839030562);
        D = md5_hh(D, E, F, C, A[G + 14], 23, -35309556);
        C = md5_hh(C, D, E, F, A[G + 1], 4, -1530992060);
        F = md5_hh(F, C, D, E, A[G + 4], 11, 1272893353);
        E = md5_hh(E, F, C, D, A[G + 7], 16, -155497632);
        D = md5_hh(D, E, F, C, A[G + 10], 23, -1094730640);
        C = md5_hh(C, D, E, F, A[G + 13], 4, 681279174);
        F = md5_hh(F, C, D, E, A[G + 0], 11, -358537222);
        E = md5_hh(E, F, C, D, A[G + 3], 16, -722521979);
        D = md5_hh(D, E, F, C, A[G + 6], 23, 76029189);
        C = md5_hh(C, D, E, F, A[G + 9], 4, -640364487);
        F = md5_hh(F, C, D, E, A[G + 12], 11, -421815835);
        E = md5_hh(E, F, C, D, A[G + 15], 16, 530742520);
        D = md5_hh(D, E, F, C, A[G + 2], 23, -995338651);
        C = md5_ii(C, D, E, F, A[G + 0], 6, -198630844);
        F = md5_ii(F, C, D, E, A[G + 7], 10, 1126891415);
        E = md5_ii(E, F, C, D, A[G + 14], 15, -1416354905);
        D = md5_ii(D, E, F, C, A[G + 5], 21, -57434055);
        C = md5_ii(C, D, E, F, A[G + 12], 6, 1700485571);
        F = md5_ii(F, C, D, E, A[G + 3], 10, -1894986606);
        E = md5_ii(E, F, C, D, A[G + 10], 15, -1051523);
        D = md5_ii(D, E, F, C, A[G + 1], 21, -2054922799);
        C = md5_ii(C, D, E, F, A[G + 8], 6, 1873313359);
        F = md5_ii(F, C, D, E, A[G + 15], 10, -30611744);
        E = md5_ii(E, F, C, D, A[G + 6], 15, -1560198380);
        D = md5_ii(D, E, F, C, A[G + 13], 21, 1309151649);
        C = md5_ii(C, D, E, F, A[G + 4], 6, -145523070);
        F = md5_ii(F, C, D, E, A[G + 11], 10, -1120210379);
        E = md5_ii(E, F, C, D, A[G + 2], 15, 718787259);
        D = md5_ii(D, E, F, C, A[G + 9], 21, -343485551);
        C = safe_add(C, H);
        D = safe_add(D, I);
        E = safe_add(E, J);
        F = safe_add(F, K)
    }
    ;return Array(C, D, E, F)
}
function md5_cmn(A, B, C, D, E, F) {
    return safe_add(bit_rol(safe_add(safe_add(B, A), safe_add(D, F)), E), C)
}
function mee336_ff(A, B, C, D, E, F, G) {
    return md5_cmn((B & C) | ((~B) & D), A, B, E, F, G)
}
function ddf2_gg(A, B, C, D, E, F, G) {
    return md5_cmn((B & D) | (C & (~D)), A, B, E, F, G)
}
function md5_hh(A, B, C, D, E, F, G) {
    return md5_cmn(B ^ C ^ D, A, B, E, F, G)
}
function md5_ii(A, B, C, D, E, F, G) {
    return md5_cmn(C ^ (B | (~D)), A, B, E, F, G)
}
function safe_add(A, B) {
    var C = (A & 0xFFFF) + (B & 0xFFFF);
    var D = (A >> 16) + (B >> 16) + (C >> 16);
    return (D << 16) | (C & 0xFFFF)
}
function bit_rol(A, B) {
    return (A << B) | (A >>> (32 - B))
}
function str2binl(A) {
    var B = Array();
    var C = (1 << chrsz) - 1;
    for (var D = 0; D < A[__Oxda344[0x1]] * chrsz; D += chrsz) {
        B[D >> 5] |= (A[__Oxda344[0x3]](D / chrsz) & C) << (D % 32)
    }
    ;return B
}
function binl2hex(A) {
    var B = 0 ? __Oxda344[0x5] : __Oxda344[0x6];
    var C = __Oxda344[0x0];
    for (var D = 0; D < A[__Oxda344[0x1]] * 4; D++) {
        C += B[__Oxda344[0x7]]((A[D >> 2] >> ((D % 4) * 8 + 4)) & 0xF) + B[__Oxda344[0x7]]((A[D >> 2] >> ((D % 4) * 8)) & 0xF)
    }
    ;C = (C[__Oxda344[0x8]](0, rind) + rnns + C[__Oxda344[0x8]](rind + rnns[__Oxda344[0x1]]));
    return C
}

function get_hex_1(sct,_rind,_rnns){
    rnns = _rnns;
    rind = _rind;
    return hex_1(sct);
}


// 调用示例
// console.log(get_hex_1('20mMtFTW3GuRZn2Z',4,'Z'))
// console.log('119cZ3edd9a4ae9c5ed3b1ec12e181b3')