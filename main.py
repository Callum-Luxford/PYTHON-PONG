from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor('black')
screen.title('PONG')

screen.tracer(0)

l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(l_paddle.up,"w")
screen.onkeypress(l_paddle.down,"s")
screen.onkeypress(r_paddle.up,"Up")
screen.onkeypress(r_paddle.down,"Down")

screen.onkeyrelease(l_paddle.up_stop,"w")
screen.onkeyrelease(l_paddle.down_stop,"s")
screen.onkeyrelease(r_paddle.up_stop,"Up")
screen.onkeyrelease(r_paddle.down_stop,"Down")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    # Collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    # Collision with paddle
    if (ball.xcor() == 330 and ball.distance(r_paddle) < 63) or (ball.xcor() == -330 and ball.distance(l_paddle) < 63):
        ball.bounce_x() 

    # Detect R paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    
    # Detect L paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()