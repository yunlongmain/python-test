# coding=utf-8

import re

m = re.search("[0-9]+",'abcd45634ef12')
print(m.group(0))

m = re.search("output_(\d{4})", "output_1986txt")
print(m.group(0))
print(m.group(1))

m = re.search("\d{4}", "output_1986txt")
print(m.group(0))
# print(m.group(1))
