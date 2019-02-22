from xml.dom import minidom
import pygame

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
            x = int(framebox[i].attributes['x'].value)
            y = int(framebox[i].attributes['y'].value)
            w = int(framebox[i].attributes['width'].value)
            h = int(framebox[i].attributes['height'].value)
            self.drawbox.append(pygame.Rect(x,y,w,h))

        for j in range(hitbox.length):
            x = int(hitbox[j].attributes['x'].value)
            y = int(hitbox[j].attributes['y'].value)
            w = int(hitbox[j].attributes['width'].value)
            h = int(hitbox[j].attributes['height'].value)
            self.hitboxes.append(pygame.Rect(x,y,w,h))

        for k in range(framebox.length):
            self.frames.append(self.parent.subsurface(self.drawbox[k]))
        for i in range(framebox.length):
            x=self.hitboxes[i].x-self.drawbox[i].x
            y=self.hitboxes[i].y-self.drawbox[i].y
            w=self.drawbox[i].width
            h=self.drawbox[i].height
            self.drawbox[i] = pygame.Rect(x,y,w,h)

        


        
