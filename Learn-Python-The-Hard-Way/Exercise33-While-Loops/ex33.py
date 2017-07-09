# -*- coding:utf-8 -*-

numbers = []

def while_loop(i, p):
    while i < p:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i
    return numbers


# call while_loop:
print "we can call the function of while_loop"
while_loop(3, 8)


print "The numbers now:"

for num in numbers:
    print num
