# -*- coding: utf-8 -*-


re = iter(range(5))

try:
    for i in range(10):
        print re.next()
except StopIteration:
    print 'here is end ', i

print 'HaHaHaHa'