
class CollisionObj():
    def __init__ (self,collisionRect,DrawingRect):
        self.collisionRect = collisionRect
        self.DrawingRect = DrawingRect
    def Update(self):
        pass
    def getCollision(self):
        return self.collisionRect
    def getDrawing(self):
        return self.DrawingRect
    def collide(self,otherObj):
        pass
    def preDraw():
        pass