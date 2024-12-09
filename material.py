import ray
from vec3 import *


class Material:
    def __init__(self, color, ambk, difk):
        self.color = color
        self.ambk = ambk
        self.difk = difk

    def shade(self, light, normal, point, objects):
        normal = normal.unit_vector()
        ef_color = light.color * self.color
        amb_comp = ef_color * self.ambk
        in_light = True
        if normal.dot(-light.direction) < 0:
            difk_comp = Color(0, 0, 0)
            in_light = False
        # else:
            # shadow_ray = ray.Ray(point + (normal * .01), -light.direction)
            # for obj in objects:
            #     if obj.hit(shadow_ray, 100)[0]:
            #         difk_comp = Color(0, 0, 0)
            #         in_light = False
            #         break
        if in_light:
            difk_comp = (ef_color * self.difk) * (normal.dot(-light.direction))
        light = amb_comp + difk_comp
        return light