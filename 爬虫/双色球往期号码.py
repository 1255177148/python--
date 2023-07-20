import requests
import ast
import pylab
import numpy as np


headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

res = requests.get('http://www.cwl.gov.cn/cwl_admin/front/cwlkj/search/kjxx/findDrawNotice?name=ssq&issueCount=&issueStart=&issueEnd=&dayStart=&dayEnd=&pageNo=1&pageSize=100&week=&systemType=PC', headers=headers)
# 通过发送请求成功res，通过(apparent_encoding)获取该网页的编码格式，并对res解码
res.encoding = res.apparent_encoding
# print(res.text)
result = ast.literal_eval(res.text)  # 将json字符串反序列化为字典格式的数据
resultList = result.get("result")
x = list()  # X轴，时间坐标
num1 = list()  # 双色球第一位
num2 = list()  # 双色球第二位
num3 = list()  # 双色球第三位
num4 = list()  # 双色球第四位
num5 = list()  # 双色球第五位
num6 = list()  # 双色球第六位
num7 = list()  # 双色球第七位
for data in resultList:
    # print(data)
    # map = ast.literal_eval(data)
    red = data["red"]
    blue = data["blue"]
    num = red + "," + blue
    code = list(num.split(","))
    dateStr = data["date"]
    index = 0
    for i, eachChar in enumerate(dateStr):
        if "(" == eachChar:
            index = i
            break
    # print(dateStr[0:index])
    x.append(dateStr[0:index])
    num1.append(int(code[0]))
    num2.append(code[1])
    num3.append(code[2])
    num4.append(code[3])
    num5.append(code[4])
    num6.append(code[5])
    num7.append(code[6])
x.reverse()
print(len(num1))
print(len(x))

# 画折线图
pylab.rcParams['font.sans-serif'] = ['SimHei'] # 指定默认字体
pylab.rcParams['axes.unicode_minus'] = False # 显示负号，坐标轴上的负号显示
pylab.xticks(rotation = 50)
pylab.yticks(range(34))
pylab.ylim(0, 33)
pylab.scatter(x, num1)
pylab.show()