import gevent
from gevent import monkey

monkey.patch_all()  # 这里使用了monkey
import requests
import time
import math
from openpyxl import Workbook
import copy


class TencentRecruit:
    # 先获取岗位的筛选条件列表数据
    selectListUrl = "https://careers.tencent.com/tencentcareer/api/data/GetMultiDictionary"  # 筛选框字典数据接口
    recruitUrl = (
        "https://careers.tencent.com/tencentcareer/api/post/Query"  # 招聘信息分页接口
    )
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
    }
    params = {
        "timestamp": int(time.time() * 1000),
        "language": "zh-cn",
        "type": "Nationality,WorkPlace,OuterType,BG,PostAttr",
    }

    def getSelectData(self):
        """
        获取腾讯招聘左侧筛选框的数据
        """
        res = requests.get(
            url=self.selectListUrl, params=self.params, headers=self.headers
        )
        jsonData = res.json()["Data"]
        return jsonData

    def handleSelect(self, jsonData, key):
        """
        组合筛选框的数据
        """
        res = jsonData[key]
        list = []
        for item in res:
            sub = {}
            sub["code"] = item["Code"]
            sub["name"] = item["Name"]
            sub["parentId"] = item["ParentId"]
            list.append(sub)
        return list

    def getPageData(self, params):
        """
        获取招聘信息
        """
        list = []
        data = self.sendPageRequest(params)
        if data["Posts"]:
            list.extend(data["Posts"])
        # 获取分页总条数
        pageCount = int(data["Count"])
        # 获取单页容量
        pageSize = int(params["pageSize"])
        # 计算出总页数,去掉第一页，因为第一页的数据已经获取出来了
        pageTotalNum = math.ceil(
            pageCount / pageSize
        )  # 使用math.ceil向上取整，即如果有小数，则整数部分+1，然后只取最后的整数部分
        job_list = []
        for i in range(2, pageTotalNum + 1):
            params["timestamp"] = int(time.time() * 1000)
            params["pageIndex"] = i
            job_list.append(gevent.spawn(self.sendPageRequest, copy.deepcopy(params))) # 这里使用gevent协程,注意，这里的params要用深拷贝，不然下一个循环改了值之后，会影响循环里的其他的请求参数
        gevent.joinall(job_list)
        result_list = [job_object.value for job_object in job_list] # 这里for循环依次获取协程执行的函数返回的结果
        for data in result_list:
            if data["Posts"]:
                list.extend(data["Posts"])
        return list

    def sendPageRequest(self, params):
        res = requests.get(url=self.recruitUrl, headers=self.headers, params=params)
        data = res.json()["Data"]
        return data
    
    def exportData(self, data):
        '''
        导出数据到excel表里
        '''
        title_list = ['职位名称','工作地点','所属事业群','职业类别','需要工作年限','职位最后更新时间','工作职责'] # 表头
        list = []
        list.append(title_list)
        for item in data:
            list.append([item['RecruitPostName'], item['LocationName'], item['BGName'], item['CategoryName'], item['RequireWorkYearsName'], item['LastUpdateTime'], item['Responsibility']])
        workbook = Workbook()
        sheet = workbook.active # 激活sheet，一般默认的第一个sheet是使用workbook.active激活并创建，后续如果想创建并写入多个sheet，则后面可以用wb.create_sheet(title="表头名")来创建sheet
        sheet.title = '腾讯招聘信息'
        for i in list:
            sheet.append(i)
        workbook.save('腾讯招聘信息.xlsx')


if __name__ == "__main__":
    tencentRecruit = TencentRecruit()
    selectData = tencentRecruit.getSelectData()
    # selectList = []
    # for key in selectData.keys():
    #     selectList.append(tencentRecruit.handleSelect(selectData, key))
    # 上面注释的是获取所有的筛选框数据，现在测试，不用勾选全部筛选框
    oneSelectParam = tencentRecruit.handleSelect(selectData, "OuterType")
    selectParamCodes = []
    for item in oneSelectParam:
        if item["parentId"] and (
            "40003" == item["parentId"] or "40004" == item["code"]
        ):
            selectParamCodes.append(item["code"])
    selectParamCode = ",".join(selectParamCodes)
    params = {
        "timestamp": int(time.time() * 1000),
        "language": "zh-cn",
        "categoryId": selectParamCode,
        "pageIndex": 1,
        "pageSize": 10,
        "area": "cn",
    }
    dataList = tencentRecruit.getPageData(params=params)
    tencentRecruit.exportData(dataList)
