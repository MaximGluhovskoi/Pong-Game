import turtle
import math
import os

wnW = 1000
wnH = 600
cur_pause = False

#setting up screen:

wn = turtle.Screen()
wn.title("Pong Game")
wn.bgcolor("black")
wn.setup(width= wnW, height= wnH)
wn.tracer(0)

# frames count

roundFrames = 1

# scores

score_a = 0
score_b = 0

#SPECS FOR PADDLES AND BALL

paddleWM = 5
originalChange = 3
ballChangeXY = 3
ballChangeX = ballChangeXY
ballChangeY = ballChangeXY

# Paddle A

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(paddleWM,1)
paddle_a.penup()
paddle_a.goto((int)((wnW/-2) + (wnW/15)),0)

# Paddle B

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(paddleWM,1)
paddle_b.penup()
paddle_b.goto((int)((wnW/2) - (wnW/15)),0)

# Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = ballChangeX
ball.dy = ballChangeY

# Pen

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, (int)(wnH/-2)-20)
pen.write("|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n", align="center", font=("Courier", 36, "normal"))
pen.goto(0, (wnH/2) - wnH/10)
pen.write("0      0", align="center", font=("Courier", 36, "normal"))

# Functions

#   paddle a keybind functions

def paddle_a_up():
    if(not cur_pause):
        y = paddle_a.ycor()
        if(y < ((wnH/2)- 12* paddleWM)):
            y += 20
            paddle_a.sety(y)
        elif(y == ((wnH/2)- 12* paddleWM)):
            y += 10
            paddle_a.sety(y)

def paddle_a_down():
    if(not cur_pause):
        y = paddle_a.ycor()
        if(y > (-1 * (wnH/2) + 12 * paddleWM)):
            y -= 20
            paddle_a.sety(y)
        elif(y == (-1 * (wnH/2) + 12 * paddleWM)):
            y -= 10
            paddle_a.sety(y)

#   paddle b keybind functions

def paddle_b_up():
    if(not cur_pause):
        y = paddle_b.ycor()
        if(y < ((wnH/2)- 12* paddleWM)):
            y += 20
            paddle_b.sety(y)
        elif(y == ((wnH/2)- 12* paddleWM)):
            y += 10
            paddle_b.sety(y)

def paddle_b_down():
    if(not cur_pause):
        y = paddle_b.ycor()
        if(y > (-1 * (wnH/2) + 12 * paddleWM)):
            y -= 20
            paddle_b.sety(y)
        elif(y == (-1 * (wnH/2) + 12 * paddleWM)):
            y -= 10
            paddle_b.sety(y)

#   pause game movement functions

def pause_game():
    global ballChangeX
    global ballChangeY
    global cur_pause
    if (cur_pause):
        ball.dx=ballChangeX
        ball.dy=ballChangeY
        pen.clear()
        pen.goto(0, (int)(wnH/-2)-20)
        pen.write("|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n", align="center", font=("Courier", 36, "normal"))
        pen.goto(0, (wnH/2) - wnH/10)
        pen.write("{}      {}".format(score_a, score_b), align="center", font=("Courier", 36, "normal"))
        cur_pause = False
    else:
        ballChangeX = ball.dx
        ballChangeY = ball.dy
        ball.dx = 0
        ball.dy = 0
        pen.goto(0, 0)
        pen.write("PAUSED", align="center", font=("Courier", 52, "normal"))
        cur_pause = True

# Keyboard bindings

wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "\\")
wn.onkeypress(paddle_b_down, "Return")
wn.onkeypress(pause_game, "Escape")

# MAIN GAME LOOP:

while True:
    wn.update()

    # increase ball speed

    roundFrames += 1
    if roundFrames % 50 == 0:
        roundFrames = 1
        ballChangeXY += .1
        ball.dx = (ball.dx/ballChangeX)*ballChangeXY
        ball.dy = (ball.dy/ballChangeY)*ballChangeXY
        ballChangeX = ballChangeXY
        ballChangeY = ballChangeXY

    # Move Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #checking collisions with up and bottom border
    if(abs(ball.ycor() - ((wnH/2)-10)) <= ballChangeXY):
        os.system("afplay wallSound.wav&")
        ball.dy *= -1

    if(abs(ball.ycor() - (wnH/(-2)+10)) <= ballChangeXY):
        os.system("afplay wallSound.wav&")
        ball.dy *= -1

    #checking out of bounds for ball
    if(abs(ball.xcor() - (wnW/(2))) <= 30):
        os.system("afplay scoreSound.wav&")
        ball.setx(0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.goto(0, (int)(wnH/-2)-20)
        pen.write("|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n", align="center", font=("Courier", 36, "normal"))
        pen.goto(0, (wnH/2) - wnH/10)
        pen.write("{}      {}".format(score_a, score_b), align="center", font=("Courier", 36, "normal"))

        roundFrames = 1
        ballChangeXY = originalChange
        ball.dx = (ball.dx/ballChangeX)*ballChangeXY
        ball.dy = (ball.dy/ballChangeY)*ballChangeXY
        ballChangeX = ballChangeXY
        ballChangeY = ballChangeXY

    if(abs(ball.xcor() - (wnW/(-2))) <= 30):
        os.system("afplay scoreSound.wav&")
        ball.setx(0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.goto(0, (int)(wnH/-2)-20)
        pen.write("|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n", align="center", font=("Courier", 36, "normal"))
        pen.goto(0, (wnH/2) - wnH/10)
        pen.write("{}      {}".format(score_a, score_b), align="center", font=("Courier", 36, "normal"))

        roundFrames = 1
        ballChangeXY = originalChange
        ball.dx = (ball.dx/ballChangeX)*ballChangeXY
        ball.dy = (ball.dy/ballChangeY)*ballChangeXY
        ballChangeX = ballChangeXY
        ballChangeY = ballChangeXY

    #checking collision with paddles
    if(abs(ball.xcor() +10 - paddle_b.xcor()) <= ballChangeXY):
        if(abs(paddle_b.ycor() - ball.ycor()) <= paddleWM * 10):
            os.system("afplay paddleSound.wav&")
            ball.dx *= -1
            

    if(abs(ball.xcor() - 10 - paddle_a.xcor()) <= ballChangeXY):
        if(abs(paddle_a.ycor() - ball.ycor()) <= paddleWM * 10):
            os.system("afplay paddleSound.wav&")
            ball.dx *= -1

    