# 协程--在线程之下，也成为微线程
# 通过greenlet实现任务之间的切换
# greenlet属于手动操作，当遇到IO操作时，程序会阻塞，不能自动切换
from greenlet import greenlet

def sing():
    print('在唱歌')
    g2.switch() # 这里会切换到g2指定的任务执行
    print('唱完歌了')

def dance():
    print('在跳舞')
    print('跳完舞了')

if __name__ == '__main__':
    g1 = greenlet(sing)
    g2 = greenlet(dance)
    
    g1.switch() # 通过switch()方法在切换到指定的任务
    