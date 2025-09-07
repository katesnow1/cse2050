from math import sqrt
class Point:
    count = 0 # Class variable
    def __init__(self, x, y):
        self._x = x
        self._y = y
        self.mag = self.dist_from_origin()
        Point.count += 1
    
    def __eq__(self, other):
        return (self._x == other.x and self._y == other.y)
    
    def dist_from_origin(self):
        return sqrt(self._x**2 + self._y**2)
    
    def __str__(self):
        """Return a string designed to be read by users"""
        return f"Point({self._x}, {self._y})"
    
    def __repr__(self):
        """Retrun a string that has all information necessary to recreate this object"""
        return f"Point({self._x}, {self._y})"
    
if __name__ == '__main__':

    p1 = Point(3,4)
    p2 = Point(3,4)
    p3 = Point(5,6)

    assert p1.x == 3
    assert p1.y == 4
    assert p1 == p2
    assert not p1 == p3
    assert p1.dist_from_origin() == 5
    print("all tests passed")
