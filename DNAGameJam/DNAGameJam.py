import pygame
import screen
import CollisionObj
from player import player
from plat import plat
from pygame import Rect
import levelload

levelload.go()

pygame.init()

pf = plat(Rect(0,0,40,40))


hero = player(Rect(60, 60, 50, 75)) 
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




cammramovement = [False,False,False,False]

done = False
while(not done):
    for event in pygame.event.get():
        if (event.type == 12):
            done = True
        elif(event.type == 2):
            if(event.key==119):
                print('w')
                cammramovement[2]=True
            elif(event.key == 97):
                print('a')
                cammramovement[0]=True
            elif(event.key == 115):
                print('s')
                cammramovement[3]=True
            elif(event.key == 100):
                print('d')
                cammramovement[1]=True
            else:
                print(event.key)
        elif(event.type == 3):
            if(event.key==119):
                print('w')
                cammramovement[2]=False
            elif(event.key == 97):
                print('a')
                cammramovement[0]=False
            elif(event.key == 115):
                print('s')
                cammramovement[3]=False
            elif(event.key == 100):
                print('d')
                cammramovement[1]=False
            else:
                print(event.key)
        else:
            print(event.type)

    shape.x = shape.x+xvel
    shape.y = shape.y+yvel


    #cammra movement
    if(cammramovement[0]==True):
        gamescreen.changex(1)
    if(cammramovement[1]==True):
        gamescreen.changex(-1)
    if(cammramovement[2]==True):
        gamescreen.changey(1)
    if(cammramovement[3]==True):
        gamescreen.changex(-1)

    if(shape.bottom>sheight or shape.top<0):
        yvel = yvel * -1
    if(shape.right>swidth or shape.left<0):
        xvel= xvel * -1;

    #screen.
    #screen.blit(starimg,shape)
    gamescreen.clear()
    gamescreen.drawRect(shape)
    for i in range(len(collistionObjlist)):
        gamescreen.drawRect(collistionObjlist[i].getCollision())

    gamescreen.drawRect(hero.getCollision())

    pygame.display.flip()

    timmer.tick(60)

pygame.display.quit()


