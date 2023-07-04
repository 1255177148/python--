with open("D://test.txt", mode="+ab") as file:
    # 这里试的是windows本地保存的文件，由于windows本地保存的文件默认格式为ANSI，所以这里的二进制编码格式也为ANSI
    file.write(",测试写入的追加内容".encode("ANSI"))