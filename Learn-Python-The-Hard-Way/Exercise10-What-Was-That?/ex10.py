# -*- coding: utf-8 -*-

tabby_cat = "\t I'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat"

fat_cat = """

I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

# fat_cat_single-quote = '''

# I 'll do a list;
# \t* Cat food
# \t* Fishies
# \t* Catnip\n\* Grass
# '''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
# print Fat_cat_single_quote

while True:
    for i in ["/", "-", "|", "\\", "|"]:
        print "%s\r" % i,


