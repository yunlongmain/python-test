# -*- coding: utf-8 -*-

c = 1

print(id(c))
print(hex(id(c)))


class from_obj(object):
    def __init__(self, to_obj):
        self.to_obj = to_obj

b = [1,2,3]
a = from_obj(b)
print(id(a.to_obj))
print(id(b))

print globals()


import gc
print(gc.get_threshold())

x = [1, 2, 3]
y = [x, dict(key1=x)]
z = [y, (x, y)]

import os

# def program_in_path(program):
#     path = os.environ.get("PATH", os.defpath).split(os.pathsep)
#     print(path)
#     path = [os.path.join(dir, program) for dir in path]
#     print(path)
#     path = [True for file in path if os.path.isfile(file)]
#     return bool(path)
#
# print(program_in_path('dot'))

# import objgraph
# objgraph.show_refs([z], filename='ref_topo.png')

from sys import getrefcount

a = []
b = [a]
a.append(b)

'''
为了回收这样的引用环，Python复制每个对象的引用计数，可以记为gc_ref。假设，每个对象i，该计数为gc_ref_i。Python会遍历所有的对象i。对于每个对象i引用的对象j，将相应的gc_ref_j减1。
在结束遍历后，gc_ref不为0的对象，和这些对象引用的对象，以及继续更下游引用的对象，需要被保留。而其它的对象则被垃圾回收。
'''
print getrefcount(a)
print getrefcount(b)