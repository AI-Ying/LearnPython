#!/usr/bin/python3
# -*- coding:utf8 -*-
# Author : Arthur Yan
# Date   : 2019-02-11 14:15:32

score = float(input("输入分数: "))
mark = ''

if score >= 90 :
    mark = 'A'
elif score >=80 and score < 90 :
    mark = 'B'
elif score >=70 and score < 80 :
    mark = 'C'
elif score >=60 and score < 70 :
    mark = 'D'
else :
    mark = 'F'

print("mark: ", mark)

