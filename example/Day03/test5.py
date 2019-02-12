#!/usr/bin/python3
# -*- coding:utf8 -*-
# Author : Arthur Yan
# Date   : 2019-02-12 14:52:29

salary = float(input("本月收入："))
insurance = float(input("五险一金："))
diff = salary - insurance -3500
if diff <=0:
    rate = 0
    deduction = 0
elif diff < 1500:
    rate = 0.03
    deduction = 0
elif diff < 9000:
    rate = 0.2
    deduction = 555
elif diff < 35000:
    rate = 0.25
    deduction = 1005
elif diff < 55000:
    rate = 0.3
    deduction = 2755
elif diff < 80000:
    rate = 0.35
    deduction = 5505
else:
    rate = 0.45
    deduction = 13505

tax = abs(diff * rate - deduction)
salary_true = diff + 3500 - tax
print('个人所得税：{}'.format(tax))
print('实际到手收入：{}'.format(salary_true))




