
from CollisionObj import CollisionObj
from pygame.math import Vector2
import math
from pygame import Rect

def GCD(a,b):
    if(a==0):
        return b
    else:
        return GCD(b%a,a)


class Rotationpoint(CollisionObj):
    def __init__(self,CollisionRect,periodofrotation,movingplatforms):
        CollisionObj.__init__(self,CollisionRect,CollisionRect)
        self.platforms = movingplatforms
        self.vectors = []

        self.degpc = 360/(periodofrotation*60)
        for plat in self.platforms:
            x=self.collisionRect.centerx - plat.getCollision().centerx
            y=self.collisionRect.centery - plat.getCollision().centery
            self.vectors.append(Vector2(x,y))
    def add(self,movingplatform):
        self.platforms.append(movingplatform)
        x=self.collisionRect.centerx - movingplatform.getCollision().centerx
        y=self.collisionRect.centery - movingplatform.getCollision().centery
        self.vectors.append(Vector2(x,y))
    def Update(self):
        self.count = 0
        for i in range(len(self.vectors)):
            self.vectors[i]=self.vectors[i].rotate(self.degpc*math.pi/180)
        for i in range(len(self.vectors)):
            polar = self.vectors[i].as_polar()
            x=math.cos(polar[1]) * polar[0]
            y=math.sin(polar[1]) * polar[0]
            self.platforms[i].move(x+self.collisionRect.centerx,y+self.collisionRect.centery)
    def id(self):
        return 3

class lineMover(CollisionObj):
    def __init__(self,x1,y1,x2,y2,speed):#direction(x,y)
        CollisionObj.__init__(self,Rect(x1,x1,10,10),Rect(x1,x1,10,10))
        self.speed = speed
        self.point1x=x1
        self.point2x=x2
        self.point1y=y1
        self.slope = (y1-y2)/(x1-x2)
        self.directions = []
        self.platforms = []
    def add(self,movingplatform):
        self.platforms.append(movingplatform)
        self.directions.append(1)
    def Update(self):
        for i in range(len(self.platforms)):
            x=None
            y=100
            if(self.directions[i]>0):
                x = self.platforms[i].collisionRect.centerx + self.directions[i]*self.speed
                if(x>self.point2x):
                    x=self.point2x
                    self.directions[i]=self.directions[i]*-1
            else:
                x = self.platforms[i].collisionRect.centerx + self.directions[i]*self.speed
                if(x<self.point1x):
                    x=self.point1x
                    self.directions[i]=self.directions[i]*-1
            y= -self.slope * (self.point1x-x)+self.point1y
            self.platforms[i].move(x,y)