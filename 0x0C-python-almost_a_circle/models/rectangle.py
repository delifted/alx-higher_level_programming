#!/usr/bin/python3
'''Module'''


from models.base import Base


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
        super().__init__(id)
