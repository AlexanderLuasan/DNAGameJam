
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
        movingplat.append(movingplatform)
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