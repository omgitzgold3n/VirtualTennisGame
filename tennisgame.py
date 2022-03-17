#Chris Golden
#HW13
#4/27/21

#A

'''
Purpose: Sets the variables and conditions that simulate gravity and the projectile motion
of the ball by using turtle.
Instance variables: self.x is the x position of the ball; self.y is the y position of the ball; the bounce variable keeps track of the bounces in the game to reference when the ball needs to reset.
self.vx is the x velocity of the ball and self.vy is the y velocity of the ball which these
will have an integer value when calling the function through terminal.
Methods: Ball class: 1. The init method creates the ball and the coordinates for the ball. 2. The move method moves the ball in the game. 3. The hit method hits the Ball
when space is pressed. 4. The reset method is used to reset the ball. I also made two other hit methods for different strengths of the hit.
Game class: 1. The init method creates the playing field, net, background and text shown during the game as well as the boundries. 2. The gameloop method loops the game
over and over until either the ball resets or the game is over.
'''
'''
The first change I chose for part D was option 5 which are soft and hard hits where I press 'h' for a hard
hit and 's' for a soft hit. I also added option 8 where I added a sun image in the background as well as a title
saying we are on the sun for the setting of my tennis match which looks pretty cool.
My third thing I chose was option1 which is a change in the angle of hitting the ball which changed the y
velocity from 15 after a hit to 10 to get a more striaght angled hit.
'''
import turtle
import math
import random

class Ball(turtle.Turtle):

    def __init__(self, x, y, vx, vy):

        turtle.Turtle.__init__(self)
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.shape('circle')
        self.turtlesize(0.3)
        self.penup()
        self.setpos(self.x,self.y)
        self.bounce = 0

    def move(self):

        #adding air friction to the y velocity as the ball falls

        self.vy = self.vy - 0.981

        self.x = self.xcor() + self.vx
        self.y = self.ycor() + self.vy
        #Creating the net reset

        if self.x == 0 and self.y <30:
            self.reset()
        #Creating the double bounce reset
        if abs(self.x) < 5:
            self.bounce = 0
        if self.y <= 0:
            self.y = (self.y * 0.75)
            self.vy *= -0.75
            self.bounce += 1
            if self.bounce == 2 and self.x > 0:
                self.reset()
            if self.bounce ==2 and self.x < 0:
                self.reset()
        else:
            self.y = self.ycor() + self.vy
        self.setpos(self.x,self.y)


    def hit(self):#regular hit

        self.vx = self.vx * -1
        self.vy = 15

    def hit2(self):#hard hit

        self.vx = self.vx * -1.5
        self.vy = 15

    def hit3(self):#soft hit

        self.vx = self.vx * -0.5
        self.vy = 15

    def hit4(self):#option1 - change in angle of hit to be more angled straight
        self.vx = self.vx * -1
        self.vy = 10


    def reset(self):

        self.x = random.uniform(-100,100)
        self.y = random.uniform(30,100)
        #making a list for the randomized velocities
        xnum1 = random.uniform(-12,-6)
        xnum2 = random.uniform(6,12)
        xrandomlist = [xnum1,xnum2]
        self.vx = random.choice(xrandomlist)
        self.vy = random.uniform(4,10)
        self.setpos(self.x,self.y)




class Game(turtle.Turtle):
    def __init__(self):


        turtle.delay()
        turtle.tracer(0,0)
        turtle.setworldcoordinates(-500, -500, 500, 500)
        #Creating the net and court, and background
        screen = turtle.Screen()
        screen.bgpic('sungif.gif')
        #Adding background text/title
        style = ('Courier', 30, 'italic')
        turtle.write("WE ON THE SUN", font=style)
        turtle.forward(400)
        turtle.left(180)
        turtle.forward(800)
        turtle.left(180)
        turtle.forward(400)
        turtle.left(90)
        turtle.forward(30)
        turtle.hideturtle()

        self.x = random.uniform(-100,100)
        self.y = random.uniform(30,100)
        #making a list for the randomized velocities
        xnum1 = random.uniform(-12,-6)
        xnum2 = random.uniform(6,12)
        xrandomlist = [xnum1,xnum2]
        self.vx = random.choice(xrandomlist)
        self.vy = random.uniform(4,10)
        self.ball = Ball(self.x, self.y, self.vx, self.vy)
        turtle.update()
        self.ball.move()
        turtle.onkeypress(self.ball.hit, 'space')#regular hit
        turtle.onkeypress(self.ball.hit2, 'h')#hard hit
        turtle.onkeypress(self.ball.hit3, 's')#soft hit
        turtle.onkeypress(self.ball.hit4, 'v')#change in angled hit
        turtle.listen()
        self.gameloop()
        turtle.update()
        turtle.mainloop()


    def gameloop(self):


        self.ball.move()
        turtle.update()
        turtle.ontimer(self.gameloop, 30)



if __name__ == '__main__':
    g = Game()
