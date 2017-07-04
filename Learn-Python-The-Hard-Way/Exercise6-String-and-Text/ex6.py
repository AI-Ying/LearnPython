# -*- coding: utf-8 -*-

# define a bit of string named x, and the string include a format character
x = "There are %d types of people" % 10
binary = "binary"
do_not = "don't"

# define a bit of string named y, and the string include a format character
y = "Those who know %s and those who %s." %(binary, do_not)


print x
print y
# %r can include any format character, and as usual, we use %r for debugging.
print "I said: %r." % x
print "I also said: '%s'." % y


# format character separated from string
# a format character can use parentheses ()
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
print joke_evaluation %(hilarious)


# a bit of string separated form string, as like java
w = "This is the left side of ..."
e = "a string with a right side..."
print w + e


