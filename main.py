import pygame

pygame.init();
screen = pygame.display.set_mode((400,300));
pygame.display.set_caption("menu");
menuAtivo = True;
start_button = pygame.draw.rect(screen,(0,0,240),(150,90,100,50));
continue_button = pygame.draw.rect(screen,(255,244,0),(150,160,100,50));
quit_button = pygame.draw.rect(screen,(244,0,0),(150,230,100,50));
button_names =["START" , "CONTINUE", "QUIT"]; 
i=0;
y=90;
pygame.display.flip();


font = pygame.font.Font(None, 40);
text = font.render("Super Shield Hacking", 1, (0, 240, 0));
screen.blit(text,(50,20));  
pygame.display.update();


while i<=2:
    font = pygame.font.Font(None, 20);
    text = font.render(button_names[i], 1, (0, 0, 0));
    screen.blit(text,(150,y));  
    pygame.display.update();
    i=i+1;
    y+=70;
    



def startGame():
    screen.fill((0,0,0));
    pygame.display.flip();
    import nemesis.py;  
    
while menuAtivo:
    for evento in pygame.event.get():
        print(evento);
        if evento.type == pygame.MOUSEBUTTONDOWN:
                        #quit button
            if pygame.mouse.get_pos()[0] >= 150 and pygame.mouse.get_pos()[1] >= 230:
                if pygame.mouse.get_pos()[0] <= 250 and pygame.mouse.get_pos()[1] <= 280:
                        pygame.quit()
                        #start button
            if pygame.mouse.get_pos()[0] >= 150 and pygame.mouse.get_pos()[1] >= 90:
                if pygame.mouse.get_pos()   [0] <= 250 and pygame.mouse.get_pos()[1] <= 140:
                        verify = open('verify_continue.txt' , "w")
                        verify.write("N")
                        verify.close();
                        startGame();
                        #continue button
            if pygame.mouse.get_pos()[0] >= 150 and pygame.mouse.get_pos()[1] >= 160:
                if pygame.mouse.get_pos()[0] <= 250 and pygame.mouse.get_pos()[1] <= 210:
                        verify = open('verify_continue.txt' , "w")
                        verify.write("S")
                        verify.close();
                        startGame();            
