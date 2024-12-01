from turtle import Screen
from padle import Paddle


screen = Screen()

screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("PONG GAME")

paddle = Paddle()
screen.listen()
screen.onkey(fun=paddle.move_up, key="Up")
screen.onkey(fun=paddle.move_down, key="Down")

screen.exitonclick()