# -*- coding: utf-8 -*-

print "----deco func-----"
def decorator(F):
    def new_F(a, b):
        print("input", a, b)
        return F(a,b)
    return new_F

# get square sum
@decorator
def square_sum(a, b):
    return a**2 + b**2

# 函数square_sum在用@decorator声明后，已经被装饰，所以不需要再手动调用decorator(square_sum)
# decorator = decorator(square_sum)
# result = decorator(3, 4)

result = square_sum(3, 4)
print(result)
print "------------"

print "----print deco cls----"
def decorator(aClass):
    class newClass:
        def __init__(self, age):
            self.total_display   = 0
            self.wrapped         = aClass(age)
        def display(self):
            self.total_display += 1
            print("total display", self.total_display)
            self.wrapped.display()
    return newClass

@decorator
class Bird:
    def __init__(self, age):
        self.age = age
    def display(self):
        print("My age is",self.age)

eagleLord = Bird(5)
for i in range(3):
    eagleLord.display()

print "-----------"