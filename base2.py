# coding=utf-8

dic = {'a': 1, 'b': "abc"}
print(dic, type(dic))

dic = {'lilei': 90, 'lily': 100, 'sam': 57, 'tom': 90}
for key in dic:
    print(dic[key])

print dic.items()


f = open("test.txt", "r")
lineDatas = f.readlines()
print(lineDatas)
for line in lineDatas:
    print(line)

f.close()


# 当一个循环结构（比如for）调用循环对象时，它就会每次循环的时候调用next()方法，直到StopIteration出现，for循环接收到，就知道循环已经结束，停止调用next()。
# open()返回的实际上是一个循环对象，包含有next()方法。而该next()方法每次返回的就是新的一行的内容，到达文件结尾时举出StopIteration。这样，我们相当于手工进行了循环。
f = open("test.txt", "r")
for line in f:
    print line
f.close()

import this
