#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author : Arthur Yan
# Date   : 2019-02-06 16:17:11

value = float(input('Input length:'))
unit = input('Input unit:')
if unit == 'in' or unit == '英寸':
    print('%f英寸 = %f厘米' % (value, (value * 2.54)))
elif unit == 'cm' or unit == '厘米':
    print('%f厘米 = %f英寸' % (value, (value / 2.54)))
else:
    print('Input valid unit:')

