import colorgram
import turtle as turtle_module
import random

t = turtle_module.Turtle()
screen = turtle_module.Screen()
screen.colormode(255)

#colors = colorgram.extract('download.jpeg', 10)
#rgb_colors = []

#for color in colors:
 #   r = color.rgb.r
 #   g = color.rgb.g
 #   b = color.rgb.b
 #   new_color = (r, g, b)
 #   rgb_colors.append(new_color)

color_list = [(247, 240, 230), (234, 240, 246), (237, 247, 243), (248, 237, 242), (148, 165, 182), (197, 159, 131),
              (188, 146, 155), (20, 33, 47), (77, 102, 120), (147, 174, 162)]
t.penup()
t.setheading(225)
t.forward(250)
t.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots):
    t.dot(20, random.choice(color_list))
    t.forward(50)

    if dot_count % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)

screen.exitonclick()
