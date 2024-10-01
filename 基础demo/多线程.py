import threading
import time

# Thread线程类参数
# target: 执行的任务名
# args: 以元组的形式给任务传参
# kwargs: 以字典的形式给任务传参

def sing():
    print('现在唱歌')
    time.sleep(2)
    print('唱完歌了')

def dance():
    print('现在跳舞')
    time.sleep(2)
    print('跳完舞了')

if __name__ == '__main__':
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t1.daemon = True # 设置守护线程，必须放在start()之前，表示主线程结束时，此线程也会结束
    t2.daemon = True
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('表演完了')