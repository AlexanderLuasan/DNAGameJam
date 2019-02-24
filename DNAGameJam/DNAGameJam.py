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
import time
pygame.font.init()


writting = pygame.font.SysFont("arial",26,False,False)

gameovertext = writting.render("Gave Over", True, pygame.Color(0,0,0))
gameoverrect = gameovertext.get_rect()
#print(testcandy.id())


#sprite.test()


gamestate = None


pygame.init()
pygame.mixer.music.load("resource/flatfootintro.mp3")
pygame.mixer.music.play()

hero = None
#jonathan's comment
timmer = pygame.time.Clock()

swidth = 1280
sheight =600
pygame.display.set_mode([swidth,sheight])
pygame.display.set_caption("stolen sweets")
gamescreen=screen.window(pygame.display.get_surface())
gameoverrect.center = (swidth/2,sheight/2)


if(not pygame.mixer.music.get_busy()):
    pygame.mixer.music.load("resource/flatfootmain.mp3")
    pygame.mixer.music.play()


back = backgroundimg(0,0,"resource/image.jpg")
#back = backgroundimg(0,0,"resource/background.jpg")

cammramovement = [False,False,False,False]

menuing = True
game = True
playing = False
death = False
win = False

while(game):#the window is open


    
    while(menuing):#menu
        if(not pygame.mixer.music.get_busy()):
            pygame.mixer.music.load("resource/flatfootmain.mp3")
            pygame.mixer.music.play()
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
   

        
    if(death):
        gamescreen.drawimg(gameoverrect,gameovertext)
        pygame.display.flip()
    while(death):#Death
        if(not pygame.mixer.music.get_busy()):
            pygame.mixer.music.load("resource/flatfootmain.mp3")
            pygame.mixer.music.play()
        for event in pygame.event.get():
            if (event.type == 12):
                game = False
                death = False
            elif(event.type == 3):
                death = False
                menuing = True
        
    if(win):
        points = writting.render("you got " + str(hero.score) + " points", True, pygame.Color(0,0,0))
        pointsrect = points.get_rect()
        pointsrect.center = (swidth/2,sheight/2)
        gamescreen.drawimg(pointsrect,points)
        pygame.display.flip()
    while(win):
        if(not pygame.mixer.music.get_busy()):
            pygame.mixer.music.load("resource/flatfootmain.mp3")
            pygame.mixer.music.play()
        for event in pygame.event.get():
            if (event.type == 12):
                game = False
                win = False
            elif(event.type == 3):
                win = False
                menuing = True
        
    
    if(playing):
        gamestate = levelload.level("resource/newmap.tmx")
        hero = player(Rect(gamestate.px,gamestate.py,28,133))
        gamescreen.camx = 0
        gamescreen.camy =0 
        

    while(playing):
        if(not pygame.mixer.music.get_busy()):
            pygame.mixer.music.load("resource/flatfootmain.mp3")
            pygame.mixer.music.play()
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


        if(hero.getCollision().right + gamescreen.camx-800 > 0):
            gamescreen.changex(-hero.velx)

        if hero.getCollision().right + gamescreen.camx < -50:
            playing = False
            death = True
            print("death")
            #done = True
        if hero.getCollision().left + gamescreen.camx - 1280 > 50:
            playing = False
            death = True
            print("death")
        if hero.getCollision().bottom + gamescreen.camy < -50:
            playing = False
            death = True
            print("death")
        if hero.getCollision().top + gamescreen.camy - 600 > 50:
            playing = False
            death = True
            print("death")
        
            #print(gamescreen.camy + sheight, hero.getCollision().top)

        if gamestate.gamefinished==True:
            win=True
            playing=False
            print("victory")

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


