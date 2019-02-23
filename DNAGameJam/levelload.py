from xml.dom import minidom
import pygame
from plat import plat,movingplat
from Rotator import Rotationpoint
from candy import candy


class level():
    def __init__(self,filename):
        mydoc = minidom.parse(filename)
        objectGroups = mydoc.getElementsByTagName('objectgroup')
        self.updaters = []
        self.platforms = []
        for objectGroup in objectGroups:
            if(objectGroup.attributes["name"].value=="Updaters"):
                objects = objectGroup.getElementsByTagName('object')
                for i in range(len(objects)):
                        self.updaters.append(None)
                for obj in objects:
                    
                    if(len(obj.getElementsByTagName("ellipse"))>0):
                        x = int(obj.attributes["x"].value)
                        y = int(obj.attributes["y"].value)
                        w = int(obj.attributes["width"].value)
                        ind = int(obj.attributes["name"].value)
                        sp = 1
                        
                        for p in obj.getElementsByTagName("property"):
                            if(p.attributes["name"].value == "speed"):
                                sp=int(p.attributes["value"].value)
                        self.updaters[ind]=Rotationpoint(pygame.Rect(x+w/2-5,y+w/2-5,10,10),sp,[])
        for objectGroup in objectGroups:
            if(objectGroup.attributes["name"].value=="Platforms"):

                plafroms = objectGroup.getElementsByTagName('object')
                for obj in plafroms:
                    x = int(obj.attributes['x'].value)
                    y = int(obj.attributes['y'].value)
                    w = int(obj.attributes['width'].value)
                    h = int(obj.attributes['height'].value)
                    p=None
                    if(obj.hasAttribute("name")):
                        p = movingplat(pygame.Rect(x,y,w,h))
                        ind = int(obj.attributes["name"].value)
                        self.updaters[ind].add(p)
                    else:
                        p = plat(pygame.Rect(x,y,w,h))
                    self.platforms.append(p)
        for objectGroup in objectGroups:
            if(objectGroup.attributes["name"].value=="Candy"):

                candys = objectGroup.getElementsByTagName('object')
                for obj in candys:
                    x = int(obj.attributes['x'].value)
                    y = int(obj.attributes['y'].value)
                    w = int(obj.attributes['width'].value)
                    h = int(obj.attributes['height'].value)
                    p = candy(pygame.Rect(x,y,w,h))
                    self.platforms.append(p)
        print(len(plafroms))
                    




def load():
    mydoc = minidom.parse('test.tmx')
    platform = mydoc.getElementsByTagName('object')
    length = platform.length
    platlist = []
    for i in range(length):
        x = int(platform[i].attributes['x'].value)
        y = int(platform[i].attributes['y'].value)
        w = int(platform[i].attributes['width'].value)
        h = int(platform[i].attributes['height'].value)
        platlist.append(plat(pygame.Rect(x,y,w,h)))

    return platlist