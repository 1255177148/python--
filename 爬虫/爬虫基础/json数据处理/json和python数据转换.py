import json

# 将json格式转换成python数据格式
# 方法一，使用json.loads()
with open("data.json", "r", encoding="utf-8") as f:
    f_data = f.read()
    print(f_data)
    # 将json格式转换成python中的数据格式
    py_data = json.loads(f_data)
    print(py_data)

# 方法二，使用json.load
py_data2 = json.load(open('data.json', 'r', encoding='utf-8'))
print(py_data2)


# 下面是将python数据格式转换为json格式
# 方法一，使用json.dumps()方法
data2 = {
    "name": "张三",
    "age": 18,
    "skill": ["python", "java", "vue"],
    "isDelete": False,
    "isActive": True,
    "addr": None,
}
j_data = json.dumps(data2, ensure_ascii=False) # 这里将ensure_ascii设置为False，也就是不用ascii码转换
print(j_data)

# 方法二，使用json.dump()方法，读取python数据为json格式后，写入到json文件里
json.dump(data2, open('data2.json', 'w', encoding='utf-8'), ensure_ascii=False)