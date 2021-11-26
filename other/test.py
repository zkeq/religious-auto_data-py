# coding:utf-8
from goto_py import goto

new_str = '123'
if '1' in new_str:
    print(new_str)
    new_str = new_str.replace('1', '')

print(new_str)

