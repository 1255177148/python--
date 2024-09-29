import requests
import re
import os
import 创建文件时非法字符过滤 as fileClean

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}
response = requests.get("https://pic.netbian.com/", headers=headers)
# 通过发送请求成功response，通过(apparent_encoding)获取该网页的编码格式，并对response解码
response.encoding = response.apparent_encoding

# .*? 非贪婪匹配，只要匹配到第一个符合结束的，就结束，【.*】为贪婪匹配，一直匹配到最后一个符合结束的 
k = re.compile('src="(/u.*?)".alt="(.*?)"') # 正则表达
imageArr = re.findall(k, response.text)
path = "爬虫获取到的图片"
if not os.path.isdir(path):
    os.mkdir(path)
for image in imageArr:
    src = image[0]
    name = image[1]
    if name.startswith('/'):
        name = name[1:]
    with open(path + "/{}.jpg".format(fileClean.cleanFileName(name)), mode="wb") as file:
        res = requests.get("https://pic.netbian.com/" + src)
        file.write(res.content)
    print("图片" + name + ".jpg获取成功")