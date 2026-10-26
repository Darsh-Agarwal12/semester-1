# Worksheet 1.5: Rectangle Class
'''Rectangle class returns area, perimeter and checks whether it is a square.'''
class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width, height):
        """
        Creates a Rectangle, given values for width and height.
        """
        # Add code here to check type and value of provided width & height,
        # raising appropriate exceptions if necessary (see README.md)
        self.width = width
        self.height = height
        if not isinstance(width, (int, float)):
            raise TypeError("Width must be a number")
        if not isinstance(height, (int, float)):
            raise TypeError("Height must be a number")
        if width <= 0:
            raise ValueError("Width must be positive")
        if height <= 0:
            raise ValueError("Height must be positive")

    def is_square(self):
        '''
        Returns True if the Rectangle is a square, False otherwise.
        '''
        return self.width == self.height
    def area(self):
        '''Returns the area of the Rectangle.'''
        return self.width * self.height
    def perimeter(self):
        '''Returns the perimeter of the Rectangle.'''
        return 2 * (self.width + self.height)

    # Implement methods is_square(), area() & perimeter() here
    # (See README.md for details of what they should do)
