# 21st Century Snakedown
# Python-pygame clone of the classic snake game
# Ning Yuan, ningyuan.sg@gmail.com, ningyuan.io
# With help from wailunoob's (wailunoob2@gmail.com) snake_game

import pygame, sys
from pygame.locals import *

FPS = 8  # set 1 for debugging mode, 8 for normal
WINDOW_WIDTH = 360
WINDOW_HEIGHT = 480
WINDOW_RES = (WINDOW_WIDTH, WINDOW_HEIGHT)
fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode(WINDOW_RES)
# COLOURS  R :  G :  B
WHITE  = (255, 255, 255)
GREY   = (100, 100, 100)
BLACK  = (  0,   0,   0)
ORANGE = (255, 128,   0)
UP = 'up'; DOWN = 'down'; LEFT = 'left'; RIGHT = 'right'

# TAIL
class Tail:
    SIZE = 20
    history = [
            pygame.Rect(WINDOW_WIDTH/2 - 40, WINDOW_HEIGHT/2, SIZE, SIZE),
            pygame.Rect(WINDOW_WIDTH/2 - 20, WINDOW_HEIGHT/2, SIZE, SIZE)
            ]
    score = 0

    def draw(self):
        for each in self.history:
            pygame.draw.rect(DISPLAYSURF, WHITE, each)
tail = Tail()

# SNAKE
class Snake:
    # spatial
    SIZE = 20
    x = WINDOW_WIDTH / 2  # start x
    y = WINDOW_HEIGHT / 2  # start y
    head = pygame.Rect(x, y, SIZE, SIZE)  #pygame Rect Obj
    collide = False # turns True in loop if collide with border, or tail
    # directional
    direction = RIGHT  # start right

    def update(self):
        self.head = pygame.Rect(self.x, self.y, self.SIZE, self.SIZE)
snake = Snake()

def main(snake, tail):
    pygame.init()
    pygame.display.set_caption("21st Century Snakedown")

    while True:
        DISPLAYSURF.fill(BLACK)
        pygame.draw.rect(DISPLAYSURF, WHITE, snake.head)
        tail.draw()

        if len(tail.history) == tail.score + 2:
            tail.history = tail.history[1:]
        tail.history.append(snake.head)

        for event in pygame.event.get():
            # exit
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # change directions
            # TODO: add wasd controls
            # TODO: snake can still turn 180 with two rapid taps
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != DOWN:
                    snake.direction = UP
                elif event.key == pygame.K_DOWN and snake.direction != UP:
                    snake.direction = DOWN
                elif event.key == pygame.K_LEFT and snake.direction != RIGHT:
                    snake.direction = LEFT
                elif event.key == pygame.K_RIGHT and snake.direction != LEFT:
                    snake.direction = RIGHT

        if snake.direction == UP:
            snake.y -= snake.SIZE
        elif snake.direction == DOWN:
            snake.y += snake.SIZE
        elif snake.direction == RIGHT:
            snake.x += snake.SIZE
        elif snake.direction == LEFT:
            snake.x -= snake.SIZE
        snake.update()

        pygame.display.update()
        fpsClock.tick(FPS)


while __name__ == '__main__':
    main(snake, tail)
