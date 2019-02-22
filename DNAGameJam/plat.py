from CollisionObj import CollisionObj
from pygame import Rect

class plat(CollisionObj):
    def __init__(self, CollisionRect):
        CollisionObj.__init__(self,CollisionRect,CollisionRect)
    def id(self):
        return "I'm a platform"

class movingplat(plat):
    def __init__(self, CollisionRect):
        plat.__init__(self, CollisionRect)
    def move(self, x, y):
        self.collisionRect.centerx = x
        self.collisionRect.centery = y
