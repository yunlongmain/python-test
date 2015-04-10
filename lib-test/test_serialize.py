# coding=utf-8

'''
cPickle包的功能和用法与pickle包几乎完全相同 (其存在差别的地方实际上很少用到)，不同在于cPickle是基于c语言编写的，速度是pickle包的1000倍
如果想使用cPickle包，我们都可以将import语句改为:
'''
import cPickle as pickle

# define class
class Bird(object):
    have_feather = True
    way_of_reproduction  = 'egg'

summer       = Bird()                 # construct an object
picklestring = pickle.dumps(summer)   # serialize object

print(picklestring)

