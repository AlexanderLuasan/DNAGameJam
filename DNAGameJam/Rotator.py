
from CollisionObj import CollisionObj
from pygame.math import Vector2
import math

class Rotationpoint(CollisionObj):
    def __init__(self,CollisionRect,movingplatforms):
        CollisionObj.__init__(self,CollisionRect,CollisionRect)
        self.platforms = movingplatforms
        self.vectors = []
        for plat in self.platforms:
            x=self.collisionRect.centerx - plat.getCollision().centerx
            y=self.collisionRect.centery - plat.getCollision().centery
            self.vectors.append(Vector2(x,y))
    def Update(self):
        for i in range(len(self.vectors)):
            self.vectors[i]=self.vectors[i].rotate(1*math.pi/180)
        for i in range(len(self.vectors)):
            polar = self.vectors[i].as_polar()
            x=math.cos(polar[1]) * polar[0]
            y=math.sin(polar[1]) * polar[0]
            self.platforms[i].move(x+self.collisionRect.centerx,y+self.collisionRect.centery)
    def id(self):
        return "rotator"
