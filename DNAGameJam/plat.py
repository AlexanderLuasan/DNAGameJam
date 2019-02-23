from CollisionObj import CollisionObj
from pygame import Rect

class plat(CollisionObj):
    def __init__(self, CollisionRect):
        CollisionObj.__init__(self,CollisionRect,CollisionRect)
    def id(self):
        return 1

class movingplat(plat):
    def __init__(self, CollisionRect):
        plat.__init__(self, CollisionRect)
    def move(self, x, y):

        if(self.stander != None):
            self.stander.collisionRect.x += self.collisionRect.centerx - x
        
        self.collisionRect.centerx = x
        self.collisionRect.centery = y
    def id(self):
        return 2
