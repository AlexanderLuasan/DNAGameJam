import pygame
import screen
import CollisionObj
from pygame import Rect
pygame.init()

#jonathan's comment
timmer = pygame.time.Clock()

swidth = 600
sheight = 400
pygame.display.set_mode([swidth,sheight])
gamescreen=screen.window(pygame.display.get_surface())

shape = pygame.Rect(0,0,40,40)
shape.center = (swidth/2,sheight/2)

xvel = 2
yvel = 4

starimg = pygame.image.load("star.jpg")
starimg = pygame.transform.scale(starimg,(40,40))

collistionObjlist = []

collistionObjlist.append(CollisionObj.CollisionObj(Rect(5, 5, 10, 10), Rect(15, 15, 10, 10)))
collistionObjlist.append(CollisionObj.CollisionObj(Rect(50, 50, 100, 10), Rect(50, 50, 100, 10)))
collistionObjlist.append(CollisionObj.CollisionObj(Rect(70, 80, 10, 10), Rect(70, 80, 10, 10)))
collistionObjlist.append(CollisionObj.CollisionObj(Rect(500, 300, 90, 90), Rect(70, 80, 10, 10)))
collistionObjlist.append(CollisionObj.CollisionObj(Rect(250, 200, 50, 50), Rect(70, 80, 10, 10)))
collistionObjlist.append(CollisionObj.CollisionObj(Rect(90, 90, 5, 5), Rect(70, 80, 10, 10)))
collistionObjlist.append(CollisionObj.CollisionObj(Rect(300, 300, 60, 60), Rect(70, 80, 10, 10)))





done = False
while(not done):
    for event in pygame.event.get():
        if (event.type == 12):
            done = True
        else:
            print(event.type)

    shape.x = shape.x+xvel
    shape.y = shape.y+yvel


    if(shape.bottom>sheight or shape.top<0):
        yvel = yvel * -1
    if(shape.right>swidth or shape.left<0):
        xvel= xvel * -1;

    #screen.
    #screen.blit(starimg,shape)
    gamescreen.clear()
    gamescreen.drawRect(shape)
    gamescreen.drawRect(collistionObjlist[0].getCollision())
    gamescreen.drawRect(collistionObjlist[1].getCollision())
    gamescreen.drawRect(collistionObjlist[2].getCollision())
    gamescreen.drawRect(collistionObjlist[3].getCollision())
    gamescreen.drawRect(collistionObjlist[4].getCollision())
    gamescreen.drawRect(collistionObjlist[5].getCollision())


    pygame.display.flip()

    timmer.tick(60)

pygame.display.quit()


