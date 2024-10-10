import requests
from lxml import etree
import re
import json
from jsonpath import jsonpath

html_url = 'https://www.bilibili.com/video/BV1me2TYdEMG/?p=1&vd_source=f6a24697d164c409037b4a81d02627ca'
cookie = "LIVE_BUVID=AUTO9116012151887565; i-wanna-go-back=-1; FEED_LIVE_VERSION=V8; PVID=1; buvid3=B03083CC-64A8-8C2F-10B0-DD76CA9F6B2F76834infoc; b_nut=1710308276; b_ut=7; _uuid=AE10A44BA-15F1-945B-10276-F9D1F5635271052671infoc; home_feed_column=5; iflogin_when_web_push=0; header_theme_version=CLOSE; rpdid=0zbfVHgY7T|A5GuC2o6|3nd|3w1RMtqc; browser_resolution=1440-799; buvid4=F7BCADEA-5F3B-3F03-4AC3-EE454EC7EE5659254-024092014-aWG5Es%2BTkIkuubTYuTo%2Bug%3D%3D; DedeUserID=300238501; DedeUserID__ckMd5=59391fe1737bdf1b; enable_web_push=DISABLE; SESSDATA=33f0f93f%2C1744038530%2Ca161e%2Aa1CjDz6U2omTg5Sal2RojLLn1cj_LtqUrc1dS7RpudyYHqdY9q3cXcTb_76Dkd8dps14MSVkttMEo1YjhlaGZzek50WXpLU2ZwcXlvTmhJZ2g4OExlQWxRQklMYzNzbkI2NjhZY0RQSmd2anZnZHpneC1zZXh4LUtWdnBqTVE3dHRvMUw2RElNYUVRIIEC; bili_jct=b1b2a69735253f6287ddeb8483adea4c; fingerprint=b7b784dd8b6fd7143cf3d562ab7a1526; buvid_fp_plain=undefined; buvid_fp=b7b784dd8b6fd7143cf3d562ab7a1526; b_lsid=8CDEB1C1_19276BDF1BA; CURRENT_BLACKGAP=0; sid=65mcjum9; CURRENT_FNVAL=4048; CURRENT_QUALITY=120; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3Mjg4MjkzNzgsImlhdCI6MTcyODU3MDExOCwicGx0IjotMX0.urYgYqWMBM8Q1L-P9CahjcUqR3_vWUGt02Qy_0fMCsI; bili_ticket_expires=1728829318; bp_t_offset_300238501=986690799779446784; bsource=search_bing"
            
headers = {
        'Referer':'https://www.bilibili.com/',
        "Cookie": cookie,
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
    }
res = requests.get(url=html_url, headers=headers)
html = etree.HTML(res.content.decode())
source_data = html.xpath('/html/head/script[4]/text()')
print(source_data[0])
# json_source = re.search(r'__playinfo__=(.*?)</script><script>', source_data[0]).group()
# print(json_source)
json_data = re.sub('window.__playinfo__=','', source_data[0], 1)
with open('data.json', 'w', encoding='utf-8') as f:
    f.write(json_data)
json_o = json.loads(json_data)
video_url = jsonpath(json_o, '$.data.dash.video[0].base_url')
print(video_url)
# video_size = jsonpath(json_o, '$.result.video_info.dash.video[0].size')
# print(video_size)
video_max_range = jsonpath(json_o, '$.data.dash.video[0].SegmentBase.indexRange')
print(video_max_range)

audio_url = jsonpath(json_o, '$.data.dash.audio[0].base_url')
print(audio_url)
# audio_size = jsonpath(json_o, '$.result.video_info.dash.audio[0].size')
# print(audio_size)
audio_max_range = jsonpath(json_o, '$.data.dash.audio[0].SegmentBase.indexRange')
print(audio_max_range)
with open('获取到的b站页面数据.html', 'w', encoding='utf-8') as f:
    f.write(res.content.decode())