// 这里是在XHR提取断点之后，在右侧窗口的调用堆栈里找到axios请求，然后获取到加密函数
const CryptoJS = require("crypto-js");

var u = "9mckdlpe$gg#$GJH"

function l(t) {
    var e = CryptoJS.enc.Utf8.parse(u);
    return "object" === typeof t && (t = JSON.stringify(t)),
        t = CryptoJS.enc.Utf8.parse(t),
        CryptoJS.AES.encrypt(t, e, {
            mode: CryptoJS.mode.ECB,
            padding: CryptoJS.pad.Pkcs7
        }).ciphertext.toString() // 这里的toString，是转成了16进制字符串
}

function encodeParams(t) {
    return l(t)
}

// 逆向js加密方法，写出对应的解密方法
function decryptParams(t) {
    t = CryptoJS.enc.Hex.parse(t); // 因为加密的时候是转成16进制字符串返回的，所以这里要先将16进制的字符串转码成bytes
    var srcs = CryptoJS.enc.Base64.stringify(t); // 这里将转码后的bytes再转回base64编码的字符串
    var e = CryptoJS.enc.Utf8.parse(u);
    return CryptoJS.AES.decrypt(srcs, e, {
        mode: CryptoJS.mode.ECB,
        padding: CryptoJS.pad.Pkcs7
    }).toString(CryptoJS.enc.Utf8)
}

var t = { "pageNo": 1, "pageSize": 20, "stationCode": "4602020000", "ymCode": "", "qyCode": "", "dateType": "2", "timestamp": (new Date).getTime() }
var encodeParam = encodeParams(t)
console.log(encodeParam)
console.log(decryptParams(encodeParam))

// 上面是请求参数中的params加解密

// 下面是请求参数中的sign加解密
function wordsToBytes(t) {
    for (var e = [], A = 0; A < 32 * t.length; A += 8)
        e.push(t[A >>> 5] >>> 24 - A % 32 & 255);
    return e
}
function stringToBytes(t) {
    return stringToBytes_(unescape(encodeURIComponent(t)))
}
function stringToBytes_(t) {
    for (var e = [], A = 0; A < t.length; A++)
        e.push(255 & t.charCodeAt(A));
    return e
}
function o(t) {
    return null != t && (A(t) || "function" == typeof (e = t).readFloatLE && "function" == typeof e.slice && A(e.slice(0, 0)) || !!t._isBuffer);
    var e
}
function A(t) {
    return !!t.constructor && "function" == typeof t.constructor.isBuffer && t.constructor.isBuffer(t)
}
function bytesToWords(t) {
    for (var e = [], A = 0, n = 0; A < t.length; A++,
        n += 8)
        e[n >>> 5] |= t[A] << 24 - n % 32;
    return e
}
n._ff = function (t, e, A, n, r, i, o) {
    return ((o = t + (e & A | ~e & n) + (r >>> 0) + o) << i | o >>> 32 - i) + e
}
    ,
    n._gg = function (t, e, A, n, r, i, o) {
        return ((o = t + (e & n | A & ~n) + (r >>> 0) + o) << i | o >>> 32 - i) + e
    }
    ,
    n._hh = function (t, e, A, n, r, i, o) {
        return ((o = t + (e ^ A ^ n) + (r >>> 0) + o) << i | o >>> 32 - i) + e
    }
    ,
    n._ii = function (t, e, A, n, r, i, o) {
        return ((o = t + (A ^ (e | ~n)) + (r >>> 0) + o) << i | o >>> 32 - i) + e
    }
function rotl(t, e) {
    return t << e | t >>> 32 - e
}
function endian(t) {
    if (t.constructor == Number)
        return 16711935 & rotl(t, 8) | 4278255360 & rotl(t, 24);
    for (var e = 0; e < t.length; e++)
        t[e] = endian(t[e]);
    return t
}
function n(t, e) {
    t.constructor == String ? t = stringToBytes(t) : o(t) ? t = Array.prototype.slice.call(t, 0) : Array.isArray(t) || t.constructor === Uint8Array || (t = t.toString());
    for (var A = bytesToWords(t), s = (t = 8 * t.length,
        1732584193), c = -271733879, u = -1732584194, l = 271733878, f = 0; f < A.length; f++)
        A[f] = 16711935 & (A[f] << 8 | A[f] >>> 24) | 4278255360 & (A[f] << 24 | A[f] >>> 8);
    A[t >>> 5] |= 128 << t % 32,
        A[14 + (64 + t >>> 9 << 4)] = t;
    var h = n._ff
        , d = n._gg
        , p = n._hh
        , g = n._ii;
    for (f = 0; f < A.length; f += 16) {
        var m = s
            , B = c
            , w = u
            , v = l;
        s = h(s, c, u, l, A[f + 0], 7, -680876936),
            l = h(l, s, c, u, A[f + 1], 12, -389564586),
            u = h(u, l, s, c, A[f + 2], 17, 606105819),
            c = h(c, u, l, s, A[f + 3], 22, -1044525330);
        s = h(s, c, u, l, A[f + 4], 7, -176418897),
            l = h(l, s, c, u, A[f + 5], 12, 1200080426),
            u = h(u, l, s, c, A[f + 6], 17, -1473231341),
            c = h(c, u, l, s, A[f + 7], 22, -45705983),
            s = h(s, c, u, l, A[f + 8], 7, 1770035416),
            l = h(l, s, c, u, A[f + 9], 12, -1958414417),
            u = h(u, l, s, c, A[f + 10], 17, -42063),
            c = h(c, u, l, s, A[f + 11], 22, -1990404162),
            s = h(s, c, u, l, A[f + 12], 7, 1804603682),
            l = h(l, s, c, u, A[f + 13], 12, -40341101),
            u = h(u, l, s, c, A[f + 14], 17, -1502002290),
            s = d(s, c = h(c, u, l, s, A[f + 15], 22, 1236535329), u, l, A[f + 1], 5, -165796510),
            l = d(l, s, c, u, A[f + 6], 9, -1069501632),
            u = d(u, l, s, c, A[f + 11], 14, 643717713),
            c = d(c, u, l, s, A[f + 0], 20, -373897302),
            s = d(s, c, u, l, A[f + 5], 5, -701558691),
            l = d(l, s, c, u, A[f + 10], 9, 38016083),
            u = d(u, l, s, c, A[f + 15], 14, -660478335),
            c = d(c, u, l, s, A[f + 4], 20, -405537848),
            s = d(s, c, u, l, A[f + 9], 5, 568446438),
            l = d(l, s, c, u, A[f + 14], 9, -1019803690),
            u = d(u, l, s, c, A[f + 3], 14, -187363961),
            c = d(c, u, l, s, A[f + 8], 20, 1163531501),
            s = d(s, c, u, l, A[f + 13], 5, -1444681467),
            l = d(l, s, c, u, A[f + 2], 9, -51403784),
            u = d(u, l, s, c, A[f + 7], 14, 1735328473),
            s = p(s, c = d(c, u, l, s, A[f + 12], 20, -1926607734), u, l, A[f + 5], 4, -378558),
            l = p(l, s, c, u, A[f + 8], 11, -2022574463),
            u = p(u, l, s, c, A[f + 11], 16, 1839030562),
            c = p(c, u, l, s, A[f + 14], 23, -35309556),
            s = p(s, c, u, l, A[f + 1], 4, -1530992060),
            l = p(l, s, c, u, A[f + 4], 11, 1272893353),
            u = p(u, l, s, c, A[f + 7], 16, -155497632),
            c = p(c, u, l, s, A[f + 10], 23, -1094730640),
            s = p(s, c, u, l, A[f + 13], 4, 681279174),
            l = p(l, s, c, u, A[f + 0], 11, -358537222),
            u = p(u, l, s, c, A[f + 3], 16, -722521979),
            c = p(c, u, l, s, A[f + 6], 23, 76029189),
            s = p(s, c, u, l, A[f + 9], 4, -640364487),
            l = p(l, s, c, u, A[f + 12], 11, -421815835),
            u = p(u, l, s, c, A[f + 15], 16, 530742520),
            s = g(s, c = p(c, u, l, s, A[f + 2], 23, -995338651), u, l, A[f + 0], 6, -198630844),
            l = g(l, s, c, u, A[f + 7], 10, 1126891415),
            u = g(u, l, s, c, A[f + 14], 15, -1416354905),
            c = g(c, u, l, s, A[f + 5], 21, -57434055),
            s = g(s, c, u, l, A[f + 12], 6, 1700485571),
            l = g(l, s, c, u, A[f + 3], 10, -1894986606),
            u = g(u, l, s, c, A[f + 10], 15, -1051523),
            c = g(c, u, l, s, A[f + 1], 21, -2054922799),
            s = g(s, c, u, l, A[f + 8], 6, 1873313359),
            l = g(l, s, c, u, A[f + 15], 10, -30611744),
            u = g(u, l, s, c, A[f + 6], 15, -1560198380),
            c = g(c, u, l, s, A[f + 13], 21, 1309151649),
            s = g(s, c, u, l, A[f + 4], 6, -145523070),
            l = g(l, s, c, u, A[f + 11], 10, -1120210379),
            u = g(u, l, s, c, A[f + 2], 15, 718787259),
            c = g(c, u, l, s, A[f + 9], 21, -343485551),
            s = s + m >>> 0,
            c = c + B >>> 0,
            u = u + w >>> 0,
            l = l + v >>> 0
    }
    return endian([s, c, u, l])
}
function bytesToString(t) {
    for (var e = [], A = 0; A < t.length; A++)
        e.push(String.fromCharCode(t[A]));
    return e.join("")
}
function bytesToHex(t) {
    for (var e = [], A = 0; A < t.length; A++)
        e.push((t[A] >>> 4).toString(16)),
        e.push((15 & t[A]).toString(16));
    return e.join("")
}
function a(t, e) {
    if (null == t)
        throw new Error("Illegal argument " + t);
    return t = wordsToBytes(n(t, e)),
        e && e.asBytes ? t : e && e.asString ? bytesToString(t) : bytesToHex(t)
}
var c = "D1ckd#$G$fDdgh23";
console.log('sign的值是:', a(encodeParam + c))