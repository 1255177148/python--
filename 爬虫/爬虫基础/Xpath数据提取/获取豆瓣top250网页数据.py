import requests
from lxml import etree # 使用这个包可以用xpath解析html

url = 'https://movie.douban.com/top250'
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
}

res = requests.get(url=url,headers=headers) # 获取html页面内容
res.encoding = 'utf-8'
html = etree.HTML(res.text) # 将html字符串转为xml文档对象
# 使用xpath提取页面数据
dataList = html.xpath('//ol[@class="grid_view"]/li')
for item in dataList:
    title = item.xpath('.//span[@class="title"][1]/text()') # text()是获取文本数据
    score = item.xpath('.//span[@class="rating_num"][1]/text()')
    print(f'电影名称：{title[0]}   评分：{score[0]}')