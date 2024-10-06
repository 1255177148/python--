import requests

headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
}

url = 'https://m804.music.126.net/20241006161758/a61af55d2256712f55d7ed16497c9f11/jdyyaac/obj/w5rDlsOJwrLDjj7CmsOj/14096443364/1ef1/fbcb/0f38/b9da5caf7a4a498bb7505ed42cbd8d93.m4a?authSecret=0000019260d13e5302d60a8ab2b40006'
res = requests.get(url=url,headers=headers)
with open('罗生门.m4a','wb') as f:
    f.write(res.content)