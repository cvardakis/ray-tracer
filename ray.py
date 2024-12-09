from light import *
import material
from vec3 import *
import shape


class Ray:

    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction.unit_vector()

    def origin(self):
        return self.origin

    def direction(self):
        return self.direction

    def at(self, t):
        return self.origin + (t *self.direction)

    @property
    def ray_color(self):

        #lights = [DirectionalLight(Vec3(1,0,0), Color(1,1,1))] #sphere lighting
        lights = [DirectionalLight(Vec3(1, 0, 1), Color(1, 1, 1)), DirectionalLight(Vec3(-1, 0, 1), Color(1, 1, 1))] #diamond lighting
        # lights = [DirectionalLight(Vec3(0, -1, -0.3), Color(1,1,1)), DirectionalLight(Vec3(-1, 0, -1), Color(1,1,1))]  #gourd lighting
        # lights = [DirectionalLight(Vec3(0, 0, -1), Color(1,1,1))]
        # lights = [DirectionalLight(Vec3(1, 1, 1), Color(1, 1, 1))]
        objects = []
        #objects = [shape.Sphere(Point3(0.25,0.0,-0.5), 0.25, material.Material(Color(255, 255, 0), 0.5, 0.6)), shape.Sphere(Point3(0, 0, -1), 0.5, material.Material(Color(255, 0, 0), 0.5, 0.6))]
        ray = self
        # gord = shape.TriangleMesh("gourd.obj", material.Material(Color(1, 0, 1), 0.1, 0.8))
        # airboat = shape.TriangleMesh("shuttle.obj", material.Material(Color(1, 0, 1), 0.1, 0.8))

        # cessna = shape.TriangleMesh("cessna.obj", material.Material(Color(.2,0,.7), 0.2, 0.9))
        # airboat.rotate(90, 0, 0)
        # airboat.translate(0, 0, -10)

        # gord.rotate(90, 0, 0)
        # objects.append(airboat)
        sphere = shape.TriangleMesh("sphere.obj", material.Material(Color(1, 0, 1), 0.1, 0.8))
        # sphere.scale(0.5, 0.5, 0.5)
        # sphere.translate(2, 2, 2)
        # objects.append(sphere)
        #objects = [shape.TriangleMesh("cube.obj", Color(0, 255, 0)), shape.Sphere(Point3(0.5, 0.5, 1.5), 0.1, Color(255, 127.5, 127.5))]
        # objects = [shape.TriangleMesh("gourd.obj", Color(255,0,255))]
        # objects = [shape.TriangleMesh("dodecahedron.obj", Color(125, 255, 125)), shape.Sphere(Point3(0,0,1), 0.1, Color(255,0,0))]
        # sphere = shape.Sphere(Point3(0,0,100), 0.2, material.Material(Color(0,0,1), 0.5, 0.6))
        diamond = shape.TriangleMesh("diamond.obj", material.Material(Color(1.0, 0, 0), 0.20, 0.9))
        diamond1 = shape.TriangleMesh("diamond.obj", material.Material(Color(0, 1, 0), 0.20, 0.9))
        diamond2 = shape.TriangleMesh("diamond.obj", material.Material(Color(0, 0, 1), 0.20, 0.9))
        diamond3 = shape.TriangleMesh("diamond.obj", material.Material(Color(1, 0, 1), 0.20, 0.9))
        diamond4 = shape.TriangleMesh("diamond.obj", material.Material(Color(1, 1, 1), 0.20, 0.9))
        diamond5 = shape.TriangleMesh("diamond.obj", material.Material(Color(0, 1, 1), 0.20, 0.9))
        diamond6 = shape.TriangleMesh("diamond.obj", material.Material(Color(0, 1, 0), 0.20, 0.9))
        diamond7 = shape.TriangleMesh("diamond.obj", material.Material(Color(1.0, 0, 0), 0.20, 0.9))
        diamond8 = shape.TriangleMesh("diamond.obj", material.Material(Color(0, 1, 0), 0.20, 0.9))
        diamond9 = shape.TriangleMesh("diamond.obj", material.Material(Color(0, 0, 1), 0.20, 0.9))
        diamond10 = shape.TriangleMesh("diamond.obj", material.Material(Color(1, 0, 1), 0.20, 0.9))
        diamond11 = shape.TriangleMesh("diamond.obj", material.Material(Color(1, 1, 1), 0.20, 0.9))
        diamond12 = shape.TriangleMesh("diamond.obj", material.Material(Color(0, 1, 1), 0.20, 0.9))
        diamond13 = shape.TriangleMesh("diamond.obj", material.Material(Color(0, 1, 0), 0.20, 0.9))
        diamond.scale(.20, .20, .20)
        diamond.translate(-55,0,0)
        diamond1.scale(.20, .20, .20)
        diamond1.translate(-80,0,0)
        diamond2.scale(.20, .20, .20)
        diamond2.translate(-33,0,0)
        diamond3.scale(.20, .20, .20)
        diamond3.translate(-33,30,0)
        diamond4.scale(.20, .20, .20)
        diamond4.translate(-33,-30,0)
        diamond5.scale(.20, .20, .20)
        diamond5.translate(-80,30,0)
        diamond6.scale(.20,.20,.20)
        diamond6.translate(-80, -30, 0)
        diamond7.scale(.20, .20, .20)
        diamond7.translate(55, -30, 0)
        diamond8.scale(.20, .20, .20)
        diamond8.translate(80, 0, 0)
        diamond9.scale(.20, .20, .20)
        diamond9.translate(30, 0, 0)
        diamond10.scale(.20, .20, .20)
        diamond10.translate(30, 30, 0)
        diamond11.scale(.20, .20, .20)
        diamond11.translate(30, -30, 0)
        diamond12.scale(.20, .20, .20)
        diamond12.translate(80, 30, 0)
        diamond13.scale(.20, .20, .20)
        diamond13.translate(80, -30, 0)
        sphere.translate(0,0,70)
        objects.append(diamond)
        objects.append(diamond1)
        objects.append(diamond2)
        objects.append(diamond3)
        objects.append(diamond4)
        objects.append(diamond5)
        objects.append(diamond6)
        objects.append(diamond7)
        objects.append(diamond8)
        objects.append(diamond9)
        objects.append(diamond10)
        objects.append(diamond11)
        objects.append(diamond12)
        objects.append(diamond13)
        objects.append(sphere)
        # t_max = math.inf
        # front = None
        # for obj in objects:
        #     # if type(obj) is shape.TriangleMesh:
        #     #        impact = obj.hit(ray, t_max)
        #     #        if impact[0] == True:
        #     #             t_max = impact[1]
        #     #             front = impact
        #     temp = obj.hit(ray, t_max)
        #     if temp[0] != False:
        #         if temp[1] < t_max:
        #             t_max = temp[1]
        #             front = temp
        # if front != None:
        #         return front[3]
        # unit_direction = self.direction.unit_vector()
        # t = 0.5 * (unit_direction.y + 1.0)
        # return (1.0 - t) * Color(255, 255, 255) + t * Color(128, 179, 255)


        # The following code is used for part 3
        closest = None
        min_t = math.inf
        for obj in objects:
            impact = obj.hit(ray, min_t)
            if impact[0] != False:
                min_t = impact[1]
                closest = impact
        current_color = Color(0, 0, 0)
        if closest:
            for light in lights:
                current_color = current_color + closest[3].shade(light, closest[2], closest[4], objects)
        current_color = current_color * 255
        if current_color.x > 255:
            current_color.x = 255
        if current_color.y > 255:
            current_color.y = 255
        if current_color.z > 255:
            current_color.z = 255
        return current_color

    def hit_sphere(self, center, radius):
        oc = self.origin - center
        a = self.direction.dot(self.direction)
        b = 2.0 * oc.dot(self.direction)
        c = oc.dot(oc) - radius * radius
        discriminant = b * b - 4 * a * c
        return discriminant > 0