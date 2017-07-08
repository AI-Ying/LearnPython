# -*- coding: utf-8 -*-

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print "This is count %d" % number

# same as above
for fruit in fruits:
    print "A fruit of type: %s" % fruit

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
    print "I got %r" % i

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print "Adding %d to the list." % i
    # append is a function that lists understand
    elements.append(i)

# now we can print them out too
for i in elements:
    print "Element was: %d" % i
# we can calculate the max and min value of elements

print "The max value of elements = %d, The min value of elements = %d" % (max(elements), min(elements))

# now we can delete the element
del elements[2]
print "Delete 2, and elements was: ", elements

# we can add The_count and fruits lists
print "The_count_fruits lists has %d elements: ", len(the_count + fruits)
print the_count + fruits

# make a two-dimensional(2D)list

two_dimlist = [[1, 2, 3], [4, 5, 6]]
print two_dimlist


# for p in two_dimlist:
#    for q in two_dimlist:
#        print "%r-%r" %(p, q)
