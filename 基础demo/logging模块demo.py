import os
import logging
from logging.handlers import TimedRotatingFileHandler

base_path = 'E://自学项目/pythonDemo/基础demo'  # 项目根路径
log_level = logging.DEBUG
log_path = os.path.join(base_path, 'log')
log_format = '%(asctime)s - %(name)s - %(filename)s[line:%(lineno)d] - %(levelname)s - %(message)s'
log_file = os.path.join(log_path, 'log.txt')


def log_init():
    '''
    日志初始化方法,在main方法里要先调用下
    '''
    if not os.path.isdir(log_path):
        os.mkdir(log_path)
    if not os.path.isfile(log_file):
        with open(log_file, 'w', encoding='utf-8') as file:
            pass
    logger = logging.getLogger('main')
    logger.setLevel(level=log_level)
    format = logging.Formatter(log_format)

    '''
    TimedRotatingFileHandler各参数含义:
    filename: 指定的日志文件
    when: 切割条件,按周(W)、天(D)、时(H)、分(M)、秒(S)切割
    interval: 间隔,就是几个when切割一次。when是W,interval是3的话就代表3周切割一次
    backupCount: 日志备份数量,就是保留几个日志文件,起过这个数量,就把最早的删除掉,从而滚动删除
    '''
    handler = TimedRotatingFileHandler(
        filename=log_file, when='D', interval=1, backupCount=7, encoding='utf-8')
    handler.setLevel(log_level)
    handler.setFormatter(format)
    logger.addHandler(handler)

    console = logging.StreamHandler() #控制台日志打印处理类
    console.setLevel(log_level)
    console.setFormatter(format)
    logger.addHandler(console)


if __name__ == '__main__':
    log_init()
    logger = logging.getLogger('main.log')
    logger.info('log 测试------')
