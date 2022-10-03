#!/usr/bin/python3
""" This module implements a class called Rectangle that
inherits from the Base class """


from models.base import Base


class Rectangle(Base):
    """A class that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Gets the width"""
        return self.__width

    @width.setter
    def width(self, w):
        """Sets the width"""
        if isinstance(w, int):
            if w <= 0:
                raise ValueError("width must be > 0")
            else:
                self.__width = w
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """Gets the height"""
        return self.__height

    @height.setter
    def height(self, h):
        """Sets the height"""
        if type(h) == int:
            if h <= 0:
                raise ValueError("height must be > 0")
            else:
                self.__height = h
        else:
            raise TypeError("height must be an integer")

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @x.setter
    def x(self, x):
        """Setter for x"""
        if type(x) == int:
            if x < 0:
                raise ValueError("x must be >= 0")
            else:
                self.__x = x
        else:
            raise TypeError("x must be an integer")

    @property
    def y(self):
        """Getter for y"""
        return self.__y

    @y.setter
    def y(self, y):
        """Setter for y"""
        if type(y) == int:
            if y < 0:
                raise ValueError("y must be >= 0")
            else:
                self.__y = y
        else:
            raise TypeError("y must be an integer")

    def area(self):
        """Returns the area value of the Rectangle"""
        return self.__width * self.__height

    def display(self):
        """Prints in stdout the Rectangle instance with the character #"""
        [print() for y in range(self.__y)]
        for i in range(self.__height):
            [print(' ', end='') for x in range(self.__x)]
            [print('#', end='') for j in range(self.__width)]
            print()

    def __str__(self):
        """Returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        """return f'[{__class__.__name__}] ({self.id}) {self.__x}/{self.__y} -
        {self.__width}/{self.__height}'"""
        return '{} ({}) {}/{} - {}/{}'.format(__class__.__name__, self.id,
        self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        if kwargs:
            for key, value in kwargs.items():
                self.__setattr__(key, value)
        else:
            try:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
            except IndexError:
                pass

    def to_dictionary(self):
        """ Returns the dictionary representation of a Rectangle """
        """return self.__dict__"""
        return {'x': getattr(self, "x"),
                'y': getattr(self, "y"),
                'id': getattr(self, "id"),
                'height': getattr(self, "height"),
                'width': getattr(self, "width")}
