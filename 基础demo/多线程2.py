from threading import Thread
import time

# 线程之间，全局变量是共享的
li = []
def writeData():
    for i in range(5):
        li.append(i)
        time.sleep(1)
    print('写入的数据是：', li)

def readData():
    print('读取的数据是：', li)

if __name__ == '__main__':
    # 创建线程
    t1 = Thread(target=writeData)
    t2 = Thread(target=readData)
    t1.start()
    t1.join() # 使当前主线程阻塞，直到指定的线程运行完毕
    t2.start()
    t2.join()
    # 上面的两个线程之间共享了全局变量li