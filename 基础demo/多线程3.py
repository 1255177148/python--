from threading import Thread, Lock
import time

# 线程间的资源抢占，因为线程间全局变量是共享的，所以多个线程间会对同一个全局变量进行资源抢夺
a = 0
b = 1000000
lock = Lock()

def add():
    lock.acquire() # 加互斥锁
    for i in range(b):
        global a # 这里要声明全局变量，因为下面要给a重新赋值，所以要声明a是全局变量
        '''
        这里相当于 a = a + 1,这里是声明a并给a赋值,这里如果不在上面声明a是全局变量,
        则这里会认为a是局部变量,所以要用global声明a是上面那个全局变量
        '''
        a += 1
    print('第一次遍历相加：', a)
    lock.release() # 释放锁

def add2():
    lock.acquire()
    for i in range(b):
        global a # 这里要声明全局变量，因为下面要给a重新赋值，所以要声明a是全局变量
        '''
        这里相当于 a = a + 1,这里是声明a并给a赋值,这里如果不在上面声明a是全局变量,
        则这里会认为a是局部变量,所以要用global声明a是上面那个全局变量
        '''
        a += 1
    print('第二次遍历相加：', a)
    lock.release()

if __name__ == '__main__':
    t1 = Thread(target=add)
    t2 = Thread(target=add2)
    t1.start()
    t2.start()
    # 上面这段在没有加锁的时候，执行的结果会不一样，原本第一次相加会是1000000，第二次相加是2000000
    # 下面会将锁加上再试下，使用Lock()来加锁，在函数里加