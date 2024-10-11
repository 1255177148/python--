import execjs # 调用并执行js代码

print(execjs.get().name) # 获取当前js运行环境
# ctx = execjs.compile(
#     '''
#     function add(x, y){
#         return x + y
#     }
#     '''
# )
# print(ctx.call('add', 1, 2))
with open('123.js', 'r', encoding='utf-8') as f:
    js_code = f.read()
    ctx = execjs.compile(js_code).call('add', 1, 2)
    print(ctx)


# 另一种执行js的方法,这个现在基本不使用了
# import PyV8

# with PyV8.JSContext() as ctx:
#     ctx.eval(js_code)
#     ctx.locals.add(1, 2)

# 第三种执行js的方法
import js2py

add = js2py.eval_js(js_code)
print(add(1, 2))