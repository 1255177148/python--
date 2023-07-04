def sum(num: int):
    return 1 if num == 1 else num + sum(num - 1)

print(sum(10))

def add(a, b, c):
    return c(a) + c(b)

d = add(-3, 5, abs)
print(d)