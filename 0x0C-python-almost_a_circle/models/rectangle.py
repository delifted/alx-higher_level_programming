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

class Rectangle(Base):
    ''' '''

#    Base.__width = width
#    Base.__height = height
#    Base.__x = x
#    Base.__y = y

    def __init__(self, width, height, x=0, y=0, id=None):
        ''' '''
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        Base.id = id
