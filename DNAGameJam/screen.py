
import pygame.draw as d
from pygame import Color
from pygame import Rect
from spritesheet import sprite,collections



imageFile = sprite('sprite.tmx')
thingpicup = collections(["bluecandy.png"])

class window():
    def __init__(self,screenSurface):
        self.screen = screenSurface;
        self.camx = 0
        self.camy = 0
    def clear(self):
        self.screen.fill(Color(200,200,200,255))
    def changex(self,v):
        self.camx+=v
    def changey(self,v):
        self.camy+=v
    def drawRect(self,rect):

        h = rect.height
        w = rect.width
        x = rect.x+self.camx
        y = rect.y+self.camy
        
        d.rect(self.screen,Color(0, 0, 0, 255),Rect(x,y,w,h),0)
    def drawObj(self, CollisionObj):
        h = CollisionObj.getCollision().h
        w = CollisionObj.getCollision().w
        x = CollisionObj.getCollision().x+self.camx
        y = CollisionObj.getCollision().y+self.camy
        if CollisionObj.id() == 0:


            animationname = "idle"
            right = CollisionObj.right

            if(CollisionObj.velx!=0):
                if(CollisionObj.velx>0):
                    right = 0
                else:
                    right = 1
                animationname = "Walking"

            if(not CollisionObj.onground):
                animationname = "jump"

            if(CollisionObj.index>= len(imageFile.dictionary[animationname]["frame"])):
                CollisionObj.index=0

            h = imageFile.dictionary[animationname]["frame"][CollisionObj.index].h
            w = imageFile.dictionary[animationname]["frame"][CollisionObj.index].w
            x += imageFile.dictionary[animationname]["frame"][CollisionObj.index].x
            y += imageFile.dictionary[animationname]["frame"][CollisionObj.index].y
            self.drawimg(Rect(x,y,w,h),imageFile.dictionary[animationname]["image"][CollisionObj.index][right])

            #d.rect(self.screen,Color(0, 0, 0, 255),Rect(x,y,w,h),0)
        elif CollisionObj.id() == 1:
            d.rect(self.screen,Color(0, 122, 14, 255),Rect(x,y,w,h),0)
        elif CollisionObj.id() == 2:
            d.rect(self.screen,Color(240, 100, 59, 255),Rect(x,y,w,h),0)
        elif CollisionObj.id() == 3:
            for i in CollisionObj.platforms:
                d.rect(self.screen,Color(160, 160, 160, 255),Rect(x,y,w,h),0)
                d.line(self.screen,Color(160, 160, 160, 255), (i.getCollision().center), (CollisionObj.getCollision().centerx,CollisionObj.getCollision().centery), 1)
        elif CollisionObj.id() == 4:
            imgnum = CollisionObj.imgnumber
            if(CollisionObj.frame>=len(thingpicup.images[imgnum])):
                CollisionObj.frame=0

            im = thingpicup.images[0][CollisionObj.frame]
            r = im.get_rect()
            r.center = CollisionObj.getCollision().center
            d.rect(self.screen,Color(66, 220, 224, 255),Rect(x,y,w,h),0)
            self.drawimg(r,im)

            
    def flip(self):
        pass
    def drawimg(self,rect,surface):
        self.screen.blit(surface,rect)
    def drawbackground(self,backgroundclass):
        loopoffsetx = -self.camx%backgroundclass.width
        loopoffsety = -self.camy%backgroundclass.height
        startx = 0
        starty = 0
        screenwidth = self.screen.get_width()
        screenheight= self.screen.get_height()
        self.screen.blit(backgroundclass.parent,Rect(startx,starty,100,100),area = Rect(loopoffsetx,loopoffsety,screenwidth,screenheight))
        if(loopoffsetx+screenwidth>backgroundclass.width):
            neededx = (loopoffsetx+screenwidth)-backgroundclass.width
            self.screen.blit(backgroundclass.parent,Rect(startx+screenwidth-neededx,starty,100,100),area = Rect(0,loopoffsety,neededx,screenheight))
        if(loopoffsety+screenheight>backgroundclass.height):
            neededy = (loopoffsety+screenheight)-backgroundclass.height
            self.screen.blit(backgroundclass.parent,Rect(startx,starty+screenheight-neededy,100,100),area = Rect(loopoffsetx,0,screenwidth,neededy))
        if(loopoffsetx+screenwidth>backgroundclass.width):
            if(loopoffsety+screenheight>backgroundclass.height):
                neededx = (loopoffsetx+screenwidth)-backgroundclass.width      
                neededy = (loopoffsety+screenheight)-backgroundclass.height
                self.screen.blit(backgroundclass.parent,Rect(startx+screenwidth-neededx,starty+screenheight-neededy,100,100),area = Rect(0,0,neededx,neededy))