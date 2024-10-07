import requests
from lxml import etree

'''
分页抓取思路:
1、准备好要抓取的数据的所有url地址
2、遍历列表中的url地址,进行抓取
'''
class DouBan:
    
    base_url = 'https://movie.douban.com/top250?start={}&filter='
    
    headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
    }
    
    def __init__(self) -> None:
        self.urlList = []
        for i in range(10):
            self.urlList.append(self.base_url.format(i * 25))

    def getData(self, url):
        '''
        根据传入的url获取每一页的数据
        '''
        res = requests.get(url=url,headers=self.headers) # 获取html页面内容
        res.encoding = 'utf-8'
        html = etree.HTML(res.text) # 将html字符串转为xml文档对象
        # 使用xpath提取页面数据
        dataList = html.xpath('//ol[@class="grid_view"]/li')
        for item in dataList:
            title = item.xpath('.//span[@class="title"][1]/text()') # text()是获取文本数据
            score = item.xpath('.//span[@class="rating_num"][1]/text()')
            num = item.xpath('.//div[@class="pic"]/em/text()')
            print(f'排名：{num[0]}  电影名称：{title[0]}   评分：{score[0]}')
    
    def runPageData(self):
        '''
        获取所有分页数据
        '''
        for url in self.urlList:
            self.getData(url)

if __name__ == '__main__':
    douBan = DouBan()
    douBan.runPageData()