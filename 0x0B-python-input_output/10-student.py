#!/usr/bin/python3
'''Module'''


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''Returns dictionary representation'''
#        for items in attrs:
        if isinstance (attrs, str):
            return self.__list__
        return self.__dict__
