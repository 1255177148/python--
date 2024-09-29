import re

def cleanFileName(fileName):
    # 替换非法字符为下划线
    filename = re.sub(r'[\\/:"*?<>|]', '_', fileName)
    # 移除文件名开头的点和空格
    filename = filename.lstrip('. ')
    # 截断文件名以满足长度限制
    filename = filename[:255] 
    return filename