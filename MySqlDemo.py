from DBUtil import db
import decimal

sql = 'select * from author'
rs = db.queryAll(sql)
print(rs)
for map in rs:
    for key, value in map.items():
        print(key, value)