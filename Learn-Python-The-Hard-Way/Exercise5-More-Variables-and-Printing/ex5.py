# -*- coding: utf-8 -*-

my_name = 'AI'
my_age = 22
my_height = 175.5 # centimeter
my_weight = 65.5 # kg
my_eyes = 'Black'
my_teeth = 'White'
my_hair = 'Black'

print "Let's talk about %s." %my_name
print "He's %s centimeter tall." %my_height
print "He's %s kg heavy." %my_weight
print "Actualy that's not too heavy."
print "He's got %s eyes and %s hair." %(my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %s I get %s." %(my_age, my_height, my_weight,
        my_age + my_height + my_weight)

# use %r: it's like saying "print this no matter what"
print "If I add %r, %r and %r I get %r." %(my_age, my_height, my_weight,
        my_age + my_height + my_weight)

# round() is around the value
print "round(1.777888) = ", round(1.777888)
print "round(1.222333) = ", round(1.222333)

# The other format characters
# http://www.python-course.eu/python3_formatted_output.php


