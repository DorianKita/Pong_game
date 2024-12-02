from turtle import Screen
from padle import Paddle
from ball import Ball

screen = Screen()
ball = Ball()


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
    ball.move()
    screen.update()

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce()

screen.exitonclick()