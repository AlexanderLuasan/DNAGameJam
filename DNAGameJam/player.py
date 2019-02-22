from CollisionObj import CollisionObj


class player(CollisionObj):
    def __init__(self,CollisionRect):
       CollisionObj.__init__(self,CollisionRect,CollisionRect)
       self.velx = 0
       self.vely = 0
       self.keys = [False,False,False,False]
    def setkey(self,index,value):
       self.keys[index]=value
    def Update(self):
        if(self.keys[0]==True):#speed control
            self.velx+=1
        if(self.keys[1]==True):
            self.velx-=1
        if(self.velx>10):
            velx=10
        if(self.velx<-10):
            velx=-10
        if(self.keys[2]==True):
            self.vely+=1
        if(self.keys[3]==True):
            self.vely-=1
        if(self.vely>10):
            vely=10
        if(self.vely<-10):
            vely=-10
        #move collision box
        self.collisionRect.x=self.collisionRect.x+self.velx
        self.collisionRect.y=self.collisionRect.y+self.vely
    def id(self):
        return "i'm player"

