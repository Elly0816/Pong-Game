from turtle import Turtle, Screen


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.setpos(position)
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color('white')

    def up(self):
        if self.ycor() <= 270 or self.ycor() >= -270:
            self.sety(self.ycor()+20)
        else:
            self.sety(self.ycor())

    def down(self):
        if self.ycor() <= 270 or self.ycor() >= -270:
            self.sety(self.ycor()-20)
        else:
            self.sety(self.ycor())


