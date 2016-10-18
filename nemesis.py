import pygame

pygame.init()
screen = pygame.display.set_mode((400,300))
pygame.display.set_caption("shield hacking")
JogoAtivo = True
GAME_BEGIN = False
# Speed in pixels per frame
speedX = 0
speedY = 0
cordX = 10
cordY = 100
groundX=0;
groundY=200;



def draw():
    screen.fill((0, 0, 0))
    ground = pygame.draw.rect(screen, (0, 255, 0), (groundX, groundY,400, 10))
    quadrado = pygame.draw.rect(screen, (255, 0, 0), (cordX, cordY ,50, 52))
    pygame.display.flip();
    
    

       
while JogoAtivo:
    for evento in pygame.event.get():
        print(evento)
    #verifica se o evento que veio eh para fechar a janela
        if evento.type == pygame.QUIT:
               JogoAtivo = False
               pygame.quit();
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_a:
                   print('GAME BEGIN')
                   GAME_BEGIN = True
                   draw();        
            if evento.key == pygame.K_LEFT:
                   speedX=-0.006
                   run= True;
            if evento.key == pygame.K_RIGHT:
                   speedX=0.006
                   run= True;
            if evento.key == pygame.K_SPACE:
                   speedY=-0.3
                   jumping= True;
        if evento.type == pygame.KEYUP:
             if evento.key == pygame.K_SPACE:
                   speedY=+0.2
                   jumping= True;
                

    if GAME_BEGIN:
        cordX+=speedX
        cordY+=speedY
        draw();
        
        if cordY +50>= groundY:
            speedY=0
            jumping=False;

          


