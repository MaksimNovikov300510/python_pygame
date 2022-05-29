from turtle import *
from time import *

class Sprite(Turtle):
    def __init__(self,x,y,step,color,shape):
        super().__init__()
        self.penup()
        self.speed(0)
        self.goto(x,y)
        self.color(color)
        self.shape(shape)
        self.step = step
    
    def is_collide(self,Sprite):
        dist = self.distance(Sprite.xcor(),Sprite.ycor())
        if dist < 20:
            return True
        else:
            return False
    
    def set_move(self,x_start,y_start,x_end,y_end):
        self.x_start = x_start
        self.y_start = y_start
        self.x_end = x_end  
        self.y_end = y_end
        self.goto(x_start,y_start)
        self.setheading(self.towards(x_end,y_end))
    
    def make_step(self):
        self.forward(self.step)
        if self.distance(self.x_end,self.y_end)<self.step:
            self.set_move(self.x_end,self.y_end,self.x_start,self.y_start)

    def up(self):
        self.goto(self.xcor(), self.ycor() + self.step)
    
    def down(self):
        self.goto(self.xcor(), self.ycor() - self.step)

    def left(self):
        self.goto(self.xcor() + self.step, self.ycor())

    def right(self):
        self.goto(self.xcor()  - self.step, self.ycor())

player = Sprite(0,-150,5,'green','circle')
enemy1 = Sprite(-200,50,10,'red','square')
enemy1.set_move(-200,30,200,30)
enemy2 = Sprite(200,-50,10,'red','square')
enemy2.set_move(200,-30,-200,-30)
enemy3 = Sprite(0, 120, 10,'red','square')

enemy3.set_move(0,-120,0,120)
point = Sprite(0, 150, 10, 'yellow', 'triangle')

scr = player.getscreen()
scr.listen()
scr.onkey(player.up, 'w')
scr.onkey(player.down, 's')
scr.onkey(player.left, 'd')
scr.onkey(player.right, 'a')



score = 0

while score < 3:
    enemy1.make_step()
    enemy2.make_step()
    enemy3.make_step()
    if player.is_collide(point):
        score +=1
        player.goto(0,-100)
    if player.is_collide(enemy1) or player.is_collide(enemy2) or player.is_collide(enemy3):
        point.hideturtle()
        break
enemy1.hideturtle()
enemy2.hideturtle()
enemy3.hideturtle()
