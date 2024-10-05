import sys
# 作用，负责程序和python解释器的交互
# 1、sys.getdefaultencoding()  获取系统默认编码格式
print(sys.getdefaultencoding())
# 2、sys.path  获取环境变量的路径，和解释器相关的
print(sys.path) # 获取python可以搜索包的路径列表
# 3、sys.platform  获取操作系统平台名称
print(sys.platform)
# 4、sys.version  获取python解释器的版本
print(sys.version)