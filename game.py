import pygame
import os
screen=pygame.display.set_mode((800,500))
playing=True
fp=60
VELOCITY=5
clock=pygame.time.Clock()
pygame.font.init()
pygame.mixer.init()
HEALTH_FONT=pygame.font.SysFont('comicsans',40)
bulletlaunchsound=pygame.mixer.Sound('Gun+Silencer.mp3')
bullethitsound=pygame.mixer.Sound('Grenade+1.mp3')
bgimage=pygame.image.load('background.png')
bgimage1=pygame.transform.scale(bgimage,(800,500))
redimage=pygame.image.load('rocket1.png')
yellowimage=pygame.image.load('rocket2.png')
redimage1=pygame.transform.rotate(pygame.transform.scale(redimage,(50,50)),270)
yellowimage1=pygame.transform.rotate(pygame.transform.scale(yellowimage,(50,50)),90)

yellow=pygame.Rect(150,200,40,40)
red=pygame.Rect(600,200,40,40)

border=pygame.Rect(400,0,10,500)

redhealth=10
yellowhealth=10
maxbullets=3
bulletvelocity=7
def handle_bullets(yellowbullets,redbullets,yellow,red):
    global yellowhealth, redhealth
    for b in yellowbullets:
        b.x=b.x+bulletvelocity
        if red.colliderect(b):
            yellowbullets.remove(b)
            redhealth=redhealth-1
            print(redhealth)
            bullethitsound.play()


    for b1 in redbullets:
        b1.x=b1.x-bulletvelocity
        if yellow.colliderect(b1):
            redbullets.remove(b1)
            yellowhealth=yellowhealth-1
            print(yellowhealth)
            bullethitsound.play()

redbullets=[]
yellowbullets=[]
    
    

while playing:
    def redmove(keypressed,red):
        if keypressed[pygame.K_UP] and red.y>0 :
            red.y=red.y-5
        if keypressed[pygame.K_DOWN] and red.y<460:
            red.y=red.y+5
        if keypressed[pygame.K_LEFT] and red.x>400:
            red.x=red.x-5
        if keypressed[pygame.K_RIGHT] and red.x<760:
            red.x=red.x+5
    def yellowmove(keypressed,yellow):
        if keypressed[pygame.K_w] and yellow.y>0:
            yellow.y=yellow.y-5
        if keypressed[pygame.K_s] and yellow.y<460:
            yellow.y=yellow.y+5
        if keypressed[pygame.K_a] and yellow.x>0:
            yellow.x=yellow.x-5
        if keypressed[pygame.K_d] and yellow.x<360:
            yellow.x=yellow.x+5

    

    clock.tick(fp)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            playing=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_c:
                bulletlaunchsound.play()
                bullet=pygame.Rect(yellow.x+20,yellow.y+20,10,5)
                
                yellowbullets.append(bullet)
            if event.key==pygame.K_SPACE:
                bulletlaunchsound.play()
                bullet4=pygame.Rect(red.x+20,red.y+20,10,5)
                redbullets.append(bullet4)



    screen.blit(bgimage1,(0,0))
    screen.blit(yellowimage1,(yellow.x,yellow.y))
    screen.blit(redimage1,(red.x,red.y))
    redhealthtext=HEALTH_FONT.render('Health:'+str(redhealth),1,(9, 167, 230))
    yelllowhealthtext=HEALTH_FONT.render('Health:'+str(yellowhealth),1,(9,167,230))
    #screen.blit(str(yellowhealth),(320,200))
    screen.blit(redhealthtext,(430,10))
    screen.blit(yelllowhealthtext,(10,10))
    
    if yellowhealth<=0:
        winnertext=HEALTH_FONT.render('Red wins',1,(9, 167, 230))
        screen.blit(winnertext,(200,200))
        pygame.display.update()
        pygame.time.delay(5000)                       
        pygame.quit()
    if redhealth<=0:
        winnertext=HEALTH_FONT.render('Yellow wins',1,(9, 167, 230))
        screen.blit(winnertext,(200,200))
        pygame.display.update()
        pygame.time.delay(5000)                       
        pygame.quit()


    pygame.draw.rect(screen,(19, 242, 213),border)
    keypressed=pygame.key.get_pressed()
    redmove(keypressed,red)
    yellowmove(keypressed,yellow)
    handle_bullets(yellowbullets,redbullets,yellow,red)
    for b in redbullets:
        pygame.draw.rect(screen,(79, 63, 20),b)
    for b in yellowbullets:
        pygame.draw.rect(screen,(79, 63, 20),b)
    pygame.display.update()





