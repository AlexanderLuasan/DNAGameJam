from CollisionObj import CollisionObj

class candy(CollisionObj):
    def __init__(self, CollisionRect):
        CollisionObj.__init__(self,CollisionRect,CollisionRect)
    def id(self):
        return 4
