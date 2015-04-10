# coding=utf-8

import signal
import time
import os

# 通过pid，os.kill(pid,sid) 给自己发送信号
print os.getpid()

# Define signal handler function
def myHandler(signum, frame):
    print("Now, it's the time")
    exit()

# register signal.SIGALRM's handler
signal.signal(signal.SIGALRM, myHandler)
signal.alarm(5)
i = 5
while True:
    print('not yet, need ' + str(i))
    i -= 1
    time.sleep(1)


