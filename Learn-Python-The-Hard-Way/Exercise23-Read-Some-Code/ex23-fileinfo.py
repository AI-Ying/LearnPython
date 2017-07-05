# -*- coding: utf-8 -*-

import os
import time
import stat
import sys

# loop input until try_count == 0 or file name is exists
try_count = 10

while try_count:
    file_name = raw_input("Enter a file name: ")
    try_count -= 1
    try:
        # os.stat(file_name)
        # Return posix.stat_result(st_mode=16877, st_ino=15861849, st_dev=2052,
        # st_nlink=2, st_uid=1000, st_gid=1000, st_size=4096, st_atime
        # =1499257346, st_mtime=1499246581, st_ctime=1499257343)
        file_stats = os.stat(file_name)
        # if the file name is exists, and break loop
        break
    except OSError:
        print ("\nNameError : [%s] No such file or directory\n", file_name)
        break

if try_count == 0:
    print ("Trial limit exceded \n Exitting program")
    sys.exit()


# create a dictionary to hold file info
# key <-> value
file_info = {
        'fname' : file_name,
        'fsize' : file_stats[stat.ST_SIZE],
        'f_mt'  : time.strftime("%d-%m-%Y %I:%M:%S %p",
            time.localtime(file_stats[stat.ST_MTIME])),
        'f_at'  : time.strftime("%d-%m-%Y %I:%M:%S %p",
            time.localtime(file_stats[stat.ST_ATIME])),
        'f_ct'  : time.strftime("%d-%m-%Y %I:%M:%S %p",
            time.localtime(file_stats[stat.ST_CTIME]))
}
print "\nfile name = ", file_info['fname']
print "file size = ", file_info['fsize'], "bytes"
print "last modified = ", file_info['f_mt']
print "last accessed = ", file_info['f_at']
print "creation time = ", file_info['f_ct']

if stat.S_ISDIR(file_stats[stat.ST_MODE]):
    print("This a directory")
else:
    print("This is not a directory\n")


# time.strftime format time
# time.localtime  translate time stamp to normal time
print file_stats
print(time.strftime("%d-%m-%Y %I:%M:%S %p", time.localtime(file_stats[stat.ST_MTIME])))
print time.strftime("%d-%m-%Y %I:%M:%S %p")
print(file_stats[stat.ST_SIZE])
print (file_info)
