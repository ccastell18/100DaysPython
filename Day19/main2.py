from player import Turtle, Screen

t = Turtle()
screen = Screen()


def move_forwards():
    t.forward(10)


screen.listen()
screen.onkey(key="space", fun=move_forwards)
screen.exitonclick()
