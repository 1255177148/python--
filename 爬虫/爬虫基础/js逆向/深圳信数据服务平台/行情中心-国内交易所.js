// 网页地址：https://webapi.cninfo.com.cn/#/marketDataDate
// 里面的方法是混淆的，这里就是一步步将混淆的方法在控制台打印出来，看到底是什么，固定值的话就直接转为值，
// 函数的话，就把函数拿过来

const _0x5c640c = require("crypto-js")
var localStorage = {
    "isLogin": "false",
    "Hm_lvt_489bd07e99fbfc5f12cbb4145adb0a9b": "1760711906055|1728799552,1729175843",
    "G_access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0ZW5hbnRfaWQiOjQ0LCJleHBpcmVzX2F0IjoxNzI5MjE5MDQ2MTU2LCJkZXZpY2VfaWQiOiJrbGluZUFsbDIuaHRtbDdqZnlqdXRvLnRtNTE5czQxbTAuZDVsNyIsInVzZXJfaWQiOiIzNTk2MjM2NzgwODYwMDE1Njc2IiwiZGV2aWNlX3R5cGUiOiIyMDEiLCJjbGllbnRfaWQiOiJTWlhTSlpYXzQ1IiwiaG9zdF9pZGVudGlmaWVyIjoiY2NjNDdkYTA4MjNjNjMyYmRmODJiZmNjMzg4ZWJjMTUiLCJqdGkiOiJhNzNjY2IzMS1hNmZmLTRkM2UtOGM4ZC0yN2I5OTM0YmE2YjQifQ.kJtVIFAKzAWPQM1qVpqCxuSXWXHu7cM2HckzeK_zTms",
    "slider": "slider-6585daec-74bf-491d-96be-deb18432bcdd",
    "device_id_internal": "a7be3736-8ac1-4396-846e-a166f0814735",
    "accept-cookie": "1",
    "G_localHttp": "https://shdatasdk.mktdata.cn/application/",
    "uniqueId": "7jfyjuto.tm519s41m0.d5l7",
    "G_userid": "3596236780860015676",
    "point": "point-6585daec-74bf-491d-96be-deb18432bcdd",
    "tempenc": "1234567887654321",
    "getItem": function () {

    }
}
function getResCode() {
    var _0x3d64a7 = _0x5c640c['AES']['encrypt'](_0x5c640c['enc']['Utf8']['parse'](Math['floor'](phNWP(new Date()['getTime'](), -0x29f * 0x1 + -0x1f16 + 0x259d * 0x1))), _0x5c640c['enc']['Utf8']['parse'](localStorage['getItem']('tempenc') || '1234567887654321'), {
        'iv': _0x5c640c['enc']['Utf8']['parse']("1234567887654321"),
        'mode': _0x5c640c['mode']['CBC'],
        'padding': _0x5c640c['pad']['Pkcs7']
    });
    return _0x5c640c['enc']['Base64']['stringify'](_0x3d64a7['ciphertext']);
}

function phNWP(_0x417158, _0x163dab) {
    return _0x417158 / _0x163dab;
}

console.log(getResCode())
console.log(localStorage['getItem']('tempenc'))