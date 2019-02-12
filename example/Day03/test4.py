#!/usr/bin/python3
# -*- coding:utf8 -*-
# Author : Arthur Yan
# Date   : 2019-02-11 16:15:55

import math

edge1 = float(input("输入边长一： "))
edge2 = float(input("输入边长二： "))
edge3 = float(input("输入边长三： "))

if edge1+edge2 > edge3 and edge1+edge3 > edge2 and edge2+edge3 > edge1 :

    circle = edge1 + edge2 + edge3 p = circle / 2
    area = math.sqrt(p * (p-edge1) * (p-edge2) * (p-edge3))
    print("周长为：{0}， 面积为：{1}".format(circle, area))
