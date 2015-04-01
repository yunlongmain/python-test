# -*- coding: utf-8 -*-

print("\n生成器")
# 生成器
def gen():
    i = 10
    yield i
    i += 1
    yield i

for j in gen():
    print(j)

def gen():
    for i in range(4):
        yield i

for j in gen():
    print(j)

# 生成器 表达式
gen = (x for x in range(4))

for j in gen:
    print(j)


# 表推导
print("\n表推导")

L = []
for x in range(10):
    L.append(x**2)
print(L)

# 快捷写法
L = [x**2 for x in range(10)]
print(L)