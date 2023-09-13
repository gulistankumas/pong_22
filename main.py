from turtle import Turtle, Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard



screen= Screen()
screen.bgcolor("Black")
screen.screensize(canvwidth=800, canvheight=600)
screen.title("GK's Pong Game")
screen.tracer(0)


r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball= Ball()
Scoreboard= Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up ,"Up")
screen.onkey(r_paddle.go_down ,"Down")
screen.onkey(l_paddle.go_up ,"w")
screen.onkey(l_paddle.go_down ,"s")




game_is_on= True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

     # üst alt duvara değip sekme

    if ball.ycor() >280 or ball.xcor() < - 280 :
        ball.bounce_y()

    #  paddlea değip sekme
   
    if ball.distance(r_paddle) < 50 and ball.xcor() >320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #right paddle topu kaçırdıysa

    if ball.xcor() >380:
        ball.reset_position()
        Scoreboard.l_point()

    if ball.xcor() <-380:
        ball.reset_position()
        Scoreboard.r_point()
        
        


screen.exitonclick()