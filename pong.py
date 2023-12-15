import turtle

win = turtle.Screen()
win.title("Pong by @Ottiapraise")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)


#Paddle A
paddle_A = turtle.Turtle()
paddle_A.speed(0)
paddle_A.shape("square")
paddle_A.shapesize(stretch_wid=5, stretch_len=1)
paddle_A.color("white")
paddle_A.penup()
paddle_A.goto(-350, 0)

#Paddle B
paddle_B = turtle.Turtle()
paddle_B.speed(0)
paddle_B.shape("square")
paddle_B.shapesize(stretch_wid=5, stretch_len=1)
paddle_B.color("white")
paddle_B.penup()
paddle_B.goto(+350, 0)


#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)

ball.dx = 2
ball.dy = 2

#Function
def paddle_A_up():
    y=paddle_A.ycor()
    y += 20
    paddle_A.sety(y)

def paddle_A_down():
    y=paddle_A.ycor()
    y -= 20
    paddle_A.sety(y)


def paddle_B_up():
    y = paddle_B.ycor()
    y += 20
    paddle_B.sety(y)


def paddle_B_down():
    y = paddle_B.ycor()
    y -= 20
    paddle_B.sety(y)


#keyboard binding
win.listen()
win.onkeypress(paddle_A_up,"w")
win.onkeypress(paddle_A_down,"s")
win.onkeypress(paddle_B_up,"Up")
win.onkeypress(paddle_B_down,"Down")


#Main game loop
while True:
    win.update()

    #Move the ball
    ball.setx(ball.xcor() = ball.dx)
    ball.sety(ball.ycor() = ball.dy)











