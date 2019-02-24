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

        self.frame=random.randint(0,359)
        self.count=0
        self.direction = random.choice([-1,1])
    def Update(self):
        if(self.count>framespeed):
            self.frame+=self.direction
        self.count+=1
    def id(self):
        return 4
