from CollisionObj import CollisionObj
from pygame import Rect

framespeed = 5
class candy(CollisionObj):
    def __init__(self, CollisionRect):
        CollisionObj.__init__(self,CollisionRect,CollisionRect)
        self.imgnumber=0
        self.frame=0
        self.count=0
    def Update(self):
        if(self.count>framespeed):
            self.frame+=1
        self.count+=1
    def id(self):
        return 4
