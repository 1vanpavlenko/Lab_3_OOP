from Triangle import Triangle
import turtle

triangle = Triangle(100, 100, 100, 0)

triangle.set_color("#FEDCBA")
triangle.draw()

triangle.set_position(-100, 200)

triangle.set_color("#ABCDEF")
triangle.draw()

turtle.mainloop()
