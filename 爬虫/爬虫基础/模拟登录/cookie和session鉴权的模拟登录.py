import requests

# 1、传递账号密码，进行登录
# 2、登录之后保存cookie
# 3、请求其他页面时，携带cookie

url = 'https://passport.17k.com/ck/user/login'
headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        'Referer':'https://passport.17k.com/login/',
        'Accept':'*/*',
        'Origin':'https://passport.17k.com'
    }
params = {
    'loginName':'18556976598',
    'password':'19941128ya!@#'
}

cookies={
    'RT':'"z=1&dm=baidu.com&si=ba87d40d-1efb-4088-af01-f8a848e71c73&ss=m1z48rx6&sl=1&tt=2la&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=3e5&ul=cr2&hd=crn"',
    'BAIDU_SSP_lcr':'https://cn.bing.com/',
    'BAIDUID':'CA29FAEC8992CEAF91F3655DD1A82A11:FG=1',
    'BDUSS':'9DdlY1ajZDc21zc0x6YklPNFU5SmJvY0lNeH5hNmtZZmhlYkNnR0FGR0p5dDVsSVFBQUFBJCQAAAAAAAAAAAEAAAAKz',
    'GUID':'f8386a9e-2841-4480-a801-816cb3599f7c'
}

# 发送请求进行登录
res = requests.post(url=url,data=params,headers=headers)
print(res.content.decode())