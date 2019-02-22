from CollisionObj import CollisionObj

class plat(CollisionObj):
    def __init__(self, CollisionRect):
        CollisionObj.__init__(self,CollisionRect,CollisionRect)
