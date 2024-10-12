import requests
import time
import execjs  # 调用并执行js代码
import re
from urllib import parse

# d.token + "&" + i + "&" + g + "&" + c.data
cookie = "cna=ZVTjF0EsgVMCAd5dTXyZlqYP; __cn_logon__=false; xlly_s=1; mtop_partitioned_detect=1; _m_h5_tk=828115a3bee338e0c160d1fb4c7637e1_1728750966200; _m_h5_tk_enc=80473bf5245f3bbf6da0d09210de9257; cookie2=162e2287e9d88ca4d9ddf4ff8310a710; t=5b15be059eef8c7c2293ced3aafbddee; _tb_token_=de3e88a38b1e; _m_h5_tk=a9011c573f0c91f197c1f382b932b233_1728756646516; _m_h5_tk_enc=aea7e1db7ba738e18462d134474a5d64; isg=BIOD9k1u4ODaSqwXlybBgD1WEkct-Bc6FdLyo7VgWuJYdKOWPcjZimen7gQ6Um8y; tfstk=gEIrQhto_uEysJq6hKKeQ8Z8LCtJv3V1ZMOBK9XHFQAkNzeEYIJE-XmhKB5FGIQQe7dCTeXWM6O5F8QqLOC2A6WLepAht6RCPrZ1eTKpx51Ufl6JtXpA5g-nOtXRu8Z1ylZ1eTxpx5N_fga8OARktHYkZncDML0ot6YnmtAvppckxQ2VnIdmxLYkEIADBLlot6x33tAvKbtJxhh2dU2sU9G6Q7zA8CXkgDmZBL8uTTuIxDmkEURMPIoHziJyzCXlV0sFoKjf0FTjd7KcBZ1k3hrr6L7cQ3vFvR0eTeSJ0I5ajDpAr_SD8iwLytSeaFjkuYyRU3vhte7Y_c9yVZ8N4aeKiTf6aNxRdAP53F72WKYmL4x55OspSgqr6IT9Ls81z5oPsgux9Kc5gMQrt28kHKR_3-zTLJkQCFOUh23pyxp218YoJ2LkHKR_3-uKJUF93Cwkr"
headers = {
    "Referer": 'https://sale.1688.com/',
    "Cookie": cookie,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
}
token = re.findall('_m_h5_tk=(.+?)_', headers['Cookie'], re.S)[0]
i = round(time.time() * 1000)  # 时间戳
g = "12574478"
data = r'{"cid":"TpFacRecommendService:TpFacRecommendService","methodName":"execute","params":"{\"pageNo\":\"1\",\"cna\":\"ZVTjF0EsgVMCAd5dTXyZlqYP\",\"pageSize\":\"20\",\"from\":\"PC\",\"sort\":\"mix\",\"trafficSource\":\"pc_index_recommend\"}"}'
sign_key = token + "&" + str(i) + "&" + g + "&" + data
with open("1688sign加密.js", "r", encoding="utf-8") as f:
    js_code = f.read()
ctx = execjs.compile(js_code).call("h", sign_key)
params = {
    "jsv": "2.6.1",
    "appKey": "12574478",
    "t": i,
    "sign": ctx,
    "v": "1.0",
    "type": "jsonp",
    "isSec": 0,
    "timeout": 20000,
    "api": "mtop.taobao.widgetService.getJsonComponent",
    "dataType": "jsonp",
    "jsonpIncPrefix": "mboxfc",
    "callback": "mtopjsonpmboxfc8",
    "data": data,
}


res = requests.get(url='https://h5api.m.1688.com/h5/mtop.taobao.widgetservice.getjsoncomponent/1.0/', headers=headers, params=params)
print(res.text)
