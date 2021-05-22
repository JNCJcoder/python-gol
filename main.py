import pygame
from grid import Grid

SIZE = WIDTH, HEIGHT = 800, 600

pygame.init()
pygame.display.set_caption("Conway Game of Life")
screen = pygame.display.set_mode(SIZE)

clock = pygame.time.Clock()

game = Grid(WIDTH, HEIGHT, 20)

isRunning = True
while isRunning:
    clock.tick(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
    
    game.update(screen)
    
    pygame.display.flip()

pygame.quit()