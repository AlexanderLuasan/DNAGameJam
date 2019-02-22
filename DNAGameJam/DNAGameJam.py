import pygame
import screen
import CollisionObj
from player import player
from plat import plat
from pygame import Rect
import levelload

levelload.go()
collistionObjlist = levelload.load()

pygame.init()

pf = plat(Rect(0,0,40,40))


hero = player(Rect(60, 60, 30, 30)) 


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

for k in range(len(collistionObjlist)):
    print(collistionObjlist[k].id())




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
            else:
                print(event.key)
        else:
            print(event.type)

    shape.x = shape.x+xvel
    shape.y = shape.y+yvel


    if(shape.bottom>sheight or shape.top<0):
        yvel = yvel * -1
    if(shape.right>swidth or shape.left<0):
        xvel= xvel * -1;
    hero.Update()


    for i in range(len(collistionObjlist)):
        if(hero.getCollision().colliderect(collistionObjlist[i].getCollision())):
            hero.collide(collistionObjlist[i])


    #cammra movement
    if(cammramovement[0]==True):
        gamescreen.changex(1)
    if(cammramovement[1]==True):
        gamescreen.changex(-1)
    if(cammramovement[2]==True):
        gamescreen.changey(1)
    if(cammramovement[3]==True):
        gamescreen.changey(-1)

    
    print(gamescreen.camx, gamescreen.camy, hero.collisionRect.left, hero.collisionRect.top)
    

    #screen.
    #screen.blit(starimg,shape)
    gamescreen.clear()
    gamescreen.drawRect(shape)
    for i in range(len(collistionObjlist)):
        gamescreen.drawRect(collistionObjlist[i].getCollision())

    gamescreen.drawRect(hero.getCollision())

    if hero.collisionRect.right + gamescreen.camx < 0:
        print("out of screen left")
        done = True
    elif hero.collisionRect.top + gamescreen.camy +  hero.collisionRect.height < 0:
        print("out ouf screen up")
        done = True
    elif hero.collisionRect.left + gamescreen.camx > swidth:
        print("out of screen right")
        done = True
    elif hero.collisionRect.top + gamescreen.camy > sheight:
        print("out of screen down")
        done = True

    pygame.display.flip()

    timmer.tick(60)

pygame.display.quit()


