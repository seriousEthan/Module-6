class Point:

    """A class to locate points"""


    def __init__(self, x, y):

        self.x = x

        self.y = y



    def __str__(self):

        return '({0}, {1})'.format(self.x, self.y)





class Rectangle:

    """A class to manufacture rectangle objects"""


    def __init__(self, posn, w, h):

        """Initialize rectangle at posn, with width w and height h"""

        self.corner = posn

        self.width = w

        self.height = h



    def __str__(self):

        return '{0}, {1}, {2}'.format(self.corner, self.width, self.height)





def create_rectangle(x, y, width, height):

    """Creates a rectangle object"""

    return Rectangle(Point(x, y), width, height)


box = Rectangle(Point(0, 0), 100, 200)
bomb = Rectangle(Point(100, 80), 5, 10) # In my video game
print("box: ", box)
print("bomb: ", bomb)


def str_rectangle(rect):

    """Returns a string representing the rectangle"""

    return str(rect)





def shift_rectangle(rect, dx, dy):

    """Moves the rectangle by adding the input values to x and y"""

    ix, iy = rect.corner.x, rect.corner.y

    rect.corner.x = ix + dx

    rect.corner.y = iy + dy





def offset_rectangle(rect, dx, dy):

    """Moves the rectangle and returns a new rectangle object"""

    ix, iy = rect.corner.x, rect.corner.y

    return create_rectangle(ix + dx, iy + dy, rect.width, rect.height)



# Checking to make sure the functions work

r1 = create_rectangle(10, 20, 30, 40)

print(str_rectangle(r1))

shift_rectangle(r1, -10, -20)

print(str_rectangle(r1))

r2 = offset_rectangle(r1, 100, 100)

print(str_rectangle(r1))

print(str_rectangle(r2))

# Works like a charm!

import turtle

# I found a way to actually draw the squares so I thought I'd try that too
ethan = turtle.Turtle()

ethan.color("#006747", "#CFC493") # USF green outline, USF gold fill

ethan.penup() # moving to the correct corner position
ethan.forward(10)
ethan.left(90)
ethan.forward(20)
ethan.pendown()

ethan.begin_fill() # drawing the first rectangle
ethan.right(90)
ethan.forward(30)
ethan.left(90)
ethan.forward(40)
ethan.left(90)
ethan.forward(30)
ethan.left(90)
ethan.forward(40)
ethan.end_fill()

ethan.penup() # Moving to the start of the second rectangle
ethan.right(90)
ethan.forward(10)
ethan.left(90)
ethan.forward(20)
ethan.pendown()

ethan.begin_fill() # drawing the second rectangle
ethan.left(90)
ethan.forward(30)
ethan.left(90)
ethan.forward(40)
ethan.left(90)
ethan.forward(30)
ethan.left(90)
ethan.forward(40)
ethan.end_fill()

ethan.penup() # moving to the third rectangle
ethan.left(90)
ethan.forward(100)
ethan.left(90)
ethan.forward(100)
ethan.pendown()

ethan.begin_fill() # drawing the third rectangle
ethan.right(90)
ethan.forward(30)
ethan.left(90)
ethan.forward(40)
ethan.left(90)
ethan.forward(30)
ethan.left(90)
ethan.forward(40)
ethan.end_fill()


turtle.done()