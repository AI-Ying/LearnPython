# -*- coding: utf-8 -*-

import os

def main():
    input_func = raw_input

    CheckDir = input_func("Enter the name of the directory to check : ")

    if os.path.exists(CheckDir):
        print("The directory exists")
    else:
        print("No directory found for " + CheckDir)
        os.makedirs(CheckDir)
        print("Directory created for " + CheckDir)


# if the function name is exists and equal hello, then start this
if __name__ =='__main__':
    main()
