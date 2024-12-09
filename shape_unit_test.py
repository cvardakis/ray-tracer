import unittest
from vec3 import *
from ray import Ray
from shape import Sphere

class SphereTestCase(unittest.TestCase):
    # no intersection
    def test_sphere_no_hit(self):
        r = Ray(Point3(0, 2, -5), Vec3(0,0,1))
        s = Sphere(Point3(0,0,0), 1, Color(1,0,0))
        hit = s.hit(r)
        self.assertEqual(1, len(hit))
        self.assertEqual(False, hit[0])

    def test_sphere_tangent(self):
        r = Ray(Point3(0,0,-5), Vec3(0,0,1))
        s = Sphere(Point3(0,0,0), 1, Color(1,0,0))
        hit = s.hit(r)
        self.assertTrue(len(hit)>3)
        self.assertTrue(hit[0])
        # closer of two intersections is at t=4
        self.assertEqual(4.0, hit[1], 0.0001)
        self.assertEqual(Vec3(0., 0., -1.), hit[2])

    def test_sphere_inside(self):
        r = Ray(Point3(0,0,0), Vec3(0,0,1))
        s = Sphere(Point3(0,0,0), 1, Color(1,0,0))
        hit = s.hit(r)
        self.assertTrue(len(hit)>3)
        self.assertTrue(hit[0])
        # one intersection is negative
        # only positive intersection is at t=1.0
        self.assertEqual(1.0, hit[1], 0.0001)
        self.assertEqual(Vec3(0., 0., 1.), hit[2])

    def test_sphere_behind(self):
        r = Ray(Point3(0,0,5), Vec3(0,0,1))
        s = Sphere(Point3(0,0,0), 1, Color(1,0,0))
        hit = s.hit(r)
        self.assertEqual(1,len(hit))
        self.assertFalse(hit[0])

    def test_small_sphere(self):
        r = Ray(Point3(0, 0, -5), Vec3(0, 0, 1))
        s = Sphere(Point3(0, 0, 0), 2, Color(1, 0, 0))
        hit = s.hit(r)
        self.assertTrue(len(hit) > 3)
        self.assertTrue(hit[0])
        # clser intersection is t=3.0, other is 7.0
        self.assertEqual(3.0, hit[1], 0.0001)
        self.assertEqual(Vec3(0., 0., -1.), hit[2])

    def test_sphere_normal_z(self):
        r = Ray(Point3(0, 0, 5), Vec3(0, 0, -1))
        s = Sphere(Point3(0, 0, 0), 2, Color())
        hit = s.hit(r)
        self.assertTrue(hit[0])
        self.assertEqual(3.0, hit[1], 0.0001)
        self.assertEqual(Vec3(0., 0., 1.), hit[2])

    def test_sphere_normal_y(self):
        r = Ray(Point3(0, 5, 0), Vec3(0, -1, 0))
        s = Sphere(Point3(0, 1, 0), 2, Color())
        hit = s.hit(r)
        self.assertTrue(hit[0])
        self.assertEqual(2.0, hit[1], 0.0001)
        self.assertEqual(Vec3(0., 1., 0.), hit[2])

    def test_sphere_normal(self):
        r = Ray(Point3(1, 1, 1), Vec3(-1, -1, -1))
        s = Sphere(Point3(0, 0, 0), 0.5, Color())
        hit = s.hit(r)
        self.assertTrue(hit[0])
        self.assertEqual(1.2320508075688765, hit[1], 0.0001)
        self.assertEqual(Vec3(0.5773502691896264,0.5773502691896264,0.5773502691896264), hit[2])

if __name__ == '__main__':
    unittest.main()