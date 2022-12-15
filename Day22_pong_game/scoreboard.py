from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.goto(-80, 180)
        self.write(self.l_score, align='center', font=('courier', 80, 'normal'))
        self.goto(80, 180)
        self.write(self.r_score, align='center', font=('courier', 80, 'normal'))

    def right_win(self):
        self.r_score +=1
        self.clear()
        self.update_score()

    def left_win(self):
        self.l_score +=1
        self.clear()
        self.update_score()

