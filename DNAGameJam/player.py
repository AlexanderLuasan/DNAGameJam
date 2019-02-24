from CollisionObj import CollisionObj
maxspeedy = 4.5
maxspeedx = 3
speedx = 3
gravity = 0.5
gravityspeed = 2
countindexvar = 0.5
framespeed = 1

class player(CollisionObj):
    def __init__(self,CollisionRect):
       CollisionObj.__init__(self,CollisionRect,CollisionRect)
       self.velx = 0
       self.index = 0
       self.vely = 0
       self.onground=False
       self.right = 0
       self.keys = [False,False,False,False,False]#left right up down
       self.countindex = 0
       self.score = 0
    def setkey(self,index,value):
        if(index==4 and value == True):
            if(self.onground):
                self.jump()
        elif(index == 0 and value == True):
            self.right = 0
        elif(index == 1 and value == True):
            self.right = 1
        self.keys[index]=value
    def jump(self):
        self.onground=False
        self.vely=-5
    def Update(self):
        self.countindex += countindexvar
        if(self.countindex==framespeed):
            self.index+=1
            self.countindex = 0
        if(self.keys[0]==True):#speed control
            self.velx+=speedx
        if(self.keys[1]==True):
            self.velx-=speedx
        if(self.velx>maxspeedx):
            self.velx=maxspeedx
        if(self.velx<-maxspeedx):
            self.velx=-maxspeedx
        #gravity

        if(self.keys[4]==True):
            self.vely+=gravity/gravityspeed
        else:
            self.vely+=gravity
        #if(self.keys[2]==True):
        #    self.vely+=1
        #if(self.keys[3]==True):
        #    self.vely-=1
        if(self.vely>maxspeedy):
            self.vely=maxspeedy
        if(self.vely<-maxspeedy):
            self.vely=-maxspeedy
        
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

        if (other.id() == 2):
            if(other.colide == False):
                #self.collisionRect.y=self.collisionRect.y+self.vely
                self.collisionRect.x=self.collisionRect.x+self.velx
                return
        if (other.id() == 4):
            self.score += 1
            other.collisionRect.x = -50
            other.collisionRect.y = -50
            print(self.score)
        self.collisionRect.y=self.collisionRect.y+self.vely
        if(self.collisionRect.colliderect(other.getCollision())):
            if(self.vely>0):
                self.collisionRect.bottom = other.getCollision().top
                self.onground = True
            elif(self.vely<0):
                self.collisionRect.top = other.getCollision().bottom
                


        self.collisionRect.x=self.collisionRect.x+self.velx
        if(self.collisionRect.colliderect(other.getCollision())):
            if(self.velx>0):
                self.collisionRect.right = other.getCollision().left
                self.velx=0
            elif(self.velx<0):
                self.collisionRect.left = other.getCollision().right
                self.velx=0
       

        

        

