import pygame
pygame.init()
pygame.display.set_caption('A Star Pathfinding')

SCREEN = pygame.display.set_mode((255, 255))
CLOCK = pygame.time.Clock()


WIDTH, HEIGHT = 20, 20
MARGIN = 5
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SCREEN.fill(BLACK)


def create_grids():
    grid = []
    for row in range(10):
        grid.append([])
        for column in range(10):
            grid[row].append(0)
    return grid


grid = create_grids()
grid[0][2] = 1


def create_board():
    for column in range(0, 255, WIDTH + MARGIN):
        for row in range(0, 255, HEIGHT + MARGIN):

            pygame.draw.rect(SCREEN, WHITE, (column + MARGIN, row + MARGIN, WIDTH, HEIGHT))


RUNNING = True
while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False

    create_board()
    pygame.display.update()
 
pygame.quit()