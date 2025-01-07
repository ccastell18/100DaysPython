from turtle import Turtle, Screen, pendown

t = Turtle()
t.shape('turtle')
t.color('red')


#for _ in range(4):
    #timmy_the_turtle.forward(100)
    #timmy_the_turtle.right(90)

#def dashed_line(length, dash_length=10):
    #for i in range (length//(2* dash_length)):
        #t.pendown()
#        t.forward(dash_length)
#        t.penup()
#        t.forward(dash_length)
#dashed_line(250)


#for _ in range(4):
    #timmy_the_turtle.forward(100)
    #timmy_the_turtle.right(90)

#def dashed_line(length, dash_length=10):
    #for i in range (length//(2* dash_length)):
        #t.pendown()
#        t.forward(dash_length)
#        t.penup()
#        t.forward(dash_length)
#dashed_line(250)


def shape(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        t.forward(100)
        t.right(angle)

for shape_side in range(3,11):
    shape(shape_side)


screen = Screen()
screen.exitonclick()
