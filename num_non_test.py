# coding:utf-8

import re

num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
str = '12点钟我们'
print(bool(re.search(r'\d', str)))
