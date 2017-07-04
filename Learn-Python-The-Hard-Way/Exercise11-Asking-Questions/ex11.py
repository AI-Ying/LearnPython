# -*- coding: utf-8 -*-

print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weight",
weight = raw_input()
print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)


# translate string to int or float
print "Input the first number:",
number1 = int(raw_input())
print "Input the second numer:",
number2 = float(raw_input())
print "The value = number1 / number2 = %r" %(number1/number2)


# compare input() and raw_input(), avoid using the input().
print "How old are you?",
age = input()
print "What the color of your eyes?",
color = raw_input()
#color = input()
print "So, you're %r old,  %r eyes." % (age, color)
