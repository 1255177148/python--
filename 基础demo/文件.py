# 打开文件
f = open("files/test.txt", encoding='utf-8')
s = f.read()
print(s)
f.close()
# 以上这种写法在最后必须要调用close()方法，有时候会忘记
# 下面用另一种写法，可以不用写close()方法
with open('files/test.txt', encoding='utf-8') as fil:
    print(fil.read())
    print(fil.closed)
print(fil.closed)

# 在写入模式的调用下，文件不能边写边读，因为写完后，指针会移动到文件末尾，这时在用read()读取读到的是空，
# 因为指针在末尾，后面没有数据，所以这个时候可以用tell()和seek()方法来查看指针位置并移动指针
with open('files/test.txt', 'a+', encoding='utf-8') as file:
    file.write('，真好笑')
    print('写完后立马读，读到的内容为：', file.read())
    print('当前指针位置：', file.tell())
    # 移动指针位置到开头
    # seek(offset, whence=0)里有两个参数，offset是偏移量，指的是从指定的位置(即whence)往后移动多少字节，
    # whence的值固定三个，0(文件开头，默认值)，1(当前位置)，2(文件末尾)
    file.seek(0, 0)
    print('移动指针后的指针位置:', file.tell())
    print('移动完指针后再读内容：', file.read())

# 上面的读取或者打开文件，默认都是以文本模式读取的，如果要读取图片之类的以二进制存放的，则就要以二级制模式读取文件
# 打开文件的参数mode值为b，则表示以二进制的方式读取或写入文件
with open('../爬虫/爬虫获取到的图片/金克丝，金克斯，猫，4K壁纸.jpg', 'rb') as fl:
    print('读取的图片文件二进制数据：', fl.read())