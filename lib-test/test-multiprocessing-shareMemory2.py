# coding=utf-8

# Similarity and difference of multi thread vs. multi process
# Written by Vamei

import os
import threading
import multiprocessing

# worker function
import time

# 线程用可以直接共享内存，而进程不能，需要间接共享（信号量、管道等），例如用封装的类  multiprocessing.[数据类型]
iii = [5,]


def worker(sign, lock,testInt):
    lock.acquire()
    print(sign, os.getpid(), testInt)
    testInt[0]+=1
    lock.release()

# Main
print('Main:',os.getpid())

# Multi-thread
record = []
lock  = threading.Lock()
for i in range(5):
    thread = threading.Thread(target=worker,args=('thread',lock,iii))
    thread.start()
    record.append(thread)

#  阻塞直到record中的线程全部运行结束
for thread in record:
    thread.join()

# Multi-process
record = []
lock = multiprocessing.Lock()
for i in range(5):
    process = multiprocessing.Process(target=worker,args=('process',lock,iii))
    process.start()
    record.append(process)

for process in record:
    process.join()
