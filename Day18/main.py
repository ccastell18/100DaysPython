#
# t = Turtle()
# t.shape('turtle')
# t.color('red')

# for _ in range(4):
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)

# def dashed_line(length, dash_length=10):
# for i in range (length//(2* dash_length)):
# t.pendown()
#        t.forward(dash_length)
#        t.penup()
#        t.forward(dash_length)
# dashed_line(250)


# for _ in range(4):
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)

# def dashed_line(length, dash_length=10):
# for i in range (length//(2* dash_length)):
# t.pendown()from turtle import Turtle, Screen, pendown

# t = Turtle()
# t.shape('turtle')
# t.color('red')


# for _ in range(4):
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)

# def dashed_line(length, dash_length=10):
# for i in range (length//(2* dash_length)):
# t.pendown()
#        t.forward(dash_length)
#        t.penup()
#        t.forward(dash_length)
# dashed_line(250)


# for _ in range(4):
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)

# def dashed_line(length, dash_length=10):
# for i in range (length//(2* dash_length)):
# t.pendown()
#        t.forward(dash_length)
#        t.penup()
#        t.forward(dash_length)
# dashed_line(250)


# def shape(num_sides):
#   angle = 360/num_sides
#   for _ in range(num_sides):
#       t.forward(100)
#       t.right(angle)

# for shape_side in range(3,11):
#    shape(shape_side)
from turtle import Turtle, Screen
import random

t = Turtle()
screen = Screen()
t.pensize(width=2)
t.speed('fastest')
screen.colormode(255)

# def move_randomly():
#   colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'black', 'cyan', 'magenta', 'brown', 'gold',
#            'turquoise', 'violet', 'maroon', 'navy']
#   angles = [0, 90, 180, 270]
#  t.pendown()
# t.setheading(random.choice(angles))
# t.color(random.choice(colors))
# t.forward(50)


# for _ in range(200):
# move_randomly]
t.hideturtle()


def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    color = (red, green, blue)
    return color


def draw_spirograph(size_gap):
    for _ in range(int(360/size_gap)):
        t.color(random_color())
        t.circle(100)
        t.setheading(t.heading() + size_gap)

draw_spirograph(5)

screen.exitonclick()

#        t.forward(dash_length)
#        t.penup()
#        t.forward(dash_length)
# dashed_line(250)


# def shape(num_sides):
#   angle = 360 / num_sides
#  for _ in range(num_sides):
#     t.forward(100)
#    t.right(angle)


# for shape_side in range(3, 11):
#   shape(shape_side)
