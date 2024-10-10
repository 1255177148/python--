import requests
from lxml import etree
import re
import json
from jsonpath import jsonpath

html_url = 'https://www.bilibili.com/video/BV1me2TYdEMG/?spm_id_from=333.1007.top_right_bar_window_dynamic.content.click&vd_source=f6a24697d164c409037b4a81d02627ca'
cookie = "buvid3=6CB1F980-6BAD-0ACF-32B7-C34B32A9604873484infoc; b_nut=1713767873; _uuid=22A81BA2-CBCC-F42B-ECBC-F104A632AC810E76458infoc; buvid_fp=a2f8defe23c38461ac49acbd377e11f7; b-user-id=90f43d8a-d64b-49d8-3ead-3a8b842a8beb; rpdid=|(umkY)RRluY0J'u~kRuumYuu; header_theme_version=CLOSE; enable_web_push=DISABLE; bmg_af_switch=1; bmg_src_def_domain=i1.hdslb.com; SESSDATA=ca608579%2C1744087073%2C35b0e%2Aa1CjCmfqRZeLW8ifKEM40aBJ6BCe7C0IwxP3y5NrMQb_bqvRquJjUVZAhGajoc6D3F34oSVjVmaGdVSWpDYnhsZDV0Nm1VOFlpVEx1c1NQSW1wWENuSTAyUUJQUkRSYnZlTU1kV0s3eXFQV0xaRjQ0ZnBUV0Nia245d0g4dUlhNlZ4NGV6bXNHQmhRIIEC; bili_jct=f0db4bceb51296eac442ae0c42d1a86c; DedeUserID=300238501; DedeUserID__ckMd5=59391fe1737bdf1b; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3Mjg3OTQzMDIsImlhdCI6MTcyODUzNTA0MiwicGx0IjotMX0.mQvSYGOO6FAZRSDT0_eMpFKHvCBV9g-hEwiZHAE1szo; bili_ticket_expires=1728794242; CURRENT_BLACKGAP=0; sid=8go36z7c; CURRENT_FNVAL=4048; VIP_DEFINITION_GUIDE=1; VIP_CONTENT_REMIND=1; buvid4=45559623-15FA-5144-E915-60245B7D03E374897-024042206-lTDs%2BIBTVnhWBxWWPupc1g%3D%3D; home_feed_column=4; browser_resolution=1159-150; bp_t_offset_300238501=986550805320433664; b_lsid=225EC2B8_19275102CBD"
        
headers = {
        'Referer':'https://www.bilibili.com/video/BV1mH2HYcENX/?',
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
# with open('获取到的b站页面数据.html', 'w', encoding='utf-8') as f:
#     f.write(res.content.decode())