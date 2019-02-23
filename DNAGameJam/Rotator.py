
from CollisionObj import CollisionObj
from pygame.math import Vector2
import math

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
    def __init__(self,CollisionRect,speed,direction,movingplatforms):#direction(x,y)
        CollisionObj.__init__(self,CollisionRect,CollisionRect)
        self.speed = speed
        self.point1x
        self.point2x
        self.point1y
        self.point2y
        self.platforms = movingplatforms
        self.directions = []
        for p in self.platfroms:
            self.directions.append(direction)
    def add(self,direction,movingplatform):
        self.platforms.append(movingplatform)
        self.directions.append(direction)
    def Update(self):
        for i in range(len(self.plaforms)):
            x=None
            y=None
            if(self.directions[i][0]>0):
                x = self.platforms[i].collisionRect.centerx + self.directions[i][0]*speed
                if(x>self.point2x):
                    x=self.point2x
                    self.directions[i][0]*-1
            else:
                x = self.platforms[i].collisionRect.centerx + self.directions[i][0]*speed
                if(x<self.point1x):
                    x=self.point1x
                    self.directions[i][0]*-1

            if(self.directions[i][1]>0):
                y = self.platforms[i].collisionRect.centerx + self.directions[i][1]*speed
                if(y>self.point2y):
                    y=self.point2y
                    self.directions[i][1]*-1
            else:
                y = self.platforms[i].collisionRect.centerx + self.directions[i][1]*speed
                if(y<self.point1y):
                    y=self.point1y
                    self.directions[i][1]*-1
            self.platforms[i].move(x,y)