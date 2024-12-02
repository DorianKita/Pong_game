from turtle import Screen
from padle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
ball = Ball()
scoreboard = Scoreboard()

screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.tracer(0)


r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
screen.listen()
screen.onkey(fun=r_paddle.move_up, key="Up")
screen.onkey(fun=r_paddle.move_down, key="Down")
screen.onkey(fun=l_paddle.move_up, key="w")
screen.onkey(fun=l_paddle.move_down, key="s")



game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    ball.move()
    screen.update()

    # Collision with walls
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # Collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    # Reset ball after score
    if ball.xcor() > 400:
        scoreboard.l_point()
        ball.reset_position()
    if ball.xcor() < -400:
        scoreboard.r_point()
        ball.reset_position()


screen.exitonclick()