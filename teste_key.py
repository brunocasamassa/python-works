import pygame
pygame.init()
pygame.display.set_mode((400,300))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); #sys.exit() if sys is imported
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                print("Hey, you pressed the key, '0'!")
            if event.key == pygame.K_LEFT:
                print("Doing whatever")