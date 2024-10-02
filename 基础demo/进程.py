# 一个正在运行的程序或者软件就是一个进程
# 程序跑起来就成了进程
# 一个进程里可以有多个线程
# 注意，进程间不共享全局变量

# 进程的状态
# 1、就绪状态：运行的条件都已经满足，正在等待CPU执行
# 2、执行状态：CPU正在执行
# 3、等待(阻塞)状态：等在某些条件满足，比如程序sleep了，此时就处于等待状态

# 进程语法结构
# multiprocessing模块提供了Process类代表进程对象
# Process类参数
# 1、target:执行的目标任务名，即子进程要执行的任务
# 2、args:以元组的形式传参
# 3、kwargs:以字典的形式传参
# 常用方法
# 1、start():开启子进程
# 2、is_alive():判断子进程是否在存活
# 3、join():主进程等待子进程执行完毕
# 常用属性
# 1、name:当前进程的别名。默认Process-N
# 2、pid:当前进程的进程编号

from multiprocessing import Process
import os

def sing(name, person):
    print('唱歌进程的编号:', os.getpid())
    print('唱歌父进程的编号:', os.getppid())
    print(f'{name}在唱歌唱歌, {person}也在唱歌')

def dance(name, person):
    print('跳舞进程的编号:', os.getpid())
    print('跳舞父进程的编号:', os.getppid())
    print(f'{name}在跳舞,{person}也在跳舞')

if __name__ == '__main__':
    # 创建子进程
    p1 = Process(target=sing, name='子进程1', args=('小白', '小明'))
    p2 = Process(target=dance, name='子进程2', kwargs={'name':'小红', 'person': '小兰'})
    p1.start()
    p2.start()
    # 访问子进程名称
    print('p1子进程名称：', p1.name)
    print('p2子进程名称：', p2.name)
    # 获取子进程的进程编号
    print('p1子进程编号：', p1.pid)
    print('p2子进程编号：', p2.pid)
    # 主进程的进程编号
    print('主进程编号：', os.getpid())