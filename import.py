# -*- coding: utf-8 -*-

import os
#import 模块，会从下面路径查找
print(os.sys.path)

# import testModule
# print testModule.tt("b")
from testModule import tt  # from testModule import *
print tt("b")
