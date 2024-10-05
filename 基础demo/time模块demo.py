import time
# 三种时间表示
# 1、时间戳(timestamp)
print(time.time())  #获取到当前的时间戳，以秒计算，从1970年1月1日 0点0时0分开始到现在的时间差，返回的是浮点型
# 2、格式化的时间字符串
print(time.asctime())
# 3、时间元组
print(time.localtime())

# 时间间的转换
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())) #将时间转换为指定格式的时间字符串
print(time.strptime('2024-09-01', '%Y-%m-%d')) #将时间字符串以指定的格式转换为时间元组