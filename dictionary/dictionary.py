#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
    File name: dictionary.py
    Author: Siôn Abraham
    Date created: 2018/10/05
    Date last modified: 2018/10/05
    Python Version: 3.7.0
'''

# Built-in/Generic Imports
import os
import re
import sys
import urllib.request
import random

def main():

    '''This script will print out the definition of a german word in the
    command line, or get its definition and store it locally if not avaliable'''

    word = sys.argv[1]
    # url = 'https://www.linguee.com/english-german/search?source=auto&query={}'.format(word)
    url = 'http://pythonprogramming.net/parse-website-using-regular-expressions-urllib/'



    fp = urllib.request.urlopen(url)
    mybytes = fp.read()
    paragraph = re.findall(r'<p>(.*?)</p>', str(mybytes))

    for eachP in paragraph:
        print('\n')
        print(eachP)

    return


if __name__ == '__main__':
    try:
        main()
    except Exception as ex:
        print('Service exception: {}.'.format(ex))

# to run: python3 dictionary.py Zusammenhang
