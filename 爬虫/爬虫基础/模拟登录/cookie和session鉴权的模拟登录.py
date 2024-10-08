import requests

# 这里模拟登录遇到了反爬虫拦截，以后有时间可以使用selenium模拟浏览器来模拟登录获取cookie

# 1、传递账号密码，进行登录
# 2、登录之后保存cookie
# 3、请求其他页面时，携带cookie

loginUrl = 'https://passport.17k.com/login/'

headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        'Referer':'https://www.17k.com/',
        'Accept':'*/*',
        'Cookie':'GUID=f8386a9e-2841-4480-a801-816cb3599f7c; c_channel=0; c_csc=web; acw_sc__v2=67053a2a805c67da79668f9f7abbff9cf6472e31; BAIDU_SSP_lcr=https://cn.bing.com/; Hm_lvt_9793f42b498361373512340937deb2a0=1728313048,1728395820; HMACCOUNT=3B317E916C806B58; acw_tc=2760828317283958382462777ed4ad0c5139afa491915443ad5ab28d300bf9; tfstk=gjDENhwhuppFDlpbflez08i5JheLEJYX8Ya7q0muAy43FBUur03TVTiutNYz74UQOJ0SzauI5y0r2HEur40zPXO6hDnLe8YjzK9jvA2ngBgUt9XMqurA-EtBFIvQe8YX516u9Ky-kXJnwHoMbuZPx60lEhPgqPX3q9qlShr8S8qux7VgIuZ5xwfnrcxa2P4ogmeuHNr7tnNmeBCv1tPaoD4NEtSYvWfZY_6ReArUTxi37WPEQkPUo5U_cNHn50DIp5dFt8nsg4looF1Q-jrq7SGeu9uqJumzq2JA0PDE4APK1wf30JzUivVDFnigZfkadvYRMcia-Sys1CLQNJuEMrFH6F3rbygoL5be5zGjfvVZoF6Zy7lodRDHSKSzzaEGRVk-TafutlEalh-wM3-PVPn6ij5RwWITbrt3t_C8tlEalh-Nw_FpklzXxWf..; Hm_lpvt_9793f42b498361373512340937deb2a0=1728396514; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22f8386a9e-2841-4480-a801-816cb3599f7c%22%2C%22%24device_id%22%3A%22192677c39dc889-071f1754060c53-26001051-1382400-192677c39dd1125%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fcn.bing.com%2F%22%2C%22%24latest_referrer_host%22%3A%22cn.bing.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%2C%22first_id%22%3A%22f8386a9e-2841-4480-a801-816cb3599f7c%22%7D; ssxmod_itna=7qIx2DgDR7D=YxBp4B4DKf38DyADBiGQDWwx2iuie2yKDsKmrDSxGKidDqxBWezwNFI7rxodmYZSAe5=jl8eWviolBPnhK+DB3DEx0=48CxYYzDt4DTD34DYDixibGxi5GRD0KDFCT5sz0xGWDm+kDWPDYxDrUhKDRxi7DDv=zx07DQHCFDDzFDfPYDGi=7GhdScwy1O1ejAxKBKD9poDsr+6FB9myILPZ6BL2bBdAx0k5q0Og1vsG1oP2ZvzetrqXAiqrQeYrAnoKlx4NhR9=AD5mAD3Yi45kBD5YcDoIUxyBkxDir0Q87DxD==; ssxmod_itna2=7qIx2DgDR7D=YxBp4B4DKf38DyADBiGQDWwx2iuie25ikUQFDl=G7xj+hRDUlQGF9cwD5CeWelexC=Y1niiaSzbGmWeSYKPYhCtttYAH6/UPQauCF5uW2SLDubQ/vIhq8vOqUN=CQUvWD0GQ+o9eRYGlLD2todGBAhwY7KqYEvPcurPGjxBIgwCD+54rx5htl30+nvx+SWh9nbMFmiFNjxdO4Aor2RvjpD1=YufClNkkYEoocWW5lyQa1IxP45bU80c+8nVFRPDKTmh6QvNDwwVYvBVisbcZ2DqD7=Deu4xD'

    }
session = requests.session()
response = session.get(url=loginUrl, headers=headers)
print(response.content.decode())

url = 'https://passport.17k.com/ck/user/login'

params = {
    'loginName':'18556976598',
    'password':'19941128ya!@#'
}

cookies={
    'RT':'"z=1&dm=baidu.com&si=ba87d40d-1efb-4088-af01-f8a848e71c73&ss=m1z48rx6&sl=1&tt=2la&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=3e5&ul=cr2&hd=crn"',
    'BAIDU_SSP_lcr':'https://cn.bing.com/',
    'BAIDUID':'CA29FAEC8992CEAF91F3655DD1A82A11:FG=1',
    'BDUSS':'9DdlY1ajZDc21zc0x6YklPNFU5SmJvY0lNeH5hNmtZZmhlYkNnR0FGR0p5dDVsSVFBQUFBJCQAAAAAAAAAAAEAAAAKz',
    'GUID':'f8386a9e-2841-4480-a801-816cb3599f7c'
}

# 发送请求进行登录
res = requests.post(url=url,data=params,headers=headers)
print(res.content.decode())