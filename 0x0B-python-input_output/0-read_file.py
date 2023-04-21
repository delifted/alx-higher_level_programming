#!/usr/bin/python3
'''A module to input file'''


def read_file(filename=""):
    '''Read file module'''
    with open("my_file_0.txt", 'r', encoding='utf-8') as f:
        print(f.read())
