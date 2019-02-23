from xml.dom import minidom
import pygame

class sprite():
    def __init__ (self, filename):
        myframe = minidom.parse('sprite.tmx')
        animationsets = myframe.getElementsByTagName('objectgroup')

       
        self.parent = pygame.image.load("50365.png")

        self.dictionary = {}
        aninames = []
        for animationset in animationsets:
            n = animationset.attributes['name'].value.split(" ")
            if n[1] not in aninames:
                aninames.append(n[1])
                self.dictionary[n[1]] = dict()
            self.dictionary[n[1]][n[0]] = []
            for animation in animationset.getElementsByTagName("object"):

                x = int(animation.attributes['x'].value)
                y = int(animation.attributes['y'].value)
                w = int(animation.attributes['width'].value)
                h = int(animation.attributes['height'].value)
                self.dictionary[n[1]][n[0]].append(pygame.Rect(x,y,w,h))
        for key in self.dictionary.keys():
            self.dictionary[key]["image"] = []


            for f in self.dictionary[key]["frame"]:
                self.dictionary[key]["image"].append(self.parent.subsurface(f))
            for i in range(len(self.dictionary[key]["frame"])):
                x=self.dictionary[key]["frame"][i].x-self.dictionary[key]["hitbox"][i].x
                y=self.dictionary[key]["frame"][i].y-self.dictionary[key]["hitbox"][i].y
                w=self.dictionary[key]["frame"][i].width
                h=self.dictionary[key]["frame"][i].height
                self.dictionary[key]["frame"][i] = pygame.Rect(x,y,w,h)

        for key in self.dictionary.keys():
            for i in range(len(self.dictionary[key]["image"])):
                self.dictionary[key]["image"][i] = (self.dictionary[key]["image"][i],pygame.transform.flip(self.dictionary[key]["image"][i],True,False))


class backgroundimg():
    def __init__ (self, x, y,filename):
        self.originx = x 
        self.originy = y
        
        self.parent = pygame.image.load(filename)
        self.width = self.parent.get_width()
        self.height = self.parent.get_height()