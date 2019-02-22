
from CollisionObj import CollisionObj



class Rotationpoint(CollisionObj):
    def __init__(self,CollisionRect,movingplatforms):
        self.platforms = movingplatforms
        self.radius = []
        self.angles = []
