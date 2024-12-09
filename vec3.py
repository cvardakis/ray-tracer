import math
import numpy  # install NumPy, or comment out this line and lines 93-94

class Vec3:
    # Listing 4 methods
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    def __neg__(self):
        return Vec3(-self.x, -self.y, -self.z)
    def __iadd__(self, other):
        if isinstance(other, Vec3):
            self.x += other.x
            self.y += other.y
            self.z += other.z
        else:
            self.x += other
            self.y += other
            self.z += other
        return self
    def __isub__(self, other):
        if isinstance(other, Vec3):
            self.x -= other.x
            self.y -= other.y
            self.z -= other.z
        else:
            self.x -= other
            self.y -= other
            self.z -= other
        return self
    def __imul__(self, t):
        self.x *= t
        self.y *= t
        self.z *= t
        return self
    def __itruediv__(self, t):
        self.x /= t
        self.y /= t
        self.z /= t
        return self

    def length(self):
        return math.sqrt(self.length_squared())
    def length_squared(self):
        return self.x*self.x + self.y*self.y + self.z*self.z

    # Listing 5 methods
    def __str__(self):
        return "{0} {1} {2} ".format(self.x, self.y, self.z)

    def __add__(self,other):
        if isinstance(other, Vec3):
            return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)
        else: # for adding a scalar to the vector
            return Vec3(self.x + other, self.y + other, self.z + other)

    def __sub__(self,other):
        if isinstance(other, Vec3):
            return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)
        else:
            return Vec3(self.x - other, self.y - other, self.z - other)

    def __mul__(self, other):
        if isinstance(other, Vec3):
            return Vec3(self.x * other.x, self.y * other.y, self.z * other.z)
        else:
            return Vec3(self.x * other, self.y * other, self.z * other)
    def __rmul__(self, t):
        return Vec3(self.x * t, self.y * t, self.z * t)

    def __truediv__(self, t):
        return Vec3(self.x / t, self.y / t, self.z / t)

    # dot product
    def dot(self, v):
        return self.x * v.x + self.y * v.y + self.z * v.z

    # cross
    def cross(self, v):
        return Vec3(self.y*v.z - self.z*v.y,
                    self.z*v.x - self.x*v.z,
                    self.x*v.y - self.y*v.x)

    def unit_vector(self):
        return self/self.length()

    # checking for equality
    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y and self.z == other.z)

    # converting to a numpy array - may speed things up later
    def to_array(self):
        return numpy.array([self.x , self.y , self.z])

# create type aliases
Point3 = Vec3       # 3D point
Color = Vec3        # RGB color


def main():
    x=Vec3(5, 0, 0)
    y=Vec3(0, 1, 0)
    should_be_z = x.cross(y)
    negy=x.cross(should_be_z)
    print(negy.unit_vector())

if __name__ == '__main__':
    main()