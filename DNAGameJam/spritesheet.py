from xml.dom import minidom
import pygame

candysize = 40
spritescale = 1
class collections:
    def __init__ (self,imgfiles):
        self.images = []
        for i in range(len(imgfiles)):
            self.images.append(pygame.image.load(imgfiles[i]))
        for i in range(len(self.images)):
            self.images[i] = pygame.transform.scale(self.images[i],(candysize,candysize))
        for i in range(len(self.images)):
            self.images[i].set_colorkey(self.images[i].get_at((0,0)))
        for i in range(len(self.images)):
            orig = self.images[i]
            self.images[i]=[]
            for j in range(360):
                self.images[i].append(pygame.transform.rotate(orig, j))

class sprite():
    def __init__ (self, filename):
        myframe = minidom.parse('resource/newsprite.tmx')
        animationsets = myframe.getElementsByTagName('objectgroup')

       
        self.parent = pygame.image.load("resource/new_sprite.png")
        
        #clearcolor
        for x in range(self.parent.get_width()):
            for y in range(self.parent.get_height()):
                c = self.parent.get_at((x,y))
                if(c.a+c.b+c.g>253*3):
                    self.parent.set_at((x,y),pygame.Color(0,0,0,0))

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
            #for f in range(len(self.dictionary[key]["frame"])):#divide 2
                #w = self.dictionary[key]["image"][f].get_width()
                #h = self.dictionary[key]["image"][f].get_height()
                #self.dictionary[key]["image"][f] = pygame.transform.scale(self.dictionary[key]["image"][f],(int(w/spritescale),int(h/spritescale)))
                
            for i in range(len(self.dictionary[key]["frame"])):
                x=(self.dictionary[key]["frame"][i].x-self.dictionary[key]["hitbox"][i].x)/spritescale
                y=(self.dictionary[key]["frame"][i].y-self.dictionary[key]["hitbox"][i].y)/spritescale
                w=self.dictionary[key]["frame"][i].width/spritescale
                h=self.dictionary[key]["frame"][i].height/spritescale
                self.dictionary[key]["frame"][i] = pygame.Rect(int(x),int(y),int(w),int(h))

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