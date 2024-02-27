import turtle
from math import sin, cos, pi, radians


class Triangle:
    default_color = "#000000"

    def __init__(self, x1, y1, x2, y2):
        self.vertex1 = (x1, y1)
        self.vertex2 = (x2, y2)

        self.color = Triangle.default_color

        self.position = (0, 0)

        self.rotation = 0

    def set_position(self, x, y):
        self.position = (x, y)

    def move(self, dx, dy):
        self.position = (self.position[0] + dx, self.position[1] + dy)

    def set_rotation(self, rotation):
        self.rotation = rotation

    def set_rotation_degree(self, degree):
        self.rotation = radians(degree)

    def rotation_matrix(self):
        fi = self.rotation

        fi_matrix = [[cos(fi), -sin(fi)],
                     [sin(fi), cos(fi)]]

        return fi_matrix

    @staticmethod
    def mult_matrix_vector(m, v):
        turned_vertex = [0, 0]

        turned_vertex[0] = m[0][0] * v[0] + m[0][1] * v[1]
        turned_vertex[1] = m[1][0] * v[0] + m[1][1] * v[1]

        return turned_vertex

    def set_color(self, color):
        self.color = color

    def calc_abs_pos(self):
        m = self.rotation_matrix()

        turned_vertex1 = self.mult_matrix_vector(m, self.vertex1)
        turned_vertex2 = self.mult_matrix_vector(m, self.vertex2)

        v1 = (self.position[0] + turned_vertex1[0],
              self.position[1] + turned_vertex1[1])

        v2 = (self.position[0] + turned_vertex2[0],
              self.position[1] + turned_vertex2[1])

        return v1, v2

    def draw(self):
        v1, v2 = self.calc_abs_pos()

        turtle.color(self.color)

        turtle.up()

        turtle.setpos(*self.position)

        turtle.down()

        turtle.goto(*v1)
        turtle.goto(*v2)

        turtle.setpos(*self.position)

        turtle.up()

        turtle.color(Triangle.default_color)
