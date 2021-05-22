import random
import numpy as np
import pygame

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

class Grid:
    def __init__(self, width: int, height: int, scale: int) -> None:
        self.WIDTH = int(width / scale)
        self.HEIGHT = int(height / scale)
        self.SIZE = (self.WIDTH, self.HEIGHT)
        self.SCALE = scale

        self.array = np.ndarray(shape=(self.SIZE), dtype=bool)
        self.canvas = pygame.Surface((width, height))
        
        self.randomizer()
        
    def randomizer(self) -> None:
        for x in range(self.WIDTH):
            for y in range(self.HEIGHT):
                self.array[x][y] = random.randint(0,1)

    def checkNeighbours(self, x: int, y: int) -> bool:
        SEARCH_MIN = -1
        SEARCH_MAX = 2

        totalNeighbours: int = 0
        ACTUAL_GRID = self.array[x][y]

        for xIndex in range(SEARCH_MIN, SEARCH_MAX):
            for yIndex in range(SEARCH_MIN, SEARCH_MAX):
                _x = (x + xIndex + self.WIDTH) % self.WIDTH
                _y = (y + yIndex + self.HEIGHT) % self.HEIGHT
                totalNeighbours += self.array[_x][_y]

        totalNeighbours -= ACTUAL_GRID

        if ACTUAL_GRID == 0 and totalNeighbours == 3:
            return 1
        elif ACTUAL_GRID == 1 and (totalNeighbours < 2 or totalNeighbours > 3):
            return 0
        else:
            return ACTUAL_GRID

    def draw(self, screen, xPos: int, yPos: int, color) -> None:
        pygame.draw.rect(screen, color, [xPos, yPos, self.SCALE - 1, self.SCALE - 1])

    def update(self, screen) -> None:
        nextGen = np.ndarray(shape=(self.SIZE), dtype=bool)

        for x in range(self.WIDTH):
            for y in range(self.HEIGHT):
                yPos = y * self.SCALE
                xPos = x * self.SCALE
                color = BLUE if self.array[x][y] == 1 else WHITE
                
                self.draw(self.canvas, xPos, yPos, color)

                nextGen[x][y] = self.checkNeighbours(x, y)

        screen.blit(self.canvas, (0, 0))
        self.array = nextGen