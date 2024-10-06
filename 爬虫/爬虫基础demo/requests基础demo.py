import requests
# 设置请求头
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
}

res = requests.get('https://www.baidu.com', headers= headers)
res.encoding = 'utf-8'
# 返回字符串返回数据
print(res.text)
# 返回字节字符串，即二进制字符串
# print(res.content)
# # 获取请求头信息
# print(res.request.headers)

# # 字符串和二进制字符之间的转换
# s = '你好啊'
# print(s.encode()) #将字符串转为二进制字符

# print(s.encode().decode()) # 将二进制字符转为字符串

