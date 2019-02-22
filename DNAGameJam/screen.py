
import pygame.draw as d
from pygame import Color
from pygame import Rect
from spritesheet import sprite



imageFile = sprite('sprite.tmx')
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
            if(CollisionObj.index>= len(imageFile.drawbox)):
                CollisionObj.index=0
            h = imageFile.drawbox[CollisionObj.index].h
            w = imageFile.drawbox[CollisionObj.index].w
            x -=  imageFile.drawbox[CollisionObj.index].x
            y -=  imageFile.drawbox[CollisionObj.index].y
            self.drawimg(Rect(x,y,w,h),imageFile.frames[CollisionObj.index])
            #d.rect(self.screen,Color(0, 0, 0, 255),Rect(x,y,w,h),0)
        elif CollisionObj.id() == 1:
            d.rect(self.screen,Color(240, 100, 59, 255),Rect(x,y,w,h),0)
        elif CollisionObj.id() == 2:
            d.rect(self.screen,Color(200, 0, 0, 255),Rect(x,y,w,h),0)
    def flip(self):
        pass
    def drawimg(self,rect,surface):
        self.screen.blit(surface,rect)