
import pygame.draw as d
from pygame import Color
from pygame import Rect
class window():
    def __init__(self,screenSurface):
        self.screen = screenSurface;
        self.camx = 0
        self.camy = 0
    def clear(self):
        self.screen.fill(Color(200,200,200,255))
    def drawRect(self,rect):

        h = rect.height
        w = rect.width
        x = rect.x+self.camx
        y = rect.y+self.camy
        
        d.rect(self.screen,Color(0, 0, 0, 255),Rect(x,y,w,h),0)
    def flip(self):
        pass