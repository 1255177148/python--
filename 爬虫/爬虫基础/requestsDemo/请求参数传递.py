import requests

base_url = "https://movie.douban.com/top250"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
}
params = {"start": "25", "filter": ""}

# 传递query参数
# res = requests.get(url=base_url,params=params,headers=headers)
# res.encoding = 'utf-8'
# print(res.text)
# 传递body参数
# 1、表单参数：form-data
#     request.post(url,data=字典参数)
# 2、json参数：
#     requets.post(url,json=字典参数)
baiduUrl = "https://fanyi.baidu.com/sug"
params = {"kw": "python"}
response = requests.post(url=baiduUrl, data=params, headers=headers)
response.encoding = "utf-8"
print(response.text)
