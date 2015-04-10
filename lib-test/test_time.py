# coding=utf-8

import time

print(dir(time))

print(time.time())   # wall clock time, unit: second
print(time.clock())  # processor clock time, unit: second


st = time.gmtime()      # 返回struct_time格式的UTC时间
print(st)
st = time.localtime()   # 返回struct_time格式的当地时间, 当地时区根据系统环境决定。
print(st)
st = time.mktime(st)    # 将struct_time格式转换成wall clock time
print(st)

import datetime
t = datetime.datetime(2012,9,3,21,30)
print(t)
print(dir(t))