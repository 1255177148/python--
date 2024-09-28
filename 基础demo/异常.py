# 抛出异常
# raise Exception("抛出了一个异常")
# 捕获异常
def login():
    pwd = input("请输入一个密码:")
    if len(pwd) >= 6:
        return "密码输入成功"
    raise Exception("密码输入失败")
try:
    print(login())
except Exception as e :
    print(e)

print('代码继续执行')