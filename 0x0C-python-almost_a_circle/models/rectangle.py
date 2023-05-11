#!/usr/bin/python3
'''Module'''


from models.base import Base


class Rectangle(Base):
    ''' '''

    def __init__(self, width, height, x=0, y=0, id=None):
        ''' '''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    # Getter functions
    @property
    def width(self):
        '''Gets width value'''
        return self.__width

    @width.setter
    def width(self, value):
        ''' '''
        self.__width = value

    @property
    def height(self):
        '''Gets height value'''
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        '''Gets value for x'''
        return self.__x

    @x.setter
    def x(self, value):
        ''' '''
        self.__x = value

    @property
    def y(self):
        '''Gets the value for y'''
        return self.__y

    @y.setter
    def y(self, value):
        ''' '''
        self.__y = value
