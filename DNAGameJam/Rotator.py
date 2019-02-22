
from CollisionObj import CollisionObj
from pygame.math import Vector2


class Rotationpoint(CollisionObj):
    def __init__(self,CollisionRect,movingplatforms):
        self.platforms = movingplatforms
        self.vectors = []
        for plat in self.platforms:
            x=plat.getCollision().centerx
            y=plat.getCollision().centery
            self.vectors.append(x,y)
    
