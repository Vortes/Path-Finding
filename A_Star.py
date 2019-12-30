import pygame
pygame.init()
pygame.display.set_caption('A Star Pathfinding')

SIZE = WIDTH, HEIGHT = 500, 500
SCREEN = pygame.display.set_mode(SIZE)
CLOCK = pygame.time.Clock()

RUNNING = True

while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
 
pygame.quit()