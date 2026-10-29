# Week 1.5, Session 2: Task 1

# Add type hints to the Point class

import math


class Point:
    """
    A point in 2D space.
    """

    def __init__(self, x:float, y:float):
        """
        Creates a Point, given x & y coordinates.
        """
        self.x = x
        self.y = y
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Coordinates must be numeric values.")

    def distance(self) -> float:
        """
        Returns distance of this Point from the origin.
        """
        return math.hypot(self.x, self.y)

    def distance_to(self, p: 'Point') -> float:
        """
        Returns distance of this Point from the specified Point.
        """
        return math.hypot(self.x - p.x, self.y - p.y)


# Test program

p = Point(2, 1)
print(p.distance())
