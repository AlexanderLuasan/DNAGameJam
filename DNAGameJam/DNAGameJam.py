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


#print(testcandy.id())


#sprite.test()


gamestate = levelload.level("resource/newmap.tmx")


pygame.init()

#pygame.mixer.music.load("flatfoot.mp3")
#pygame.mixer.music.play()
hero = player(Rect(gamestate.px,gamestate.py,28,133))
#jonathan's comment
timmer = pygame.time.Clock()

swidth = 1280
sheight =600
pygame.display.set_mode([swidth,sheight])
gamescreen=screen.window(pygame.display.get_surface())





back = backgroundimg(0,0,"resource/background.jpg")


cammramovement = [False,False,False,False]

menuing = True
game = True
playing = False
while(game):#the window is open


    
    while(menuing):#menu
        for event in pygame.event.get():
            if (event.type == 12):
                game = False
                menuing = False
            elif(event.type == 3):
                menuing = False
                playing = True


        gamescreen.clear()
        pygame.display.flip()

        timmer.tick(60)

    

    while(False):#menu
        print("death")

    while(False):#menu
        print("sucsess")
    
    

    while(playing):
        for event in pygame.event.get():
            if (event.type == 12):
                playing = False
                game = False
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

        gamestate.checkevents(abs(gamescreen.camx))
        gamescreen.changex(-1)

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

    
        if hero.getCollision().right + gamescreen.camx < 0:
            done = True
        if hero.getCollision().left + gamescreen.camx - 1280 > 0:
            done = True
        if hero.getCollision().top + gamescreen.camy < 0:
            done = True
        if hero.getCollision().bottom + gamescreen.camy - 600 > 0:
            done = True
            #print(gamescreen.camy + sheight, hero.getCollision().top)



        #screen.
        #screen.blit(starimg,shape)
        gamescreen.clear()
        gamescreen.drawbackground(back)
        #gamescreen.drawRect(shape)
        for i in range(len(gamestate.platforms)):
            gamescreen.drawObj(gamestate.platforms[i])

        gamescreen.drawObj(hero)
        #gamescreen.drawRect(rp.getCollision())
        #gamescreen.drawimg(shape,starimg)
        pygame.display.flip()

        timmer.tick(60)

pygame.display.quit()


