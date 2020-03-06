# Notes -  Turtle Recursion



'''
Turtle is an introductory graphics program for learning.
'''


import turtle


my_turtle = turtle.Turtle()
my_turtle.showturtle()
my_turtle.shape("turtle")
my_turtle.speed(0)  # set speed 0 is fastest


# Set Up My Screen

my_screen = turtle.Screen()
my_screen.bgcolor("blue")


# Draw A Shape using go-to method

# Red Square
my_turtle.fillcolor("green")
my_turtle.begin_fill()  # Starts a shape which will be filled

my_turtle.goto(200, 0)  # bottom right
my_turtle.goto(200, 200)  # top right
my_turtle.goto(0, 200)  # top left
my_turtle.goto(0, 0)  # bottom left

my_turtle.end_fill()  # end to fill shape that was drawn above


# draw shape using headings
my_turtle.up()
my_turtle.goto(-200, 200)
my_turtle.down()
my_turtle.setheading(270)  # face south

my_turtle.fillcolor("light green")
my_turtle.begin_fill()

# draw octagon
for i in range(8):
    my_turtle.forward(50)
    my_turtle.left(45)

my_turtle.end_fill()


my_screen.clear()


def recursive_rect(width, height, depth):
    if depth > 0:
        my_turtle.width(depth)
        my_turtle.up()
        my_turtle.goto(width / 2, height / 2)  # top right
        my_turtle.down()
        my_turtle.goto(-width / 2, height / 2)  # top left
        my_turtle.goto(-width / 2, -height / 2)  # bottom left
        my_turtle.goto(width / 2, -height / 2)  # bottom right
        my_turtle.goto(width / 2, height / 2)  # back to beginning
        recursive_rect(width / 1.5, height / 1.5, depth - 1)

recursive_rect(400, 200, 7)


my_screen.clear()


def recursive_ncaa(x, y, height, depth):
    if depth > 0:
        my_turtle.up()
        my_turtle.goto(x, y)
        my_turtle.down()
        my_turtle.setheading(0)
        my_turtle.forward(50)
        my_turtle.left(90)
        my_turtle.forward(height / 2)
        my_turtle.right(90)
        my_turtle.forward(50)
        my_turtle.up()
        my_turtle.goto(x, y)
        my_turtle.down()
        my_turtle.setheading(0)
        my_turtle.forward(50)
        my_turtle.right(90)
        my_turtle.forward(height / 2)
        my_turtle.left(90)
        my_turtle.forward(50)
        recursive_ncaa(x + 100, y + height / 2, height / 2, depth - 1)  # top bracket
        recursive_ncaa(x + 100, y - height / 2, height / 2, depth - 1)


recursive_ncaa(-300, 0, 300, 6)

my_screen.clear()

def recursive_ncaa(x, y, height, depth):
    if depth > 0:
        my_turtle.up()
        my_turtle.goto(x, y)
        my_turtle.down()
        my_turtle.goto(x + height, y)
        my_turtle.goto(x + height, y + height / 2)
        my_turtle.goto(x + height, y - height / 2)
        recursive_ncaa(x + 100, y + height / 2, height / 2, depth - 1)  # top bracket
        recursive_ncaa(x + 100, y - height / 2, height / 2, depth - 1)

recursive_ncaa(-300, 0, 300, 6)

my_screen.exitonclick()