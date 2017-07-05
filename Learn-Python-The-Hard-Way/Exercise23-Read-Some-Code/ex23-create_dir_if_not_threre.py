# -*- coding: utf-8 -*-

import os

MESSAGE = 'The directory already exists.'
TESTDIR = 'testdir'

# try
# ....
# except ...
# ...
# else
# ...
#


try:

    # os.path.abspath(path)
    # Return a normalized absolutized version of the pathname path
    home = os.path.abspath("")
    print home

    # os.path.join(path, *paths)
    # Return the value about path/*paths eg: /home/TESTDIR
    # test:
    # print os.path.join(home, TESTDIR)
    if not os.path.exists(os.path.join(home, TESTDIR)):
        # create dir
        os.makedirs(TESTDIR)
    else:
        print(MESSAGE)
except Exception as e:
    print(e)

else:
    print "Good"
