from Triangle import Triangle
import turtle
import random

triangles = []
hex_alphabet = [str(hex(i))[2:] for i in range(16)]

for i in range(100):
    x1, y1 = random.randint(-100, 100), random.randint(-100, 100)
    x2, y2 = random.randint(-100, 100), random.randint(-100, 100)

    t = Triangle(x1, y1, x2, y2)

    x, y = random.randint(-100, 100), random.randint(-100, 100)

    t.set_position(x, y)

    color = '#'

    for c in range(6):
        color += hex_alphabet[random.randint(0, 15)]

    t.set_color(color)

    triangles.append(t)

for triangle in triangles:
    triangle.draw()

turtle.mainloop()
