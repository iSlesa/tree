#!/usr/bin/env python3

import os
import argparse
import termcolor

def listall(path,j=0):
    list_ = os.listdir(path)
    os.chdir(path)
    num = len(list_)
    for i in range(num):
        if not list_[i].startswith('.'):
            if os.path.isdir(list_[i]):
                if i == (num)-1:
                    print("│    "*j+"└──",end=" ")
                    termcolor.cprint(list_[i], 'green',attrs=['bold'] )
                else:
                    print("│    "*j+'├──',end=" ")
                    termcolor.cprint(list_[i], 'green',attrs=['bold'] )
                path_ = path+'/'+list_[i]
                os.chdir(path_)
                listall(path_,j+1)
            else:
                if i == (num)-1:
                    print("│    "*j+'└── '+list_[i])
                else:
                    print("│    "*j+'├── '+list_[i])
        os.chdir(path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", type=str, default=os.getcwd(), help="Path to directory")
    path = os.path.abspath(parser.parse_args().path)
    if not os.path.isdir(path):
        print(path+" is not a directory. Please enter a valid path.")
    else:
        termcolor.cprint(os.path.basename(os.path.normpath(path)), 'blue', attrs=['bold'])
        listall(path)
