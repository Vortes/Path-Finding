import pygame
pygame.init()

SIZE = WIDTH, HEIGHT = 500, 500
SCREEN = pygame.display.set_mode(SIZE)

RUNNING = True

while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
 
pygame.quit()