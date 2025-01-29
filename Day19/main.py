from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make Your Bet", prompt="What color turtle will win?")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y = [ -70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0,6):
    t = Turtle(shape="turtle")
    t.color(colors[turtle_index])
    t.penup()
    t.goto(x=-230, y=y[turtle_index])
    all_turtles.append(t)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 220:
            is_race_on = False
            winning_color = t.pencolor()
            if winning_color != user_bet:
                print("Sorry. Your turtle lost!")
            else:
                print(f"You've won! the {winning_color} turtle is the winner")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()