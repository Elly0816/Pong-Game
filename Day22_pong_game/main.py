import turtle
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

# Initialize the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('green')
screen.title('Pong')
screen.tracer(0)
line = turtle.Turtle()
line.penup()
line.color('white')
line.setposition(0, 300)
line.right(90)
line.width(5)
line.pendown()
line.forward(600)
line.hideturtle()


# Create right and left paddles
left_p = Paddle((-350, 0))
right_p = Paddle((350, 0))
ball = Ball()

# Initialise the scoreboard
score = Scoreboard()

# Listen for key presses
screen.listen()
screen.onkey(right_p.up, 'Up')
screen.onkey(right_p.down, 'Down')
screen.onkey(left_p.up, 'w')
screen.onkey(left_p.down, 's')

game_on = True

sleep = 0.1

while game_on:
    time.sleep(sleep)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.deflect_wall()

    # Detect collision with right paddle and left paddle
    if (ball.distance(right_p) < 50 and ball.xcor() > 320) or (ball.distance(left_p) < 50 and ball.xcor() < -320):
        ball.deflect_paddle()
        if sleep > 0:
            sleep -= 0.005

    #   Detect if the right paddle misses the ball
    if (ball.distance(right_p) >= 50 and ball.xcor() > 380):
        ball.reset_position()
        score.left_win()
        sleep = 0.1

    #   Detect if the left paddle misses the ball
    elif (ball.distance(left_p) >= 50 and ball.xcor() < -380):
        ball.reset_position()
        score.right_win()
        sleep = 0.1





screen.exitonclick()
