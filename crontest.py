#!/usr/bin/env python
#coding=utf-8
#
#crontest.py

from datetime import datetime

file = open('datefile','a')

def main():
    file.write(str(datetime.now())+'\n')
    file.close()
    
    
if __name__== "__main__":
    main()
    
