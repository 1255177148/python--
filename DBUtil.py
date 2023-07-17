import pymysql


class DBUtil:
    config = {
        'host': '127.0.0.1', # 数据库ip
        'port': 3306, # 端口号
        'user': 'root', # 用户名
        'password': 'root', # 密码
        'db': 'book', # 库名
        'cursorclass': pymysql.cursors.DictCursor, # 游标类型，查询结果以集合的形式返回
        'charset':'utf8mb4'
    }
    def __init__(self) -> None:
        self.conn = pymysql.connect(**DBUtil.config)
        self.cursor = self.conn.cursor()
    
    def close(self):
        '''
        关闭链接
        '''
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
    
    def executeSql(self, sql, *args):
        '''执行sql语句,用于增删改'''
        try:
            # 执行sql
            self.cursor.execute(sql, args)
            # 提交事务
            self.conn.commit()
        except Exception as e:
            print('sql执行失败,原因{}', e)
            if self.conn:
                self.conn.rollback()
        finally:
            self.close()
    
    def queryOne(self, sql, *args):
        '''查询一条数据'''
        try:
            # 执行sql
            self.cursor.execute(sql, args)
            # 获取结果
            result = self.cursor.fetchone()
            # 返回数据
            return result
        except Exception as e:
            print('sql执行失败,原因{}', e)
        finally:
            self.close()
    
    def queryAll(self, sql, *args):
        '''查询所有符合条件的数据'''
        try:
            # 执行sql
            self.cursor.execute(sql, args)
            # 获取结果
            result = self.cursor.fetchall()
            # 返回数据
            return result
        except Exception as e:
            print('sql执行失败,原因{}', e)
        finally:
            self.close()

db = DBUtil()