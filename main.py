from ray import *
from vec3 import *

# Connor Vardakis
# This project was a lot of exposure for the proper way to call methods.
# Prior to this project I was struggling to run methods correctly. I feel I now have a better
# understanding on how the files interact with each other.

if __name__ == "__main__":
    # Image
    aspect_ratio = 16 / 9
    image_width = 400
    image_height = (image_width / aspect_ratio)

    # Camera
    viewport_height = 2.0
    viewport_width = aspect_ratio * viewport_height
    focal_length = 1.0

    # origin = Point3(0.5, 0.5, 2)
    # origin = Point3(0, 0, 2)  # This is the origin for part 2 OBJ Files
    # origin = Point3(0, 0, 0) # This is the origin for parts 1 and 3
    # origin = Point3(-1.0, 0.5, 2.5) #gourd lighting
    origin = Point3(0, 0, 80) #diamond obj
    # origin = Point3(0, 0.75, 4)
    horizontal = Vec3(viewport_width, 0, 0)
    vertical = Vec3(0, viewport_height, 0)
    lower_left_corner = origin - horizontal / 2 - vertical / 2 - Vec3(0, 0, focal_length)

    # Render
    image = open("cessna.ppm", "w")
    image.write("P3\n")
    image.write(str(image_width))
    image.write(" ")
    image.write(str(int(image_height)))
    image.write("\n")
    image.write("255")
    image.write("\n")
    for j in reversed(range(int(image_height))):
        if j % 10 == 0:
            print("Scanlines remaining: ", j)
        for i in range(image_width):
            u = i / (image_width - 1)
            v = j / (image_height - 1)
            r = Ray(origin, lower_left_corner + u * horizontal + v * vertical - origin)
            pixel_color = r.ray_color
            pixel_color.x = int(pixel_color.x)
            pixel_color.y = int(pixel_color.y)
            pixel_color.z = int(pixel_color.z)
            image.write(str(pixel_color))
    image.close()
