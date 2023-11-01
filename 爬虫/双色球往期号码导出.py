import requests
import ast
import pylab
import numpy as np
from openpyxl import Workbook

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

res = requests.get('http://www.cwl.gov.cn/cwl_admin/front/cwlkj/search/kjxx/findDrawNotice?name=ssq&issueCount=&issueStart=&issueEnd=&dayStart=&dayEnd=&pageNo=1&pageSize=100&week=&systemType=PC', headers=headers)
# 通过发送请求成功res，通过(apparent_encoding)获取该网页的编码格式，并对res解码
res.encoding = res.apparent_encoding
# print(res.text)
result = ast.literal_eval(res.text)  # 将json字符串反序列化为字典格式的数据
resultList = result.get("result")
numList = list()   # 双色球往期号码集合
for data in resultList:
    # print(data)
    # map = ast.literal_eval(data)
    red = data["red"]
    blue = data["blue"]
    num = red + "," + blue
    numList.append(list(num.split(",")))

workbook = Workbook()

sheet = workbook.active
sheet.title = '往期号码'
for data in numList:
    sheet.append(data)
workbook.save('往期号码.xlsx')