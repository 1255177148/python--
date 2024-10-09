import gevent
from gevent import monkey

monkey.patch_all()  # 这里使用了monkey
import requests
import time
import math


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
            list.append(data["Posts"])
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
            job_object = gevent.spawn(self.sendPageRequest, params)
            job_list.append(job_object)
        gevent.joinall(job_list)
        result_list = [job_object.value for job_object in job_list]
        for data in result_list:
            if data["Posts"]:
                list.append(data["Posts"])
        return list

    def sendPageRequest(self, params):
        res = requests.get(url=self.recruitUrl, headers=self.headers, params=params)
        data = res.json()["Data"]
        return data


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
    print(dataList)
