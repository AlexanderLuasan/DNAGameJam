import pygame
import screen
import CollisionObj
from player import player
from plat import plat
from plat import movingplat
from pygame import Rect
import levelload
from spritesheet import sprite, backgroundimg
from Rotator import Rotationpoint
from candy import candy
from Rotator import lineMover


testcandy = candy(Rect(50, 50, 20, 20))

#print(testcandy.id())


#sprite.test()


gamestate = levelload.level("newmap.tmx")


pygame.init()

hero = player(Rect(0,0,14,30))
#jonathan's comment
timmer = pygame.time.Clock()

swidth = 800
sheight = 500
pygame.display.set_mode([swidth,sheight])
gamescreen=screen.window(pygame.display.get_surface())

shape = pygame.Rect(0,0,40,40)
shape.center = (swidth/2,sheight/2)

xvel = 2
yvel = 4

starimg = pygame.image.load("star.jpg")
starimg = pygame.transform.scale(starimg,(40,40))


back = backgroundimg(0,0,"background.jpg")


cammramovement = [False,False,False,False]

done = False
index = 0

while(not done):
    for event in pygame.event.get():
        if (event.type == 12):
            done = True
        elif(event.type == 2):
            if(event.key==119):
                #print('w')
                cammramovement[2]=True
            elif(event.key == 97):
                #print('a')
                cammramovement[0]=True
            elif(event.key == 115):
                #print('s')
                cammramovement[3]=True
            elif(event.key == 100):
                #print('d')
                cammramovement[1]=True
            elif(event.key == 273):
                #print('upkey')
                hero.setkey(3, True)
            elif(event.key == 276):
                #print('leftkey')
                hero.setkey(1, True)
            elif(event.key == 274):
                #print('downkey')
                hero.setkey(2, True)
            elif(event.key == 275):
                #print('rightkey')
                hero.setkey(0, True)
            elif(event.key == 32):
                hero.setkey(4,True)
            else:
                pass
                #print(event.key)
        elif(event.type == 3):
            if(event.key==119):
                #print('w')
                cammramovement[2]=False
            elif(event.key == 97):
                #print('a')
                cammramovement[0]=False
            elif(event.key == 115):
                #print('s')
                cammramovement[3]=False
            elif(event.key == 100):
                #print('d')
                cammramovement[1]=False
            elif(event.key == 273):
                #print('upkey')
                hero.setkey(3, False)
            elif(event.key == 276):
                #print('leftkey')
                hero.setkey(1, False)
            elif(event.key == 274):
                #print('downkey')
                hero.setkey(2, False)
            elif(event.key == 275):
                #print('rightkey')
                hero.setkey(0, False)
            elif(event.key == 32):
                hero.setkey(4,False)
            else:
                pass
                #print(event.key)
        else:
            pass
            #print(event.type)

    shape.x = shape.x+xvel
    shape.y = shape.y+yvel

    if(shape.bottom>sheight or shape.top<0):
        yvel = yvel * -1
    if(shape.right>swidth or shape.left<0):
        xvel= xvel * -1;
    makeing.Update()
    for u in gamestate.updaters:
        u.Update()
    hero.Update()

    
    for i in range(len(gamestate.platforms)):
        if(hero.getCollision().colliderect(gamestate.platforms[i].getCollision())):
            hero.collide(gamestate.platforms[i])
            gamestate.platforms[i].collide(hero)

    #cammra movement
    if(cammramovement[0]==True):
        gamescreen.changex(3)
    if(cammramovement[1]==True):
        gamescreen.changex(-3)
    if(cammramovement[2]==True):
        gamescreen.changey(3)
    if(cammramovement[3]==True):
        gamescreen.changey(-3)

    if(False):
        if hero.getCollision().right + gamescreen.camx < 0:
            done = True
        if hero.getCollision().left + gamescreen.camx - 600 > 0:
            done = True
        if hero.getCollision().top + gamescreen.camy < 0:
            done = True
        if hero.getCollision().bottom + gamescreen.camy - 400 > 0:
            done = True
        #print(gamescreen.camy + sheight, hero.getCollision().top)



    #screen.
    #screen.blit(starimg,shape)
    gamescreen.clear()
    gamescreen.drawbackground(back)
    #gamescreen.drawRect(shape)
    gamescreen.drawObj(mpf)
    for i in range(len(gamestate.platforms)):
        gamescreen.drawObj(gamestate.platforms[i])

    gamescreen.drawObj(hero)
    #gamescreen.drawRect(rp.getCollision())
    #gamescreen.drawimg(shape,starimg)
    pygame.display.flip()

    timmer.tick(60)

pygame.display.quit()


