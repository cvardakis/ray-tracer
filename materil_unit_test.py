import unittest
from vec3 import *
from material import *
from light import *

class MyTestCase(unittest.TestCase):
    def test_direct(self):
        light = DirectionalLight(Vec3(0, 0, 1), Color(1,1,1))
        n = Vec3(0, 0, -1)
        # point = Point3(0, 0, 0)
        surface = Material(Color(1,1,1), 0.1, 0.9)
        color = surface.shade(light, n)
        #self.assertEqual(Color(1., 1., 1.), color)
        self.assertEqual(1., color.x)

    def test_45_angle(self):
        light = DirectionalLight(Vec3(0, -1, 1), Color(1,1,1))
        n = Vec3(0, 0, -1)
        # point = Point3(0, 0, 0)
        surface = Material(Color(1,1,1), 0.1, 0.9)
        color = surface.shade(light, n)
        self.assertEqual(Color(0.7363961030678927, 0.7363961030678927, 0.7363961030678927), color)

    def test_behind(self):
        light = DirectionalLight(Vec3(0, 0, -1), Color(1,1,1))
        n = Vec3(0, 0, -1)
        # point = Point3(0, 0, 0)
        surface = Material(Color(1,1,1), 0.1, 0.9)
        color = surface.shade(light, n)
        self.assertEqual(Color(0.1, 0.1, 0.1), color)

if __name__ == '__main__':
    unittest.main()