from CollisionObj import CollisionObj
from pygame import Rect

class candy(CollisionObj):
    def __init__(self, CollisionRect):
        CollisionObj.__init__(self,CollisionRect,CollisionRect)
    def id(self):
        return 4
