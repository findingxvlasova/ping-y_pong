import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreborad import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")

paddle_right = Paddle()
paddle_left = Paddle(-350, 0)
ball = Ball()
scoreborads = Scoreboard()

screen.listen()
screen.onkey(paddle_right.go_up, "Up")
screen.onkey(paddle_right.go_down, "Down")

screen.onkey(paddle_left.go_up, "w")
screen.onkey(paddle_left.go_down,"s")

game_is_on = True
while game_is_on:
    time.sleep(0.0001)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()

    if ball.xcor() > 400 or ball.xcor() < -400:
        ball.reset_position()

    if ball.distance(paddle_right) < 20 and ball.xcor() > 320 or ball.distance(paddle_left) < 20 and ball.xcor() < -320:
        ball.paddle_bounce()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreborads.inrease_l()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreborads.inrease_r()

screen.exitonclick()