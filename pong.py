from turtle import Screen
from padle import Paddle


screen = Screen()

screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.tracer(0)

paddle = Paddle()
screen.listen()
screen.onkey(fun=paddle.move_up, key="Up")
screen.onkey(fun=paddle.move_down, key="Down")


game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()