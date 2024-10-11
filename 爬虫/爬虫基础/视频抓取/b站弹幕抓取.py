import requests
import re
import jieba  # 中文分词器
from wordcloud import wordcloud  # 制作词云
import matplotlib.pyplot as plt  # 绘图

base_url = "https://api.bilibili.com/x/v2/dm/web/history/seg.so"

params = {
    "type": 1,
    "oid": "34568185",
    "date": "2024-10-01",
    # "pid": "21071819",
    # "wts": "1728626287",
    # "w_rid": "a28f00d5e810fd2892f6ff25ba8dfec0",
    # "pull_mode": 1,
    # "ps":0,
    # "pe":"120000",
    # "web_location":"1315873",
    # "segment_index":1
}
cookie = "buvid3=6CB1F980-6BAD-0ACF-32B7-C34B32A9604873484infoc; b_nut=1713767873; _uuid=22A81BA2-CBCC-F42B-ECBC-F104A632AC810E76458infoc; buvid_fp=a2f8defe23c38461ac49acbd377e11f7; rpdid=|(umkY)RRluY0J'u~kRuumYuu; header_theme_version=CLOSE; enable_web_push=DISABLE; SESSDATA=ca608579%2C1744087073%2C35b0e%2Aa1CjCmfqRZeLW8ifKEM40aBJ6BCe7C0IwxP3y5NrMQb_bqvRquJjUVZAhGajoc6D3F34oSVjVmaGdVSWpDYnhsZDV0Nm1VOFlpVEx1c1NQSW1wWENuSTAyUUJQUkRSYnZlTU1kV0s3eXFQV0xaRjQ0ZnBUV0Nia245d0g4dUlhNlZ4NGV6bXNHQmhRIIEC; bili_jct=f0db4bceb51296eac442ae0c42d1a86c; DedeUserID=300238501; DedeUserID__ckMd5=59391fe1737bdf1b; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3Mjg3OTQzMDIsImlhdCI6MTcyODUzNTA0MiwicGx0IjotMX0.mQvSYGOO6FAZRSDT0_eMpFKHvCBV9g-hEwiZHAE1szo; bili_ticket_expires=1728794242; CURRENT_BLACKGAP=0; buvid4=45559623-15FA-5144-E915-60245B7D03E374897-024042206-lTDs%2BIBTVnhWBxWWPupc1g%3D%3D; bp_t_offset_300238501=986605501728948224; home_feed_column=5; browser_resolution=1920-919; sid=5448fd3i; CURRENT_FNVAL=4048; b_lsid=622BF6109_1927A3E0597"
referer = "https://www.bilibili.com/bangumi/play/ep199612?theme=movie&from_spmid=666.25.episode.0"
headers = {
    "Referer": referer,
    "Cookie": cookie,
    "Origin": "https://www.bilibili.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
}
res = requests.get(url=base_url, params=params, headers=headers)
# print(res.text)
content_list = re.findall("[\u4e00-\u9fa5]+", res.text)
content = "\n".join(content_list)
with open("弹幕.text", "a", encoding="utf-8") as f:
    f.write(content)
# 使用分词
delete_list = {"了", "\n", "的", "是", "但", "吗", "才"}
jieba.load_userdict("custom_dict.text")
with open("弹幕.text", "r", encoding="utf-8") as f:
    text_list = jieba.lcut(f.read())
    wc = wordcloud.WordCloud(
        font_path="../../../font/MSYH.TTC",
        background_color="white",
        max_font_size=30,
        min_font_size=10,
        stopwords=delete_list,
    )
    wc.generate(",".join(text_list))
    wc.to_file('image.png')
    plt.imshow(wc) # 创建图像
    plt.axis('off') #关闭坐标轴
    plt.show()
