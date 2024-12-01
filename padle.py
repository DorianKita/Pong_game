from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed('fastest')
        self.resizemode('user')
        self.color('white')
        self.shapesize(5,1)
        self.goto(x=350,y=0)
        self.shape('square')


    def move_up(self):
        self.goto(x=350,y= self.ycor() + 30)

    def move_down(self):
        self.goto(x=350,y= self.ycor() - 30)