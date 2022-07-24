import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_card import ScoreBoard

screen = Screen()

screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)

# paddle
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
# ball
ball = Ball()
# score card
l_score = ScoreBoard()
r_score = ScoreBoard()
screen.listen()
screen.onkey(fun=r_paddle.go_up, key='Up')
screen.onkey(fun=r_paddle.go_down, key='Down')

screen.onkey(fun=l_paddle.go_up, key='w')
screen.onkey(fun=l_paddle.go_down, key='s')

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with top and bottom wall
    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce()

    # detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.kick()
    # detect collision with left and right wall
    if ball.xcor() < -380:
        ball.reset_position()
        r_score.r_increment_score()
    if ball.xcor() > 380:
        ball.reset_position()
        l_score.l_increment_score()

screen.exitonclick()
