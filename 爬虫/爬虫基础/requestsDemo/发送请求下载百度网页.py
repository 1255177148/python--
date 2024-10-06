import requests

# 设置请求头
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
}

res = requests.get('https://www.baidu.com', headers=headers)
res.encoding = 'utf-8'
with open('baidu.html', '+a', encoding='utf-8') as f:
    f.write(res.text)