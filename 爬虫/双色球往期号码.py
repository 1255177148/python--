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
    num2.append(int(code[1]))
    num3.append(int(code[2]))
    num4.append(int(code[3]))
    num5.append(int(code[4]))
    num6.append(int(code[5]))
    num7.append(int(code[6]))
x.reverse()
print(len(num1))
print(len(x))

# 画折线图
pylab.rcParams['font.sans-serif'] = ['SimHei'] # 指定默认字体
pylab.rcParams['axes.unicode_minus'] = False # 显示负号，坐标轴上的负号显示
pylab.ylim(0, 17)
pylab.scatter(x, num7)
'''
默认画出的图，一般有四条轴，横坐标轴两条，分别是上(top)和下(buttom)，纵坐标轴两条，分别是左(left)和右(right)，
现在我们想画出一般数学课上学的笛卡尔坐标系，只有两个坐标轴，那么就分别去掉横坐标的上(top)轴，和纵坐标的右(right)轴
'''
axes = pylab.gca() # 获取当前的坐标轴
axes.spines['right'].set_color('none') # 右轴的颜色设置为空
axes.spines['top'].set_color('none') # 上轴的颜色设置为空
axes.spines['bottom'].set_position(('data', 0)) # 这里的data指的是纵坐标的值，也就是指将横坐标水平移动到纵坐标值为0的位置
axes.spines['left'].set_position(('axes', 0.046)) # 这里的axes指的就是坐标轴，也就是指将纵坐标移到横坐标4.6%的位置
axes
pylab.xticks(rotation = 50)
pylab.yticks(range(17))
pylab.show()