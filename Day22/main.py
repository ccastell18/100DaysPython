# Score
# paddle
# Ball
from turtle import Screen, Turtle
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong-like Game')
screen.tracer(0)

paddle_1 = Paddle()
paddle_1.goto(300, 0)

paddle_2 = Paddle()
paddle_2.goto(-300, 0)

screen.listen()
screen.onkeypress(paddle_1.move_up, 'Up')
screen.onkeypress(paddle_1.move_down, 'Down')

screen.onkeypress(paddle_2.move_up, 'a')
screen.onkeypress(paddle_2.move_down, 'z')

game_is_on = True
while game_is_on:
    screen.update()



screen.exitonclick()
