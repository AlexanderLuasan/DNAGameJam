
from CollisionObj import CollisionObj
from pygame.math import Vector2
import math

class Rotationpoint(CollisionObj):
    def __init__(self,CollisionRect,movingplatforms):
        self.platforms = movingplatforms
        self.vectors = []
        for plat in self.platforms:
            x=plat.getCollision().centerx
            y=plat.getCollision().centery
            self.vectors.append(x,y)
    def Update(self):
        for i in range(len(self.vectors)):
            self.vectors[i].rotate(1)
        for i in range(len(self.vectors)):
            polar = self.vectors[i].as_polar()
            x=math.cos(polar[1]) * polar[0]
            y=math.sin(polar[1]) * polar[1]
            self.platforms[i].move(x,y)
