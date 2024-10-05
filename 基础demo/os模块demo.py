import os

# os模块
# 作用：用于和操作系统进行交互
# 1、os.name  指示正在使用的工作平台（返回操作系统类型）
print(os.name) # 对于windows,返回nt,对于linux,返回posix
# 2、os.getenv(环境变量名称)  读取指定的环境变量
print(os.getenv('path'))
# 3、os.path.split() 把目录名和文件名分离，以元组的形式接收，第一个元素是目录名，第二个是文件名
print(os.path.split(r'E:\自学项目\pythonDemo\基础demo\os模块demo.py'))
# 4、os.path.dirname  显示split分割的第一个元素，即目录名
# 5、os.path.basename  显示split分割的第二个元素，即文件名
print(os.path.dirname(r'E:\自学项目\pythonDemo\基础demo\os模块demo.py'))
print(os.path.basename(r'E:\自学项目\pythonDemo\基础demo\os模块demo.py'))
# 6、os.path.exists()  判断路径(文件或目录)是否存在
print(os.path.exists(r'E:\自学项目\pythonDemo\基础demo\os模块demo.py'))
# 7、os.path.isfile()  判断是否存在文件
print(os.path.isfile(r'E:\自学项目\pythonDemo\基础demo')) # 传入目录的话就会返回False
# 8、os.path.isdir()   判断目录是否存在
print(os.path.isdir(r'E:\自学项目\pythonDemo\基础demo\os模块demo.py')) # 传入文件路径的话就会返回False，只能判断目录路径
# 9、os.path.abspath()  获取当前路径的绝对路径
print(os.path.abspath('os模块demo.py'))
# 10、os.path.isabs()   判断是否是绝对路径
print(os.path.isabs(r'E:\自学项目\pythonDemo\基础demo\os模块demo.py'))