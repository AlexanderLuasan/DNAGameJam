from xml.dom import minidom
import pygame
from plat import plat

class sprite():
    def __init__ (self, filename):
        myframe = minidom.parse('sprite.tmx')
        frame = myframe.getElementsByTagName('objectgroup')
        framebox = frame[0].getElementsByTagName('object')
        hitbox = frame[1].getElementsByTagName('object')
        self.frames = []
        self.hitboxes = []
        self.drawbox = []
        self.parent = pygame.image.load("50365.png")

        for i in range(framebox.length):
            x = framebox[i].attributes['x'].value
            y = framebox[i].attributes['y'].value
            w = framebox[i].attributes['width'].value
            h = framebox[i].attributes['height'].value
            frames.append(plat(pygame.Rect(x,y,w,h)))

        for j in range(hitbox.length):
            x = hitbox[j].attributes['x'].value
            y = hitbox[j].attributes['y'].value
            w = hitbox[j].attributes['width'].value
            h = hitbox[j].attributes['height'].value
            hitboxes.append(pygame.Rect(x,y,w,h))

        for k in range(framebox.length):


        


        
