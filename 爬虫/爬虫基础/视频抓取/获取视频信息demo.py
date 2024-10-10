import requests

referer = 'https://www.bilibili.com/bangumi/play/ss12548?theme=movie&from_spmid=666.7.operation.0'
cookie = "buvid3=6CB1F980-6BAD-0ACF-32B7-C34B32A9604873484infoc; b_nut=1713767873; _uuid=22A81BA2-CBCC-F42B-ECBC-F104A632AC810E76458infoc; buvid_fp=a2f8defe23c38461ac49acbd377e11f7; b-user-id=90f43d8a-d64b-49d8-3ead-3a8b842a8beb; rpdid=|(umkY)RRluY0J'u~kRuumYuu; b_lsid=C2177F49_19274B7BC66; header_theme_version=CLOSE; enable_web_push=DISABLE; home_feed_column=5; bmg_af_switch=1; bmg_src_def_domain=i1.hdslb.com; SESSDATA=ca608579%2C1744087073%2C35b0e%2Aa1CjCmfqRZeLW8ifKEM40aBJ6BCe7C0IwxP3y5NrMQb_bqvRquJjUVZAhGajoc6D3F34oSVjVmaGdVSWpDYnhsZDV0Nm1VOFlpVEx1c1NQSW1wWENuSTAyUUJQUkRSYnZlTU1kV0s3eXFQV0xaRjQ0ZnBUV0Nia245d0g4dUlhNlZ4NGV6bXNHQmhRIIEC; bili_jct=f0db4bceb51296eac442ae0c42d1a86c; DedeUserID=300238501; DedeUserID__ckMd5=59391fe1737bdf1b; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3Mjg3OTQzMDIsImlhdCI6MTcyODUzNTA0MiwicGx0IjotMX0.mQvSYGOO6FAZRSDT0_eMpFKHvCBV9g-hEwiZHAE1szo; bili_ticket_expires=1728794242; CURRENT_BLACKGAP=0; sid=8go36z7c; CURRENT_FNVAL=4048; VIP_DEFINITION_GUIDE=1; VIP_CONTENT_REMIND=1; buvid4=45559623-15FA-5144-E915-60245B7D03E374897-024042206-lTDs%2BIBTVnhWBxWWPupc1g%3D%3D; browser_resolution=1920-455"

headers = {
    'Referer': referer,
    'Cookie':cookie,
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
}

url = 'https://xy180x97x245x56xy.mcdn.bilivideo.cn:4483/upgcxcode/85/81/34568185/34568185_p1-1-100111.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1728544376&gen=playurlv2&os=mcdn&oi=1926844647&trid=0000424ed459e40c444d9f7b9aa2f8dd09c5p&mid=300238501&platform=pc&og=hw&upsig=f4e27561e90e00d12404714d3824afa1&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform,og&mcdnid=50010948&bvc=vod&nettype=0&orderid=0,3&buvid=6CB1F980-6BAD-0ACF-32B7-C34B32A9604873484infoc&build=0&f=p_0_0&agrr=0&bw=45515&logo=A0020000'
