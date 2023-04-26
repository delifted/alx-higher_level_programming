#!/usr/bin/python3
'''Module'''


class Base:
    '''Represents base of all classes to be created'''

    __nb_objects = 0

    def __init__(self, id=None):
        ''' '''
        if id is None:
            id = Base.__nb_objects + 1
            Base.__nb_objects += 1
        self.id = id
