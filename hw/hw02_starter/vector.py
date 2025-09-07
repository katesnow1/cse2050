from math import sqrt, cos, sin, atan

class Vector:
    """Class for methods that have been factored out from Rectangluar and Polar Vectors"""
    def __init__(self, *args):
        """Users should specify rectangular or polar instead"""
        raise NotImplementedError("Specify RectangularVector or PolarVector.")
    
    # Define "getters" for x, y, mag, and angle
    def get_x(self):
        """Returns x-component of vector."""
        return self._x
    
    def get_y(self):
        """Returns y-component of vector."""
        return self._y
    
    def get_mag(self):
        """Returns magnitude of vector."""
        return self._mag

    def get_ang(self):
        """Returns angle of vector."""
        return self._ang
    
    def __eq__(self, other):
        """Returns True is both vectors in params are equal to each other"""
        return round(self._x, 3) == round(other._x, 3) and round(self._y, 3) == round(other._y, 3)
            
    def __add__(self, other):
        """Returns a RectangularVector equal to the sum of the vectors passed through in params"""
        return RectangularVector(self._x + other._x, self._y + other._y)
    
    def rectangular(self):
        """Returns a RectangularVector object equal to object in params"""
        return RectangularVector(self._mag * cos(self._ang), self._mag * sin(self._ang))
    
    def polar(self):
        """Returns a PolarVector object equal to object in params"""
        return PolarVector(sqrt(self._x**2 + self._y**2), atan(self._y / self._x))

    def dot(self, other):
        """Returns dot product of vectors self and other"""
        return self._x * other._x + self._y * other._y
    
    def __mul__(self, *args):
        """Users should use a dot product instead"""
        raise NotImplementedError("Please use dot() if you would like to find a dot product, as cross products are not yet supported.")



class RectangularVector(Vector):
    """Rectangular vectors have an x and y component."""
    def __init__(self, x, y):
        """Creates a new vector with given x- and y- attributes."""
        self._x = x
        self._y = y
        self._mag = sqrt(x**2 + y**2)
        self._ang = atan(y/x)

    def _update(self):
        """Updates the magnitude and angle of the vector whenever x or y is changed"""
        self._mag = sqrt(self._x**2 + self._y**2)
        self._ang = atan(self._y/self._x)
    
    def set_x(self, new_x):
        """sets new x value and updates magnitude and angle values"""
        self._x = new_x
        self._update()
    
    def set_y(self, new_y):
        """sets new y value and updates magnitude and angle values"""
        self._y = new_y
        self._update()

    def __repr__(self):
        """returns a string representation of the RectangularVector object"""
        return f"RectangularVector({self._x}, {self._y})"


class PolarVector(Vector):
    """Polar Vectors have a magnitude and angle component"""
    def __init__(self, mag, ang):
        """Creates a new vector with given magnitude and angle values"""
        self._mag = mag
        self._ang = ang
        self._x = mag * cos(ang)
        self._y = mag * sin(ang)

    def _update(self):
        """Updates x and y whenever the magnitude and angle are changed"""
        self._x = self._mag * cos(self._ang)
        self._y = self._mag * sin(self._ang)


    def set_mag(self, new_mag):
        """Sets the magnitude to the param new_mag"""
        self._mag = new_mag
        self._update()

    def set_ang(self, new_ang):
        """Sets the angle to the param new_ang"""
        self._ang = new_ang
        self._update()
    
    def __repr__(self):
        """Returns a string representation of the Polar Vector object"""
        return f"PolarVector({self._mag}, {self._ang})"