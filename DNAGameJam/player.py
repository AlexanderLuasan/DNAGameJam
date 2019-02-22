from CollisionObj import CollisionObj
maxspeed = 3

class player(CollisionObj):
    def __init__(self,CollisionRect):
       CollisionObj.__init__(self,CollisionRect,CollisionRect)
       self.velx = 0
       self.vely = 0
       self.keys = [False,False,False,False]#left right up down
    def setkey(self,index,value):
       self.keys[index]=value
    def Update(self):
        if(self.keys[0]==True):#speed control
            self.velx+=1
        if(self.keys[1]==True):
            self.velx-=1
        if(self.velx>maxspeed):
            self.velx-=1;
        if(self.velx<-maxspeed):
            velx=-maxspeed
        if(self.keys[2]==True):
            self.vely+=1
        if(self.keys[3]==True):
            self.vely-=1
        if(self.vely>maxspeed):
            vely=maxspeed
        if(self.vely<-maxspeed):
            vely=-10
        
        if(self.keys[0]==False and self.keys[1]==False):
            self.velx-=0.1
            if(self.velx<0):
                self.velx=0;
        if(self.keys[1]==False and self.keys[0]==False):
            self.velx+=0.1
            if(self.velx>0):
                self.velx=0;
        if(self.keys[2]==False and self.keys[3]==False):
            self.vely-=0.1
            if(self.vely<0):
                self.vely=0;
        if(self.keys[3]==False and self.keys[2]==False):
            self.vely+=0.1
            if(self.vely>0):
                self.vely=0;
        
        #move collision box
        self.collisionRect.x=self.collisionRect.x+self.velx
        self.collisionRect.y=self.collisionRect.y+self.vely
    def id(self):
        return "i'm player"

