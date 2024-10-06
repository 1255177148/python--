import requests

# 设置请求头
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
}
url = 'https://search-operate.cdn.bcebos.com/b0716a9ac381875c1509966978467e3d.gif'

res = requests.get(url=url, headers=headers)

with open('baidu.gif', '+ab') as f:
    f.write(res.content)