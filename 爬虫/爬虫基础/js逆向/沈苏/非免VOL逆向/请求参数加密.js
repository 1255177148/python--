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

var t = { "pageNo": 1, "pageSize": 20, "stationCode": "4602020000", "ymCode": "", "qyCode": "", "dateType": "2", "timestamp": 1728875708457 }
console.log(encodeParams(t))
console.log(decryptParams(encodeParams(t)))