
import pygame.draw as d
from pygame import Color
class window():
    def __init__(self,screenSurface):
        self.screen = screenSurface;
        self.camx = 0
        self.camy = 0
    def drawRect(self,rect):
        self.screen.fill(Color(200,200,200,255))
        d.rect(self.screen,Color(0, 0, 255, 255),rect,0)
    def flip(self):
        pass