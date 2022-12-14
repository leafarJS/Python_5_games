#game pong

import turtle as tr
import winsound 

screen = tr.Screen()
screen.title("Pong by Jorge")
screen.bgcolor("red")
screen.setup(width=800, height=600)
screen.tracer(0)

#Score 
score_1 = 0
score_2 = 0




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
ball_dy = -0.3

#pen
pen = tr.Turtle()
pen.speed()
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,260)



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
    #sound
    #winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
  
  if ball.ycor() < -290:
    ball.sety(-290)
    ball_dy *= -0.9
    #winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    
  if ball.xcor() > 390:
    ball.goto(0,0)
    ball_dx *= -0.9
    score_1 += 1
    pen.clear()
    pen.write(f"Player A: {score_1} | Player B: {score_2}", align = "center", font = ("Courier", 24, "bold"))
    
  if ball.xcor() < -390:
    ball.goto(0,0)
    ball_dx *= -0.9
    score_2 += 1
    pen.clear()
    pen.write(f"Player A: {score_1} | Player B: {score_2}", align = "center", font = ("Courier", 24, "bold"))
    
  #collisions ball y paddle
  if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < player_2.ycor() + 54 and ball.ycor() > player_2.ycor() - 50:
    ball.setx(340)
    ball_dx *= -0.9
    #winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    
  if ball.xcor()  < -340 and ball.xcor() > -350 and ball.ycor() < player_1.ycor() + 54 and ball.ycor() > player_1.ycor() - 50:
    ball.setx(-340)
    ball_dx *= -0.9
    #winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)