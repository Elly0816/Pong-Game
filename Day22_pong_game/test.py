from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
screen.setup(width=500, height=500)
tim.speed(10)

for _ in range(250):
    tim.setheading(random.randrange(0, 360))
    tim.forward(10)

screen.exitonclick()