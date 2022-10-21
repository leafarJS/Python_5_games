#game pong

import turtle as tr

screen = tr.Screen()
screen.title("Pong by Jorge")
screen.bgcolor("red")
screen.setup(width=800, height=600)
screen.tracer(0)

#player 1
player_1 = tr.Turtle()
player_1.speed(0)
player_1.shape("square")
player_1.color('black')
player_1.shapesize(stretch_wid=5, stretch_len=1)
player_1.penup()
player_1.goto(x=-350, y=0)

#player 1
player_2 = tr.Turtle()
player_2.speed(0)
player_2.shape("square")
player_2.color('black')
player_2.shapesize(stretch_wid=5, stretch_len=1)
player_2.penup()
player_2.goto(x=350, y=0)

#ball 
ball = tr.Turtle()
ball.speed(0)
ball.shape("square")
ball.color('black')
ball.penup()
ball.goto(x=0, y=0)

ball_dx = 0.3
ball_dy = 0.3

#pen
pen = tr.Turtle()
pen.speed()
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 | Player B: 0", aling = "center", font = ("sans-serif", 24, "normal"))


#function 
def player_1_up():
  y = player_1.ycor()
  y += 20
  player_1.sety(y)
  
def player_1_down():
  y = player_1.ycor()
  y -= 20
  player_1.sety(y)
  
def player_2_up():
  y = player_2.ycor()
  y += 20
  player_2.sety(y)
  
def player_2_down():
  y = player_2.ycor()
  y -= 20
  player_2.sety(y)  


#keyborn binding
screen.listen()
screen.onkeypress(player_1_up, "w")
screen.onkeypress(player_1_down, "s")

screen.onkeypress(player_2_up, "Up")
screen.onkeypress(player_2_down, "Down")

# Main game loop
while True:
  screen.update()
  
  #move the ball
  ball.setx(ball.xcor() + ball_dx)
  ball.sety(ball.ycor() + ball_dy)
  
  #border ckeking
  if ball.ycor() > 290:
    ball.sety(290)
    ball_dy *= -0.9
  
  if ball.ycor() < -290:
    ball.sety(-290)
    ball_dy *= -0.9
    
  if ball.xcor() > 390:
    ball.goto(0,0)
    ball_dx *= -0.9
    
  if ball.xcor() < -390:
    ball.goto(0,0)
    ball_dx *= -0.9
    
  #collisions ball y paddle
  if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < player_2.ycor() + 54 and ball.ycor() > player_2.ycor() - 50:
    ball.setx(340)
    ball_dx *= -0.9
    
  if ball.xcor()  < -340 and ball.xcor() > -350 and ball.ycor() < player_1.ycor() + 54 and ball.ycor() > player_1.ycor() - 50:
    ball.setx(-340)
    ball_dx *= -0.9