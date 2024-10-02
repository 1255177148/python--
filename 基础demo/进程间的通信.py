# 进程间的通信主要使用queue来通信
from multiprocessing import Process, Queue
import time
# from queue import Queue #这里的queue队列是用于多线程的，如果要用进程的队列，则在multiprocessing中导入

# 初始化一个队列对象
# q = Queue(3) # 最多可以接受3条消息，如果这里没有传参数或者传负数，则表示接受消息条数没有上限，直到耗尽内存
# q.put('消息一') # 放入一条消息
# q.put('消息二')
# q.put('消息三')

# print(q.get()) # 获取一条消息，先入先出run

def writeData(q1):
    for i in range(5):
        q1.put(i)
        time.sleep(0.1)

def readData(q2):
    while not q2.empty():
        print('取出的数据是：', q2.get())

if __name__ == '__main__':
    q = Queue()
    p1 = Process(target=writeData, args=(q,))
    p2 = Process(target=readData, args=(q,))
    p1.start()
    p1.join()
    p2.start()
    p2.join()