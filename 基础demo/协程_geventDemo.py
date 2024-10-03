# 协程--gevent来实现
# 使用gevent来自动切换任务
# gevent里有一个monkey.patch_all()方法，是一个补丁，会将原有代码里所有的IO操作替换成gevent自己的方法，
# 使得原有的阻塞IO变成了非阻塞IO
import gevent

# 下面时最简单的示范
# def sing():
#     print('在唱歌')
#     gevent.sleep(1) # 模拟IO阻塞
#     print('唱完歌了')

# def dance():
#     print('在跳舞')
#     gevent.sleep(1)
#     print('跳完舞了')

# if __name__ == '__main__':
#     # 创建协程
#     g1 = gevent.spawn(sing)
#     g2 = gevent.spawn(dance)
#     # 等待协程执行完毕
#     # g1.join()
#     # g2.join()
#     # 上面时单个join，等待单个任务执行完毕，还可以使用joinall()，一次等待所有的任务执行完毕
#     gevent.joinall([g1, g2])

# 上面是最简单的模拟IO延时的小demo，下面写一个更实际点的应用场景示例，上面先都注释掉
from gevent import monkey
monkey.patch_all() # 这里使用了monkey