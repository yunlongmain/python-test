# coding=utf-8

#通过__name__判断是直接运行还是被import
print(__name__)

filename = __file__[__file__.rfind('/')+1:]
print(filename)


import os.path
filename2 = os.path.basename(__file__)
print filename2