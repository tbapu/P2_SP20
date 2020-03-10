'''
Turtle Recursion (30pts)

1)  Using the turtle library, create the H fractal pattern as shown in the image (htree4.jpg) in this directory. (15pts)

2)  Using the turtle library, create any of the other recursive patterns in the directory. (10pts)

3)  Create your own work of art with a repeating pattern of your making.  It must be a repeated pattern using recursion. Snowflakes, trees, and spirals are a common choice.  Or you can create a third one from the directory. (5pt)


 Each fractal should
 - be recursive
 - have a depth of at least 4
 - be contained on the screen

  Have fun!

'''



import turtle

my_turtle = turtle.Turtle()
my_turtle.showturtle()
my_turtle.shape("turtle")
my_screen = turtle.Screen()
my_screen.bgcolor("blue")
my_turtle.fillcolor("green")
my_turtle.speed(0)



# H - Tree
def recursive_H(x, y, height, width, depth):
    if depth > 0:
        for i in range(2):
            my_turtle.up()
            my_turtle.goto(x, y)
            my_turtle.down()
            my_turtle.goto(x + width, y)
            my_turtle.goto(x + width, y + height / 2)
            my_turtle.goto(x + width, y - height / 2)
            recursive_H(x + width, y + height / 2, height / 2, width / 2, depth - 1)
            recursive_H(x + width, y - height / 2, height / 2, width / 2, depth - 1)
            height, width = -height, -width

# Squares
def recursive_S(x, y, height, width, depth):
    if depth > 0:
        my_turtle.up()
        my_turtle.goto(x + width, y + height)
        my_turtle.down()
        my_turtle.begin_fill()
        my_turtle.goto(x + width, y - height)
        my_turtle.goto(x - width, y - height)
        my_turtle.goto(x - width, y + height)
        my_turtle.goto(x + width, y + height)
        my_turtle.end_fill()
        recursive_S(x + width, y + height, height / 2, width / 2, depth - 1)
        recursive_S(x + width, y - height, height / 2, width / 2, depth - 1)
        recursive_S(x - width, y + height, height / 2, width / 2, depth - 1)
        recursive_S(x - width, y - height, height / 2, width / 2, depth - 1)

# Sierpenski_Triangles
def recursive_T(x, y, height, width, depth):
    if depth > 0:
        my_turtle.up()
        my_turtle.goto(x - width / 2, y - height / 2)
        my_turtle.down()
        my_turtle.goto(x, y + height / 2)
        my_turtle.goto(x + width / 2, y - height / 2)
        my_turtle.goto(x - width / 2, y - height / 2)
        my_turtle.goto(x - width / 4, y)
        my_turtle.goto(x + width / 4, y)
        my_turtle.goto(x, y - height / 2)
        my_turtle.goto(x - width / 4, y)
        recursive_T(x, y + height / 4, height / 2, width / 2, depth - 1)
        recursive_T(x - width / 4, y - height / 4, height / 2, width / 2, depth - 1)
        recursive_T(x + width / 4, y - height / 4, height / 2, width / 2, depth - 1)

# Escher Fractal
def escher(x, y, height, width, depth):
    if depth > 0:
        my_turtle.up()
        my_turtle.goto(x - width / 2, y - height / 2)
        my_turtle.down()
        my_turtle.goto(x - width / 2, y + height / 2)
        my_turtle.goto(x + width / 2, y + height / 2)
        my_turtle.goto(x + width / 2, y - height / 2)
        my_turtle.goto(x - width / 2, y - height / 2)
        my_turtle.goto(x - width / 2, y)
        my_turtle.goto(x, y + height / 2)
        my_turtle.goto(x + width / 2, y)
        my_turtle.goto(x, y - height / 2)
        my_turtle.goto(x - width / 2, y)
        escher(x, y, height / 2, width / 2, depth - 1)
        
# Plus Fractal
def plus(x, y, height, width, depth):
    if depth > 0:
        my_turtle.up()
        my_turtle.goto(x, y)
        my_turtle.down()
        my_turtle.goto(x - width / 2, y)
        my_turtle.goto(x + width / 2, y)
        my_turtle.goto(x, y)
        my_turtle.goto(x, y - height / 2)
        my_turtle.goto(x, y + height / 2)
        plus(x - width / 2, y, height / 2, width / 2, depth - 1)
        plus(x + width / 2, y, height / 2, width / 2, depth - 1)
        plus(x, y - height / 2, height / 2, width / 2, depth - 1)
        plus(x, y + height / 2, height / 2, width / 2, depth - 1)
        
# Snowflake Fractal
def snowflake(x, y, height, width, depth):
    if depth > 0:
        my_turtle.up()
        my_turtle.goto(x, y)
        my_turtle.down()
        my_turtle.goto(x + width / 2, y)
        my_turtle.goto(x - width / 2, y)
        my_turtle.goto(x, y)
        my_turtle.goto(x + width / 4, y + height / 2)
        my_turtle.goto(x - width / 4, y - height / 2)
        my_turtle.goto(x, y)
        my_turtle.goto(x - width / 4, y + height / 2)
        my_turtle.goto(x + width / 4, y - height / 2)
        snowflake(x + width / 2, y, height / 3, width / 3, depth - 1)
        snowflake(x - width / 2, y, height / 3, width / 3, depth - 1)
        snowflake(x + width / 4, y + height / 2, height / 3, width / 3, depth - 1)
        snowflake(x - width / 4, y - height / 2, height / 3, width / 3, depth - 1)
        snowflake(x - width / 4, y + height / 2, height / 3, width / 3, depth - 1)
        snowflake(x + width / 4, y - height / 2, height / 3, width / 3, depth - 1)
        
# My Fractal
def my_fractal(x, y, height, width, depth):
    my_screen.bgcolor("black")
    for i in range(2):
        if depth > 0:
            my_turtle.up()
            my_turtle.goto(x + width / 6, y + height / 6)
            my_turtle.down()
            my_turtle.begin_fill()
            my_turtle.goto(x - width / 6, y + height / 6)
            my_turtle.goto(x - width / 3, y)
            my_turtle.goto(x + width / 3, y)
            my_turtle.goto(x + width / 6, y + height / 6)
            my_fractal(x + width / 6, y + height / 6, height / 2, width / 2, depth - 1)
            my_fractal(x - width / 6, y + height / 6, height / 2, width / 2, depth - 1)
            my_fractal(x + width / 3, y, height / 2, width / 2, depth - 1)
            my_fractal(x - width / 3, y, height / 2, width / 2, depth - 1)
        height= -height
        my_turtle.fillcolor("red")
        my_turtle.end_fill()

# H - Tree
recursive_H(0, 0, my_screen.window_height() / 2, my_screen.window_width() / 4, 3)
my_screen.clear()

# Squares
recursive_S(0, 0, my_screen.window_height() / 5, my_screen.window_width() / 5, 4)
my_screen.clear()

# Sierpenski_Triangles
recursive_T(0, 0, my_screen.window_height() - 100, my_screen.window_width() - 100, 5)
my_screen.clear()

# Escher Fractal
escher(0, 0, my_screen.window_height() - 100, my_screen.window_width() - 100, 7)
my_screen.clear()

# Plus Fractal
plus(0, 0, my_screen.window_height() / 2, my_screen.window_width() / 2, 4)
my_screen.clear()

# Snowflake Fractal
snowflake(0, 0, my_screen.window_height() / 2, my_screen.window_width() / 2, 4)

# My Fractal
my_fractal(0, 0, my_screen.window_height() / 2, my_screen.window_width() / 2, 4)


my_screen.exitonclick()