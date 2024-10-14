// 思路：1、通过在XHR提取断点里，将数据请求接口的断点添加，然后一步步找到数据的返回行，异步的ajax一般可以在new Promise对象代码中请求，
//在onreadystatechange事件函数中，收到请求的相应数据，然后调试的过程中注意右侧调试框里的作用域内的变量是否有解析后的明文数据，有的话，说明以经过解密函数，
//可以在此处打个断点，然后重新请求进入调试，注意快到出现明文的地方后，慢点儿调试，看是否有解密函数。
// axios.interceptors.response.use()这个是ajax请求的返回拦截器，可以在请求之后拦截返回的数据并进行处理，当前逆向项目，解密返回数据就是在这个拦截器函数内解密的

const CryptoJS = require("crypto-js");
var c = "D1ckd#$G$fDdgh23"
var u = "9mckdlpe$gg#$GJH"
function f(t) {
    var e = CryptoJS.enc.Utf8.parse(u);
    return t = CryptoJS.enc.Hex.parse(t).toString(),
        t = CryptoJS.enc.Hex.parse(t),
        t = CryptoJS.enc.Base64.stringify(t).toString(CryptoJS.enc.Utf8),
        CryptoJS.AES.decrypt(t, e, {
            mode: CryptoJS.mode.ECB,
            padding: CryptoJS.pad.Pkcs7
        }).toString(CryptoJS.enc.Utf8).toString().replace(/\u0000/g, "")
}
function wordsToBytes(t) {
    for (var e = [], A = 0; A < 32 * t.length; A += 8)
        e.push(t[A >>> 5] >>> 24 - A % 32 & 255);
    return e
}
function bytesToWords(t) {
    for (var e = [], A = 0, n = 0; A < t.length; A++,
        n += 8)
        e[n >>> 5] |= t[A] << 24 - n % 32;
    return e
}
function stringToBytes_(t) {
    for (var e = [], A = 0; A < t.length; A++)
        e.push(255 & t.charCodeAt(A));
    return e
}
function stringToBytes(t) {
    return stringToBytes_(unescape(encodeURIComponent(t)))
}
function bytesToString(t) {
    for (var e = [], A = 0; A < t.length; A++)
        e.push(String.fromCharCode(t[A]));
    return e.join("")
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
function A(t) {
    return !!t.constructor && "function" == typeof t.constructor.isBuffer && t.constructor.isBuffer(t)
}
function o(t) {
    return null != t && (A(t) || "function" == typeof (e = t).readFloatLE && "function" == typeof e.slice && A(e.slice(0, 0)) || !!t._isBuffer);
    var e
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

function decryptData(t) {
    t = JSON.parse(t)
    if (!t.params)
        return t;
    var e = f(t.params);
    if (a(t.params + c) !== t.sign)
        return console.log(222),
            alert('解密失败')
    try {
        return JSON.parse(e)
    } catch (t) {
        return e
    }
}
t = '{"params": "8151ff3bc4f57d0676395c54277d375fe6490049a36e1ac61a18f6254822c7f6ba499816645a85cfe85f1ac6974ceb9f66ef732bcf5ade7f0fbaf1afc2f6927f05b0fe43202d93ff5c1ef7c6207f95b16d2a769adb848524f5f9204ad04a3c15c2cca382fe1a6e72114b7b8e24afc940508602cfff216000df9ca870b606a0a73f1676a059e24b11fd357e34abb5ac6e041379baf1f6d54fcab21a45b15cd105cb917b0bf31867259120ac3d047455e47d9212c8bbe4320a0990cd6c456c394cfa1efa62ac680bdb9fa3a3e6a517a0c7420d181ab33cebdad745d7d7a4b2856bc25dbd328ad2d381e164994e27abb08c8ec535c96373eff8045bad2e1c7dc975c03630c4c50b6b3d37b3ac83cf7ce92caa1384f418c9094fc6c3c8b78ca846ad10b1939ff63a4554b00643e863c2111e767bb536a1ace8c6e5834a7e82f328a2d195a48567c0fbac0424a93bc765fedd2d50ba9bc7575bbd9dc1bacbd8da77f1f3573b9191e7b26773d7b6a6312f1657dc710ba74cb94833f5a19cad1f8184a3da8b8a1c04810a80a792bb5ffc63232951c31a333de53ddee4e4b894ba7afb15b186bf926e242fdaba8e41dfd3c5c341d092304e196c7ce7aa6378ae0335297e47e37d8d06054eb691a2edd316913b7366d8cc804c3eb33f79231597d178ef034cf70ac228ebbd2d313a83d7b6b56b09b6d72874c4def08c4f7a8a4882d519e6ed50ee1036dc279d4d55420e8e96d877268a22229011a98d354851cbbdfcf374b34c5da8533656c326529e301932cbf42c7258a9a1756ee48a687ee850b9ac2805bcd1e707e86cf168f0b014bbb4d6129e89641af7c9c2c96b15e43acb16c6a8fb46edbd32e44320d921c13a5b7efe3f63752569de0c9a1588f33a085bb1bead506e29682186daf040571a29179bf70f2bd3e6eb943fad8aacce3572a63f4d56911cdfbe22dbe381a8f8f364959403bef9f5fd60b596e29dcb2702e528c379eb755848b319a12988a3b93541575cfcd114649a232f855ccf836e182ed441676490cc4187ddbbdeba6bfec7fe92f930768840b636aef3200f8c0582e6f5dd082e45dae8b9bee0acebbbf55fed899dfd9f44bb234c3f67cd621f3868f5d0699b38760906193dc0b4104a0a0adc21843fbdabcca4ae91cd2717f669867891a4da4b4ca698eda2b2cce2a278176c4a2461cb2312a5afde12f7a79091398a5a95e7aee46fe08b39a24420095e1e8ec5c2e0eb120413e7ea4d1dbdf1189639804b986b2281335c0f334b6f9440d5fa776a3d0ae65b260820700dabe348488ffd5df5d8f7f2b722086fce2d9d1232cc38b3adb708f0773d625a1a0ed39085554b24dd2d5d4515149b896424fa47e400e1b70ac664d0878128c7abb809ade640c64cbb363f1676a059e24b11fd357e34abb5ac6ebfb692130267e16661875b49cf6c7dc0169d2bb16dba71b427b64e0721b40c903f1676a059e24b11fd357e34abb5ac6e6de52df6bf0861ad2fd02f26edc2c7cda63f4f86100a9f429cf3532b34a861d3df4eade3dd7d3856d5e218fd53b6f16075a0245bad58532dfad19eed30976ee434f4340297c71779be2a65f75b35cd486cc4abd480987c6090f675333ee5ad14d23f095550f358ec633df18232c3ad2bb2aaa3e4620d3e7df0b0c78081942397bcacd36b8c3ef60b188293900068e73ba7ed2389896d068c5bfec66d04dfef527abb21f47a11a8c9cd75d5919eb6ea05e3f40e925df0c6555fa27d10890c3be9e682a5705297ccaf0c6fa284536768e5b866201fd4f678c88664ba93d591e35d7da8ef6020674dd9b955a0fc406cd906489bce9dbb87813c1d9d6c6a8d1c81f5493727f58430d205e0b5cf3fe335f23c898065069cb6e804857f0485383301814eb0cf95c49712a0270edd8dc646b95d1ea93094273f2f557109619e722f987145fc21e109ab094e2139805051fd0b6082f896b812d1f86d2e0ad8b01aff911a63c6e4dc8ee47961a258057688ca8b0adc698c6e00d6337ca0360a6fbaec907a61b534caca0c293670773b22af6aa2e442e557a87b26e464b52825abfb0651b06b7ad3d1b688ef045b6d51b1c280fa956ecd7f1bbf6d1af3d395d42bc4cbcc028e8e533094e00d78730fe02c86e7d7c96e829b180c26ae8704dbe6e823eedf253dd4e873d87efec61462b12c5be4cbb61246bab28abff3fb2346b1f67454d8e6d615def16dbc64554caec884e4a8513845f97b1c8c7fc59b4ee74b26a448cf62eb2115c078a7237d88485c399ca7f89535e57dc538bd70b0d0690f94f36be708392f4e85ec97a694d7bcb57b95df9376965b2fa32285934eefb17c8511ed768522bd40143948c52b1ace33163be86ebc2bd3e6eb943fad8aacce3572a63f4d56e251464c813dc7d1bd504cbdb43cb5157d3119a9e1a5468b141f763e606f6485ab01941e1b278a872496145d5980632c154299606e0f1dca657be1859855fe4a5955d09f75399696ee30acf7999cf8c59f729c163daf6eb1a96604b7c36e063be5baf13830247fca6ba87eadf902fe3d6ab90c4aa8a5c4fe1ffba41c7c13470baaa3578f1a50c0d4acb5432dda206b063879ca92fe1e05d0bda12a94103d3ed57aee1eb4b7ef3dfda96dbb86b85195f89de4ef0cbeef9dc318aff38a79b58c8583d3ca43cdec2ecc73792fe12a9b78f770300d166b35360bb58692cab8d7b42cd82a8b6afe87212aef17723cad1651451522e4d9c353fe4b226a649ccfcc76537bba69ed7aa63336f791ed0a4e48f5be63972976ede359a9f3209f652efc44a5e9f7b254af4303779c77ba5302e67bf8628d0fe10368f76fcfa63e373c68cb2d965b2fa32285934eefb17c8511ed76851e5cb8f4ffdb9bd4e306be6ccb306825408c973819b0737b5e87af9623f11d992b8d743c3394c07b909105c7807f174c7cce16477bb357c2331141812168620e", "sign": "985ae5f37b8ac63e99405c452965cce7"}'
console.log(decryptData(t))