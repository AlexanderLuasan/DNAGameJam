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
        self.stander=None
        self.colide = False
    def move(self, x, y):
        
        if(y-self.collisionRect.centery>0):#go down
            self.colide = False
        else:
            self.colide = True
        if(self.stander != None):
            if self.collisionRect.top == self.stander.collisionRect.bottom:
                self.stander.collisionRect.x += x-self.collisionRect.centerx
                self.stander.collisionRect.y += y-self.collisionRect.centery
            else:
                self.stander = None
        
        self.collisionRect.centerx = x
        self.collisionRect.centery = y
    def id(self):
        return 2
    def collide(self,OtherObj):
        self.stander = OtherObj
        

