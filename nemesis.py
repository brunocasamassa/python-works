import pygame
import os

pygame.init()
screen = pygame.display.set_mode((400,300))
pygame.display.set_caption("shield hacking")
JogoAtivo = True
GAME_BEGIN = False
run =True
jumping =True;
# Speed in pixels per frame
speedX = 0
speedY = 0
cordX = 10;
cordY = 150;
groundX=0;
groundY=200;
verify = open('verify_continue.txt' , "r");



def loadCoords():
    f1 = open( "coords.txt", "r")
    text=f1.read()
    num_list=text.split()
    print (num_list)
    cordX=num_list[0]
    print(cordX)
    cordY=num_list[1]
    f1.close()  
    return cordX,cordY
    

def copiaArquivo(cordX, cordY):
  x=str(cordX);
  y=" "+str(cordY);
  f1 = open( 'coords.txt', "w")
  f1.write(x);
  f2 = open( 'coords.txt', "w")
  f2.seek(2)
  f2.write(y);
  f1.close()
  f2.close()


def draw():
    screen.fill((0, 0, 0))
    ground = pygame.draw.rect(screen, (0, 255, 0), (groundX, groundY,400, 10))
    square = pygame.draw.rect(screen, (255, 0, 0), (cordX, cordY ,50, 50))
    enemy = pygame.draw.rect(screen, (255, 0, 155), (200, 150 ,50, 50));
    pygame.display.flip();
    if square.colliderect(enemy) == True:
        run=False;
          
             
    
""" SCREEN(press START)  """ 
font = pygame.font.SysFont(None, 55);
text = font.render("Press A to Start", 1, (255, 0, 0));
screen.blit(text,(50,20));
pygame.display.update();

       
while JogoAtivo:
    for evento in pygame.event.get():
        print(evento)
        
    #verifica se o evento que veio eh para fechar a janela
        if evento.type == pygame.QUIT:
               JogoAtivo = False
               copiaArquivo(cordX, cordY);
               pygame.quit();
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_a:
                   print('GAME BEGIN')
                   GAME_BEGIN = True
                   if verify.read()=="S":
                       cordX,cordY=loadCoords();
                       cordX = float(cordX);
                       cordY = float(cordY);
                   pygame.mixer.init();
                   sound1 = pygame.mixer.Sound('GunsNRoses_ParadiseRemix_xD.wav');
                   chan1 = pygame.mixer.find_channel()
                   chan1.queue(sound1);
            if evento.key == pygame.K_LEFT:
                   speedX=-0.006
                   run= True;
            if evento.key == pygame.K_RIGHT:
                   speedX=0.006
                   run= True;
            if evento.key == pygame.K_SPACE:
                   speedY=-0.3
                   jumping= True;
                   sound2 = pygame.mixer.Sound('MMX2_SE_00019.wav');
                   chan2 = pygame.mixer.find_channel();
                   chan2.queue(sound2);
        if evento.type == pygame.KEYUP:
             if evento.key == pygame.K_SPACE:
                   speedY=+0.2
                   
                   
                

    if GAME_BEGIN:
        draw();
        if run == True:   
            cordX+=speedX
        if jumping == True:
            cordY+=speedY
   
        
        """ground detection"""
        if cordY +50>= groundY:
            speedY=0
        if cordX + 50 >=200 and cordX <=250:
            speedX=0;

          


