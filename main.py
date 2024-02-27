from Triangle import Triangle
import turtle
import random

triangles = []

# for i in range(100):
#     x1, y1 = random.randint(-100, 100), random.randint(-100, 100)
#     x2, y2 = random.randint(-100, 100), random.randint(-100, 100)
#
#     t = Triangle(x1, y1, x2, y2)
#
#     x, y = random.randint(-100, 100), random.randint(-100, 100)
#
#     t.set_position(x, y)
#
#     r, g, b = (random.randint(0, 255) for _ in range(3))
#
#     color = r << 16 | g << 8 | b
#
#     hex_color = str(hex(color))[2:]
#
#     if len(hex_color) < 6:
#         hex_color = (6 - len(hex_color)) * '0' + hex_color
#
#     t.set_color('#' + hex_color)
#
#     triangles.append(t)
#
# for triangle in triangles:
#     triangle.draw()

turtle.speed(0)

triangle = Triangle(100, 100, 100, 0)
triangle.draw()

for degree in range(3, 363, 3):
    triangle.set_rotation_degree(degree)
    triangle.draw()
    triangle.move(0, -1 / 3)

    turtle.clear() if degree < 360 else turtle

turtle.mainloop()
