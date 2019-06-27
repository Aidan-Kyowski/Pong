#-------------------------------------------------------------------------------
# Name:        Pong
# Purpose:
#
# Author:      Aidan Kyowski
#
# Created:     24/06/2019
#-------------------------------------------------------------------------------
from turtle import *
from winsound import *
from random import randrange

gm = screensize(400,300)
bgcolor("black")
tracer(0,0)

    #score counting
score_1 = 0
score_2 = 0

    #player 1
paddle_1 = Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("white")
paddle_1.shapesize(5,1)
paddle_1.penup()
paddle_1.goto(-350,0)

    #player 2
paddle_2 = Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("white")
paddle_2.shapesize(5,1)
paddle_2.penup()
paddle_2.goto(350,0)

    #center line
part1 = Turtle()
part1.speed (0)
part1.shape("square")
part1.color("white")
part1.shapesize(1.5, 0.5)
part1.penup()
part1.goto(0, 0)

part2 = Turtle()
part2.speed (0)
part2.shape("square")
part2.color("white")
part2.shapesize(1.5, 0.5)
part2.penup()
part2.goto(0, -75)

part3 = Turtle()
part3.speed (0)
part3.shape("square")
part3.color("white")
part3.shapesize(1.5, 0.5)
part3.penup()
part3.goto(0, 75)

part4 = Turtle()
part4.speed (0)
part4.shape("square")
part4.color("white")
part4.shapesize(1.5, 0.5)
part4.penup()
part4.goto(0, -150)

part5 = Turtle()
part5.speed (0)
part5.shape("square")
part5.color("white")
part5.shapesize(1.5, 0.5)
part5.penup()
part5.goto(0, 150)

part6 = Turtle()
part6.speed (0)
part6.shape("square")
part6.color("white")
part6.shapesize(1.5, 0.5)
part6.penup()
part6.goto(0, -225)

part7 = Turtle()
part7.speed (0)
part7.shape("square")
part7.color("white")
part7.shapesize(1.5, 0.5)
part7.penup()
part7.goto(0, 225)

part8 = Turtle()
part8.speed (0)
part8.shape("square")
part8.color("white")
part8.shapesize(1.5, 0.5)
part8.penup()
part8.goto(0, -300)

part9 = Turtle()
part9.speed (0)
part9.shape("square")
part9.color("white")
part9.shapesize(1.5, 0.5)
part9.penup()
part9.goto(0, 300)

    #ball
ball = Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)

#ball movement
value = randrange(1,4)
if value == 1:
    startx = 0.5
    starty = 0.5
elif value == 2:
    startx = 0.5
    starty = -0.5
elif value == 3:
    startx = -0.5
    starty = 0.5
elif value == 4:
    startx = -0.5
    starty = -0.5
ball.dx = startx
ball.dy = starty

    #starting score
score = Turtle()
score.speed (0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("0                                                   0", align="center", font=("Arial", 25, "normal"))

    #end game
def endgame():
    bye()

    #paddle movement
def paddle_1up():
    a = paddle_1.ycor()
    if a < 250:
        a = a + 20
        paddle_1.penup()
        paddle_1.goto(-350,a)
    else:
        a=a

def paddle_1down():
    b = paddle_1.ycor()
    if b > -250:
        b = b - 20
        paddle_1.penup()
        paddle_1.goto(-350,b)
    else:
        b = b

def paddle_2up():
    c = paddle_2.ycor()
    if c < 250:
        c = c + 20
        paddle_2.penup()
        paddle_2.goto(350,c)
    else:
        c = c
def paddle_2down():

   d = paddle_2.ycor()
   if d > -250:
        d = d - 20
        paddle_2.penup()
        paddle_2.goto(350,d)
   else:
        d = d

onkeypress(endgame, "space")
onkeypress(paddle_1up,"w")
onkeypress(paddle_1down,"s")
onkeypress(paddle_2up,"Up")
onkeypress(paddle_2down,"Down")
listen()

    #respawning of the ball
def ballstart():
    if ball.dx > 0 and ball.dy > 0:
        ball.dx = -0.5
        ball.dy = -0.5
    elif ball.dx > 0 and ball.dy < 0:
        ball.dx = -0.5
        ball.dy = 0.5
    elif ball.dx < 0 and ball.dy < 0:
        ball.dx = 0.5
        ball.dy = 0.5
    elif ball.dx < 0 and ball.dy > 0:
        ball.dx = 0.5
        ball.dy = -0.5
    else:
        exit

#main game
while True:
    update()

    #move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border check
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1
        PlaySound("bounce.wav", SND_ASYNC)

    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *= -1
        PlaySound("bounce.wav", SND_ASYNC)

    if ball.xcor()>390:
        ball.goto(0,0)
        ballstart()
        score_1 = score_1 + 1
        score.clear()
        score.write("{}                                                   {}".format(score_1, score_2), align="center", font=("Arial", 25, "normal"))

    if ball.xcor()<-390:
        ball.goto(0,0)
        ballstart()
        score_2 = score_2 + 1
        score.clear()
        score.write("{}                                                   {}".format(score_1, score_2), align="center", font=("Arial", 25, "normal"))

    #paddle and ball colisions
    if (ball.xcor() > 330 and ball.xcor() < 350) and (ball.ycor() < paddle_2.ycor() + 60 and ball.ycor() > paddle_2.ycor() - 60):
        ball.setx(330)
        ball.dx = ball.dx + 0.02
        if ball.dy > 0:
            ball.dy = ball.dy + 0.02
        elif ball.dy < 0 :
            ball.dy = ball.dy - 0.02
        ball.dx *= -1
        PlaySound("bounce.wav", SND_ASYNC)

    if (ball.xcor() < -330 and ball.xcor() > -350) and (ball.ycor() < paddle_1.ycor() + 60 and ball.ycor() > paddle_1.ycor() - 60):
        ball.setx(-330)
        ball.dx = ball.dx - 0.02
        if ball.dy > 0:
            ball.dy = ball.dy + 0.02
        elif ball.dy < 0 :
            ball.dy = ball.dy - 0.02
        ball.dx *= -1
        PlaySound("bounce.wav", SND_ASYNC)
