import requests

headers = {
        'Referer':'https://www.bilibili.com/video/BV1mH2HYcENX/?',
        "Cookie":'LIVE_BUVID=AUTO9116012151887565; CURRENT_FNVAL=4048; i-wanna-go-back=-1; FEED_LIVE_VERSION=V8; PVID=1; buvid3=B03083CC-64A8-8C2F-10B0-DD76CA9F6B2F76834infoc; b_nut=1710308276; b_ut=7; _uuid=AE10A44BA-15F1-945B-10276-F9D1F5635271052671infoc; home_feed_column=5; iflogin_when_web_push=0; header_theme_version=CLOSE; rpdid=0zbfVHgY7T|A5GuC2o6|3nd|3w1RMtqc; browser_resolution=1440-799; buvid4=F7BCADEA-5F3B-3F03-4AC3-EE454EC7EE5659254-024092014-aWG5Es%2BTkIkuubTYuTo%2Bug%3D%3D; DedeUserID=300238501; DedeUserID__ckMd5=59391fe1737bdf1b; enable_web_push=DISABLE; CURRENT_QUALITY=112; b_lsid=63365C910_19271D35599; SESSDATA=33f0f93f%2C1744038530%2Ca161e%2Aa1CjDz6U2omTg5Sal2RojLLn1cj_LtqUrc1dS7RpudyYHqdY9q3cXcTb_76Dkd8dps14MSVkttMEo1YjhlaGZzek50WXpLU2ZwcXlvTmhJZ2g4OExlQWxRQklMYzNzbkI2NjhZY0RQSmd2anZnZHpneC1zZXh4LUtWdnBqTVE3dHRvMUw2RElNYUVRIIEC; bili_jct=b1b2a69735253f6287ddeb8483adea4c; bp_t_offset_300238501=986331212232523776; sid=4v8atslf; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3Mjg3NDU3NTIsImlhdCI6MTcyODQ4NjQ5MiwicGx0IjotMX0.B_K4tWhzSVrhVMd21bSknoXfo2mQ8d1FmqUHkxI-NY8; bili_ticket_expires=1728745692; fingerprint=b7b784dd8b6fd7143cf3d562ab7a1526; buvid_fp_plain=undefined; buvid_fp=b7b784dd8b6fd7143cf3d562ab7a1526',
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
    }

url = 'https://xy123x246x94x68xy.mcdn.bilivideo.cn:8082/v1/resource/26200637457-1-30280.m4s?agrr=0&build=0&buvid=B03083CC-64A8-8C2F-10B0-DD76CA9F6B2F76834infoc&bvc=vod&bw=26981&deadline=1728493769&e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M%3D&f=u_0_0&gen=playurlv2&logo=A0020000&mcdnid=50004732&mid=300238501&nbs=1&nettype=0&og=hw&oi=1927025721&orderid=0%2C3&os=mcdn&platform=pc&sign=9e3400&traceid=trVlpqfnYutBjA_0_e_N&uipk=5&uparams=e%2Cuipk%2Cnbs%2Cdeadline%2Cgen%2Cos%2Coi%2Ctrid%2Cmid%2Cplatform%2Cog&upsig=50d8dbdd99ed4c37b6e674493dabbb71'
url2 = 'https://xy61x147x214x141xy.mcdn.bilivideo.cn:4483/upgcxcode/57/74/26200637457/26200637457-1-100027.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1728493769&gen=playurlv2&os=mcdn&oi=1927025721&trid=0000766c898002a545cd9a10ce7f34a9265eu&mid=300238501&platform=pc&og=hw&upsig=e58ba1b907839c93346735e6fa81e480&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform,og&mcdnid=50004732&bvc=vod&nettype=0&orderid=0,3&buvid=B03083CC-64A8-8C2F-10B0-DD76CA9F6B2F76834infoc&build=0&f=u_0_0&agrr=0&bw=147343&logo=A0020000'

res1 = requests.get(url=url, headers=headers)
res2 = requests.get(url=url2, headers=headers)

with open('sp1.mp4', 'wb') as f:
    f.write(res1.content)

with open('sp2.mp4', 'wb') as f:
    f.write(res2.content)

from moviepy.editor import ffmpeg_tools # 这是一个处理音视频剪辑的库
ffmpeg_tools.ffmpeg_merge_video_audio('sp1.mp4', 'sp2.mp4', '获得诺贝尔奖真的能加学分？！【司徒之脑洞】.mp4')