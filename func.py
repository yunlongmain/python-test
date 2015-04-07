# -*- coding: utf-8 -*-

re = map((lambda x,y: x+y),[1,2,3],[6,7,9])
print(re)


def func(a):
    if a > 100:
        return True
    else:
        return False

print filter(func,[10,56,101,500])


def line_conf():
    b = 15
    def line(x):
        return 2*x+b
    return line       # return a function object

b = 5
my_line = line_conf()
print(my_line(5))


print(my_line.__closure__)
print(dir(my_line.__closure__[0]))
print(my_line.__closure__[0].cell_contents)