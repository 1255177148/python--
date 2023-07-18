from DBUtil import db
import decimal

sql = "insert into author(id,code,name,value) values (%s, %s, %s, %s)"
params = list()
i = 1
while i <= 5:
    params.append([i, 'test' + str(i), '作者' + str(i), '26.05'])
    i+=1
db.executeBatchSql(sql, params)