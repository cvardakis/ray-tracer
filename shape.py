from abc import ABC, abstractmethod
from vec3 import *

class Shape(ABC):
    @abstractmethod
    def hit(self, ray, t_max=math.inf, t_min=0):
        pass

class Sphere(Shape):

    def __init__(self, center, radius, material):
        self.center = center
        self.radius = radius
        #self.color = color
        self.material = material  #this is needed for part 3 which is the material

    # When using this for the diffuse light section the t_max should be left as a variable.
    def hit(self, ray, t_max, t_min=0):
        oc = ray.origin - self.center
        a = ray.direction.length_squared()
        half_b = oc.dot(ray.direction)
        c = oc.length_squared() - self.radius*self.radius

        discriminant = half_b*half_b - a*c
        if discriminant < 0:
            return (False,)

        sqrtd = math.sqrt(discriminant)

        root = (-half_b - sqrtd) / a
        if (root < t_min) or (t_max < root):
            root = (-half_b + sqrtd) / a
            if (root < t_min) or (t_max < root):
                return (False,)

        t = root
        p = ray.at(t)
        normal = (p - self.center) / self.radius
        return (True, t, normal, self.material)

    def translate(self, x, y, z):
        self.center += Vec3(x, y, z)

    def scale(self, factor):
        self.radius *= factor

class TriangleMesh(Shape):
    def __init__(self, filename, color):
        self.color = color
        self.filename = filename
        self.normals = []
        self.vert = []
        self.triangle_normals = []
        self.triangles = []
        self.read_obj_file()

    def read_obj_file(self):
        vertices = []
        normals = []
        triangles = []
        triangle_normals = []


        fp = open(self.filename, "r")
        # fp.readline()   - BE SURE TO REMOVE THIS LINE (SORRY FOR ERROR)
        all_lines = fp.readlines()
        fp.close()

        for line in all_lines:
            values = line.split()
            # only process lines that contain vertices, normals, and faces
            if len(values) > 3:
                if values[0] == 'v':
                    self.vert.append(Vec3(float(values[1]), float(values[2]), float(values[3])))
                elif values[0] == 'vn':
                    self.normals.append(Vec3(float(values[1]), float(values[2]), float(values[3])))
                elif values[0] == 'f':
                    v = []  # vertex numbers
                    if '/' in line:
                        n = []  # normals
                        # ignoring textures
                        for i in range(1, 4):
                            face = values[i].split('/')
                            v.append(int(face[0]) - 1)  # modify vertex number so first is in 0
                            if len(face[2]):
                                n.append((int(face[2])) - 1)  # modify normal number so first is 0
                        self.triangle_normals.append((n[0], n[1], n[2]))
                    else:
                        for i in range(1, 4):
                            v.append(int(values[i])-1)  # modify vertex number so first is in 0
                    self.triangles.append((Vec3(int(v[0]), int(v[1]), int(v[2]))))
        # print("read", len(vertices), "vertices")
        return triangles, vertices, triangle_normals

    def hit(self, ray, t_max, t_min=0):
    #We will start by calculating t
        triangle_normals = self.triangle_normals
        vertices = self.vert
        triangles = self.triangles
        front = None
        front_t = math.inf
        for tri in range(len(triangles)):
            triangle = triangles[tri]
            #Calculations for verticies and barycentric (I know I didn't spell that correctly)
            ax = vertices[triangle.x].x
            ay = vertices[triangle.x].y
            az = vertices[triangle.x].z
            bx = vertices[triangle.y].x
            by = vertices[triangle.y].y
            bz = vertices[triangle.y].z
            cx = vertices[triangle.z].x
            cy = vertices[triangle.z].y
            cz = vertices[triangle.z].z
            dx = ray.direction.x
            dy = ray.direction.y
            dz = ray.direction.z
            ox = ray.origin.x
            oy = ray.origin.y
            oz = ray.origin.z
            a = ax - bx
            b = ax - cx
            c = dx
            d = ax - ox
            e = ay - by
            f = ay - cy
            g = dy
            h = ay - oy
            i = az - bz
            j = az - cz
            k = dz
            l = az - oz
            denominator = (a*(f*k-g*j)+b*(g*i-e*k)+c*(e*j-f*i))
            if denominator == 0:
                continue
            t = (a*(f*l-h*j)+b*(h*i-e*l)+d*(e*j-f*i))/(a*(f*k-g*j)+b*(g*i-e*k)+c*(e*j-f*i))
            if (t < t_min) or (t > t_max):
                continue
            gamma = (a*(h*k-g*l)+d*(g*i-e*k)+c*(e*l-h*i))/(a*(f*k-g*j)+b*(g*i-e*k)+c*(e*j-f*i))
            if (gamma < 0) or (gamma > 1):
                continue
            beta = (d*(f*k-g*j)+b*(g*l-h*k)+c*(h*j-f*l))/(a*(f*k-g*j)+b*(g*i-e*k)+c*(e*j-f*i))
            if (beta < 0) or (beta > 1 - gamma):
                continue
            alpha = 1 - beta + gamma
            if t < front_t:
                front_t = t
                front = tri
                # calculations for normals, cause I guess I didn't do it
                if triangle_normals:
                    tri_n = triangle_normals[tri]
                    normA = self.normals[tri_n[0]]
                    normB = self.normals[tri_n[1]]
                    normC = self.normals[tri_n[2]]
                    n = (normA * alpha) * (normB * beta) + (normC * gamma)
                else:
                    vertA = vertices[triangle.x]
                    vertB = vertices[triangle.y]
                    vertC = vertices[triangle.z]
                    n = ((vertB - vertA).cross(vertC - vertA).unit_vector())


        if front_t == math.inf:
            return (False, )
        # if math.inf > front_t >= t_min:
        #     return(False, )
        return (True, front_t, n, self.color, ray.at(t))

    # def intersection(self, ray):
    #     for i range len(self.triangles)
    #         if triangles[i]
    #     pass

    def translate(self, x, y, z):
        for i in range(len(self.vert)):
            self.vert[i].x += x
            self.vert[i].y += y
            self.vert[i].z += z

    def rotate(self, x, y, z):
        for i in range(len(self.vert)):
            if x:
                self.vert[i].y = self.vert[i].y * math.cos(math.radians(x)) - self.vert[i].z * math.sin(math.radians(x))
                self.vert[i].z = self.vert[i].y * math.sin(math.radians(x)) + self.vert[i].z * math.cos(math.radians(x))
            if y:
                self.vert[i].x = self.vert[i].x * math.cos(math.radians(y)) - self.vert[i].z * math.sin(math.radians(y))
                self.vert[i].z = self.vert[i].x * math.sin(math.radians(y)) + self.vert[i].z * math.cos(math.radians(y))
            if z:
                self.vert[i].x = self.vert[i].x * math.cos(math.radians(z)) - self.vert[i].y * math.sin(math.radians(z))
                self.vert[i].z = self.vert[i].x * math.sin(math.radians(z)) + self.vert[i].y * math.cos(math.radians(z))


    def scale(self, x, y, z):
        for i in range(len(self.vert)):
            self.vert[i].x *= x
            self.vert[i].y *= y
            self.vert[i].z *= z




