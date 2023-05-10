#!/usr/bin/python3
'''Module'''


class Base:
    '''Represents base of all classes to be created'''

    __nb_objects = 0

    def __init__(self, id=None):
        ''' '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
