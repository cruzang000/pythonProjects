import math


class Rectangle:
    """
    Rectangle class, defines methods for shape with 2 sets of equal length opposite parallel sides
    """
    def __init__(self, width, height):
        """
        init method sets height and width
        :param width: width of shape
        :type width: int
        :param height: height of shape
        :type height: int
        """
        self.width = width
        self.height = height

    def set_height(self, height):
        """
        sets shape height
        :param height: new shape height
        :type height: int
        """
        self.height = height

    def set_width(self, width):
        """
        sets shape width
        :param width: new shape width
        :type width: int
        """
        self.width = width

    def get_area(self):
        """
        multiples width and height to return area
        :return: area of share
        :rtype: int
        """
        return self.width * self.height

    def get_perimeter(self):
        """
        takes width and height to return perimeter
        :return: perimeter of shape
        :rtype: int
        """
        return (2 * self.width) + (2 * self.height)

    def get_diagonal(self):
        """
        takes width and height to return diagonal
        :return: diagonal of shape
        :rtype: int
        """
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        """
        returns string picture of shape with stars "*"
        :return: string picture of shape
        :rtype: string
        """
        if self.width > 50 or 50 < self.height:
            return "Too big for picture."

        return '\n'.join([("*" * self.width) for row in range(self.height)]) + "\n"

    def get_amount_inside(self, shape):
        """
        takes shape and calculates how many of passed in shape will fit in current shape
        :param shape: shape to test how many times fits inside current shape
        :type shape: rectangle/square object
        :return: amount of shapes that fit inside current shape
        :rtype: int
        """
        return math.floor(float(self.width / shape.width) * (self.height / shape.height))

    def __str__(self):
        """
        returns string representation of object
        :return: class name, width and height
        :rtype: string
        """
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    """
    Square class subclass Rectangle
    """
    def __init__(self, length):
        """
        calls Rectangle init method to set width and height
        :param length: length of side of square
        :type length: int
        """
        Rectangle.__init__(self, length, length)

    def set_side(self, side):
        """
        sets width and height of square to side
        :param side: length of side to set height and width to
        :type side: int
        """
        self.height = side
        self.width = side

    def set_width(self, width):
        """
        calls set side method to set all sides to new length
        :param width: new length for square
        :type width: int
        """
        self.set_side(width)

    def set_height(self, height):
        """
       calls set side method to set all sides to new length
       :param height: new length for square
       :type height: int
       """

        self.set_side(height)

    def __str__(self):
        """
        returns str of class name and side length
        :return: string representation of object
        :rtype: string
        """
        return f"Square(side={self.height})"