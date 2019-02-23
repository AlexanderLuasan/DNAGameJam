from CollisionObj import CollisionObj
from pygame import Rect
import random
import time
framespeed = 5
random.seed(time.time())
class candy(CollisionObj):
    def __init__(self, CollisionRect):
        CollisionObj.__init__(self,CollisionRect,CollisionRect)

        self.imgnumber=random.randint(0, 1)
        print(self.imgnumber)
        self.frame=0
        self.count=0
    def Update(self):
        if(self.count>framespeed):
            self.frame+=1
        self.count+=1
    def id(self):
        return 4
