#!/usr/bin/python3
# -*- coding:utf8 -*-
# Author      : Arthur Yan
# Date        : 2019-02-14 14:49:13
# Description : 打印三角形


for i in range(6):
    for j in range(i+1):
        print("*", end='')
    print()

for i in range(6):
    for j in range(6-i-1):
        print(' ', end='')
    for n in range(i):
        print('*', end="")
    print()


for i in range(6):
    for j in range(6-i-1):
        print(' ', end='')
    for n in range(2*i+1):
        print('*', end='')
    print()
print()

for i in range(6):
    for n in range(i):
        print(" ", end='')
    for j in range(2*(6-i)):
        print("*", end='')
    for m in range(i):
        print(" ", end='')
    print()
