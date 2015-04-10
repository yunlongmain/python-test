# coding=utf-8

from itertools import *

# 无穷循环器
'''
count(5, 2)     #从5开始的整数循环器，每次增加2，即5, 7, 9, 11, 13, 15 ...

cycle('abc')    #重复序列的元素，既a, b, c, a, b, c ...

repeat(1.2)     #重复1.2，构成无穷循环器，即1.2, 1.2, 1.2, ...

repeat也可以有一个次数限制:

repeat(10, 5)   #重复10，共重复5次
'''

# imap函数与map()函数功能相似，只不过返回的不是序列，而是一个循环器
rlt = map(pow, [1, 2, 3], [1, 2, 3])
print rlt

rlt = imap(pow, [1, 2, 3], [1, 2, 3])
print rlt
for num in rlt:
    print(num)

c = compress('ABCD', [1, 1, 0, 1])
print c
for num in c:
    print(num)

print "------ groupby ------"

def height_class(h):
    if h > 180:
        return "tall"
    elif h < 160:
        return "short"
    else:
        return "middle"

friends = [191, 158, 159, 165, 170, 177, 181, 182, 190]

friends = sorted(friends, key = height_class)
print(friends)
for m, n in groupby(friends, key = height_class):
    print(m)
    print(list(n))


print(groupby(friends, key = height_class))