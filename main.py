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




# Main game loop
while True:
  screen.update()