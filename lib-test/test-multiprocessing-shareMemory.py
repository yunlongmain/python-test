# coding=utf-8

# modified from official documentation
import multiprocessing

def f(n, a):
    n   = 3.14
    a[0]      = 5

# num   = multiprocessing.Value('d', 0.0)
num = 1  # 未共享
arr   = multiprocessing.Array('i', range(10))

p = multiprocessing.Process(target=f, args=(num, arr))
p.start()
p.join()

print num
print arr[:]