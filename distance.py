# Import statements
from sys import exit
from math import sqrt

# Class Definitions
class Point(object) :

    def __init__(self, num_dimensions) :
        self.num_dimensions = num_dimensions

    def get_num_dimensions(self) :
        return self.num_dimensions

    # Abstract method that returns list of the coordinates 
    def get_coordinates(self) :
        print("Not implemented. Subclass and override.")
        exit(1)

class Point2D(Point) :

    def __init__(self, x_coordinate, y_coordinate) :
        num_dimensions = 2
        super(Point2D, self).__init__(num_dimensions)
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def get_coordinates(self) :
        return [self.x_coordinate, self.y_coordinate]

class Point3D(Point) :

    def __init__(self, x_coordinate, y_coordinate, z_coordinate) :
        num_dimensions = 3
        super(Point3D, self).__init__(num_dimensions)
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.z_coordinate = z_coordinate

    # Return a list containing the three coordinates as x, y, z
    def get_coordinates(self) :
        return [self.x_coordinate, self.y_coordinate, self.z_coordinate]


def distance(p1, p2) :
    if p1.num_dimensions == p2.num_dimensions :
        distance_squared = 0
        for i in range(p1.num_dimensions) :
            distance_squared += ((p1.get_coordinates()[i] -
                 p2.get_coordinates()[i]) ** 2)
        return sqrt(distance_squared)
    else : 
        print ("Error: Dimensions must be the same to compute distance.")
#########TESTING##############TESTING############TESTING########TESTING#########

pt2d = Point2D(0,0)
pt2d2 = Point2D(1,1)
pt3d = Point3D(-1,4,-6)
pt3d2 = Point3D(8,10,20)

print pt2d.get_coordinates()
print pt3d.get_coordinates()

print pt2d.get_num_dimensions()
print pt3d.get_num_dimensions()

print distance(pt2d,pt2d2)
print distance(pt3d,pt3d2)
print distance(pt2d, pt3d)