from turtle import Turtle
import random

HEADING = random.randint(0, 360)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')
        self.x_move = 10
        self.y_move = 10

    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.setpos(x, y)

    def deflect_wall(self):
        self.y_move *= -1

    def deflect_paddle(self):
        self.x_move *= -1

    def reset_position(self):
        self.home()
        self.deflect_paddle()
