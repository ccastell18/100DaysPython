# Score
# paddle
# Ball
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong-like Game')
screen.tracer(0)

paddle_1 = Paddle()
paddle_1.goto(300, 0)

paddle_2 = Paddle()
paddle_2.goto(-300, 0)

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(paddle_1.move_up, 'Up')
screen.onkeypress(paddle_1.move_down, 'Down')

screen.onkeypress(paddle_2.move_up, 'a')
screen.onkeypress(paddle_2.move_down, 'z')

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle_1) < 50 and ball.xcor() < 340:
        ball.bounce_x()
    if ball.distance(paddle_2) < 50 and ball.xcor() > -340:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
screen.exitonclick()


