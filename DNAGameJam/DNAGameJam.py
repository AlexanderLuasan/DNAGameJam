import pygame
import screen
import CollisionObj
from player import player
from plat import plat
from plat import movingplat
from pygame import Rect
import levelload
from spritesheet import sprite
from Rotator import Rotationpoint




#sprite.test()
collisionObjlist = levelload.load()


pygame.init()

pf = plat(Rect(0,0,40,40))
mpf = movingplat(Rect(300, 50, 10, 10))
hero = player(Rect(60, 60, 14, 30)) 

rp = Rotationpoint(Rect(300,300,10,10),12,[mpf])


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




# collistionObjlist.append(CollisionObj.CollisionObj(Rect(5, 5, 10, 10), Rect(15, 15, 10, 10)))
# collistionObjlist.append(CollisionObj.CollisionObj(Rect(50, 50, 100, 10), Rect(50, 50, 100, 10)))
# collistionObjlist.append(CollisionObj.CollisionObj(Rect(70, 80, 10, 10), Rect(70, 80, 10, 10)))
# collistionObjlist.append(CollisionObj.CollisionObj(Rect(500, 300, 90, 90), Rect(70, 80, 10, 10)))
# collistionObjlist.append(plat(Rect(350, 300, 60, 60)))
# collistionObjlist.append(plat(Rect(400, 300, 60, 60)))

collisionObjlist.append(mpf)
collisionObjlist.append(pf)
#collisionObjlist.append(hero)
collisionObjlist.append(rp)

for k in range(len(collisionObjlist)):
    print(collisionObjlist[k].id())




cammramovement = [False,False,False,False]

done = False
index = 0

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
            elif(event.key == 273):
                print('upkey')
                hero.setkey(3, True)
            elif(event.key == 276):
                print('leftkey')
                hero.setkey(1, True)
            elif(event.key == 274):
                print('downkey')
                hero.setkey(2, True)
            elif(event.key == 275):
                print('rightkey')
                hero.setkey(0, True)
            elif(event.key == 32):
                hero.setkey(4,True)
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
            elif(event.key == 273):
                print('upkey')
                hero.setkey(3, False)
            elif(event.key == 276):
                print('leftkey')
                hero.setkey(1, False)
            elif(event.key == 274):
                print('downkey')
                hero.setkey(2, False)
            elif(event.key == 275):
                print('rightkey')
                hero.setkey(0, False)
            elif(event.key == 32):
                hero.setkey(4,False)
            else:
                print(event.key)
        else:
            print(event.type)

    shape.x = shape.x+xvel
    shape.y = shape.y+yvel

    rp.Update()
    if(shape.bottom>sheight or shape.top<0):
        yvel = yvel * -1
    if(shape.right>swidth or shape.left<0):
        xvel= xvel * -1;
    hero.Update()


    for i in range(len(collisionObjlist)):
        if(hero.getCollision().colliderect(collisionObjlist[i].getCollision())):
            hero.collide(collisionObjlist[i])


    #cammra movement
    if(cammramovement[0]==True):
        gamescreen.changex(1)
    if(cammramovement[1]==True):
        gamescreen.changex(-1)
    if(cammramovement[2]==True):
        gamescreen.changey(1)
    if(cammramovement[3]==True):
        gamescreen.changey(-1)

    
    if hero.getCollision().right + gamescreen.camx < 0:
        done = True
    if hero.getCollision().left + gamescreen.camx - 600 > 0:
        done = True
    if hero.getCollision().top + gamescreen.camy < 0:
        done = True
    if hero.getCollision().bottom + gamescreen.camy - 400 > 0:
        done = True
    print(gamescreen.camy + sheight, hero.getCollision().top)
    #screen.
    #screen.blit(starimg,shape)
    gamescreen.clear()
    gamescreen.drawRect(shape)
    for i in range(len(collisionObjlist)):
        gamescreen.drawObj(collisionObjlist[i])

    gamescreen.drawObj(hero)
    gamescreen.drawRect(rp.getCollision())
    gamescreen.drawimg(shape,starimg)
    pygame.display.flip()

    timmer.tick(60)

pygame.display.quit()


