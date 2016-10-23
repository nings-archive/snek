# 21st Century Snakedown
# Python-pygame clone of the classic snake game
# Ning Yuan, ningyuan.sg@gmail.com, ningyuan.io
# With help from wailunoob's (wailunoob2@gmail.com) snake_game

import pygame, sys
from pygame.locals import *

FPS = 3
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 360
WINDOW_HEIGHT = 480
WINDOW_RES = (WINDOW_WIDTH, WINDOW_HEIGHT)
# COLOURS  R :  G :  B
WHITE  = (255, 255, 255)
GREY   = (100, 100, 100)
BLACK  = (  0,   0,   0)
ORANGE = (255, 128,   0)
# SNAKE
snakeSIZE = 20
snakex = WINDOW_WIDTH / 2  # start x
snakey = WINDOW_HEIGHT / 2  # start y
snakeHead = pygame.Rect(snakex, snakey, snakeSIZE, snakeSIZE)
snakeCollide = False  # turns True in loop if collide with border, or tail
UP = 'up'; DOWN = 'down'; LEFT = 'left'; RIGHT = 'right'  # snake directions
snakeDirection = RIGHT  # start right

def main():
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode(WINDOW_RES)
    pygame.display.set_caption("21st Century Snakedown")

    while True:
        DISPLAYSURF.fill(BLACK)
        pygame.draw.rect(DISPLAYSURF, WHITE, snakeHead)

        if snakeDirection == UP:
            snakey += snakeSIZE
        elif snakeDirection == DOWN:
            snakey -= snakeSIZE
        elif snakeDirection == RIGHT:
            snakex += snakeSIZE
        elif snakeDirection == LEFT:
            snakex -= snakeSIZE

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        fpsClock.tick(FPS)


while __name__ == '__main__':
    main()
