from CollisionObj import CollisionObj
maxspeed = 3
gravity = 0.2


class player(CollisionObj):
    def __init__(self,CollisionRect):
       CollisionObj.__init__(self,CollisionRect,CollisionRect)
       self.velx = 0
       self.vely = 0
       self.onground=False
       self.keys = [False,False,False,False,False]#left right up down
    def setkey(self,index,value):
        if(index==4 and value == True):
            if(self.onground):
                self.jump()
        self.keys[index]=value
    def jump(self):
        self.onground=False
        self.vely=-10
    def Update(self):
        if(self.keys[0]==True):#speed control
            self.velx+=1
        if(self.keys[1]==True):
            self.velx-=1
        if(self.velx>maxspeed):
            self.velx=maxspeed
        if(self.velx<-maxspeed):
            self.velx=-maxspeed
        #gravity
        if(self.keys[4]==True):
            self.vely+=gravity/2
        else:
            self.vely+=gravity
        #if(self.keys[2]==True):
        #    self.vely+=1
        #if(self.keys[3]==True):
        #    self.vely-=1
        if(self.vely>maxspeed):
            self.vely=maxspeed
        if(self.vely<-maxspeed):
            self.vely=-maxspeed
        
        if(self.keys[0]==False and self.keys[1]==False):
            self.velx-=0.1
            if(self.velx<0):
                self.velx=0
        if(self.keys[1]==False and self.keys[0]==False):
            self.velx+=0.1
            if(self.velx>0):
                self.velx=0
        #if(self.keys[2]==False and self.keys[3]==False):
        #    self.vely-=0.1
        #    if(self.vely<0):
        #        self.vely=0
        #if(self.keys[3]==False and self.keys[2]==False):
        #    self.vely+=0.1
        #    if(self.vely>0):
        #        self.vely=0
        #move collision box
        self.collisionRect.x=self.collisionRect.x+self.velx
        self.collisionRect.y=self.collisionRect.y+self.vely
    def id(self):
        return 0
    def collide(self,other):
        
        self.collisionRect.x=self.collisionRect.x-self.velx
        self.collisionRect.y=self.collisionRect.y-self.vely


        self.collisionRect.x=self.collisionRect.x+self.velx
        if(self.collisionRect.colliderect(other.getCollision())):
            if(self.velx>0):
                self.collisionRect.right = other.getCollision().left
            elif(self.velx<0):
                self.collisionRect.left = other.getCollision().right
        
        self.collisionRect.y=self.collisionRect.y+self.vely
        if(self.collisionRect.colliderect(other.getCollision())):
            if(self.vely>0):
                self.collisionRect.bottom = other.getCollision().top
                self.onground=True
            elif(self.vely<0):
                self.collisionRect.top = other.getCollision().bottom

        

        

