from xml.dom import minidom
import pygame
from plat import plat

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
