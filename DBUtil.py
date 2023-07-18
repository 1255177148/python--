import pymysql
import decimal


class DBUtil:
    config = {
        'host': '127.0.0.1',  # 数据库ip
        'port': 3306,  # 端口号
        'user': 'root',  # 用户名
        'password': 'root',  # 密码
        'db': 'book',  # 库名
        'cursorclass': pymysql.cursors.DictCursor,  # 游标类型，查询结果以集合的形式返回
        'charset': 'utf8mb4'
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

    def executeSql(self, sql, args):
        '''执行sql语句,用于增删改'''
        try:
            # 执行sql
            targetSql = self.cursor.mogrify(sql, args)
            print("执行的sql--->", targetSql)
            self.cursor.execute(targetSql)
            # 提交事务
            self.conn.commit()
        except Exception as e:
            print('sql执行失败,原因--->', e)
            if self.conn:
                self.conn.rollback()
        finally:
            self.close()

    def executeBatchSql(self, sql, args):
        '''批量执行sql语句,用于增删改'''
        try:
            # 执行sql
            self.cursor.executemany(sql, args)
            # 提交事务
            self.conn.commit()
        except Exception as e:
            print('sql执行失败,原因--->', e)
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
            print('sql执行失败,原因--->', e)
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

if __name__ == '__main__':
    '''demo例子'''
    db = DBUtil()
    # # 批量新增
    # insertSql = "insert into author(id,code,name,value) values (%s, %s, %s, %s)"
    # params = list()
    # i = 1
    # while i <= 5:
    #     params.append([i, 'test' + str(i), '作者' + str(i), '26.05'])
    #     i += 1
    # db.executeBatchSql(insertSql, params)
    
    # 批量更新，使用case when的用法，先拼接sql字符串，后面参数用%s注入
    updateSql = "update author set value = case {} where id in %s" # 原始sql语句 
    splicing = list() # 要拼接的case when语句
    param2 = list() # where条件id in 后面的参数，in后面的小括号会自动拼上的
    updateParam = list() # case when 里的参数
    j = 1
    tempSql = "when id = %s then %s"
    while j <= 2:
        updateParam.append(j)
        updateParam.append('16.05')
        splicing.append(tempSql)
        param2.append(j)
        j+=1
    param = " ".join(map(str, splicing)) + " end"
    updateSql = updateSql.format(param)
    print("更新的sql--->" + updateSql)
    updateParam.append(param2)
    print("参数--->" + str(updateParam))
    db.executeSql(updateSql, updateParam)
    
