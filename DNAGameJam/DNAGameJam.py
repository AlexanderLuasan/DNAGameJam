import pygame


pygame.init()

#jonathan's comment
timmer = pygame.time.Clock()

swidth = 600
sheight = 400
pygame.display.set_mode([swidth,sheight])
screen = pygame.display.get_surface();

shape = pygame.Rect(0,0,40,40)
shape.center = (swidth/2,sheight/2)

xvel = 2
yvel = 4

starimg = pygame.image.load("star.jpg")
starimg = pygame.transform.scale(starimg,(40,40))

done = False
while(not done):
    for event in pygame.event.get():
        if event.type == 12:
            done = True
        else:
            print(event.type)

    shape.x = shape.x+xvel
    shape.y = shape.y+yvel


    if(shape.bottom>sheight or shape.top<0):
        yvel = yvel * -1
    if(shape.right>swidth or shape.left<0):
        xvel= xvel * -1;

    screen.fill(pygame.Color(200,200,200,255))
    screen.blit(starimg,shape)
    
    pygame.draw.rect(screen,pygame.Color(0, 0, 0, 255),shape,1)
    pygame.display.flip()

    timmer.tick(60)

pygame.display.quit()


