#!/usr/bin/python3
'''Module'''


from models.base import Base


class Rectangle(Base):
    ''' '''

    def __init__(self, width, height, x=0, y=0, id=None):
        ''' '''
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    # Getter functions
    @property
    def width(self):
        '''Gets width value'''
        return self.__width

    @property
    def height(self):
        '''Gets height value'''
        return self.__height

    @property
    def x(self):
        '''Gets value for x'''
        return self.__x

    @property
    def y(self):
        '''Gets the value for y'''
        return self.__y

    # Setter functions list
    @width.setter
    def width(self, value):
        '''sets the value for width'''
        if (type(value) is not int):
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @height.setter
    def height(self, value):
        '''Sets height value'''
        if (type(value) is not int):
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__height = value

    @x.setter
    def x(self, value):
        '''Sets x value'''
        if (type(value) is not int):
            raise TypeError("x must be an integer")

        if value <= 0:
            raise ValueError("x must be > 0")

        self.__x = value

    @y.setter
    def y(self, value):
        '''Sets y value'''
        if (type(value) is not int):
            raise TypeError("y must be an integer")

        if value <= 0:
            raise ValueError("y must be > 0")

        self.__y = value
