# coding=utf-8

import subprocess
rc = subprocess.call(["ls","-l"])
rc = subprocess.call("ls -l",shell=1)


import subprocess
child = subprocess.Popen(["ping","-c","5","www.baidu.com"])
child.wait()
print("parent process")

# import time
# time.sleep(5)

import subprocess
child = subprocess.Popen(["cat"], stdin=subprocess.PIPE)
child.communicate("vamei")