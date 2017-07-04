# -*- coding: utf-8 -*-

from sys import argv

script, filename = argv

print "We're going to erase %r." %filename
print "If you don't want that, hit CTRL-C(^C)"
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
# open the text file with write
target = open(filename, 'w+')

# default with only read
# target = open(filename)

# open the text file with append
# target = open(filename, 'a')

# open the text file with only read
# target = open(filename, 'r')

# Empties the file.
print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")
target.write(line1+ "\n" + line2 + "\n" + line3 + "\n")

print "And finally, we close it."
target.close()

# Reads just one line of a text file
test1 = open(filename)
print test1.readline()
print "-"*10

# Reads just one line of a text file
print test1.readline()
print "-"*10

# Reads the text file, if the file doesn't close, continue read the rest of file. Compare the follow case.
print test1.read()
test1.close()

# When closed file, read the text file from start.
print "-"*10
test2 = open(filename)
print test2.read()
test2.close()
