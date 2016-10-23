# 21st Century Snakedown
# Python-pygame clone of the classic snake game
# Ning Yuan, ningyuan.sg@gmail.com, ningyuan.io
# With help from wailunoob's (wailunoob2@gmail.com) snake_game
# TODO: Add food spawns
# TODO: Add collision with food (+ growth)
# TODO: Add end game conditionals
# TODO: Add play again option
# TODO: Add score pop ups
# TODO: Add session high scores
# TODO: Add wasd controls
# TODO: Fix 180 turn exploit

import pygame, sys
from pygame.locals import *

FPS = 8
global SIZE
SIZE = 20
WINDOW_WIDTH = 360
xGrids = WINDOW_WIDTH / SIZE
WINDOW_HEIGHT = 480
yGrids = WINDOW_HEIGHT / SIZE
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
    x = WINDOW_WIDTH / 2  # start x
    y = WINDOW_HEIGHT / 2  # start y
    head = pygame.Rect(x, y, SIZE, SIZE)  #pygame Rect Obj
    collide = False # turns True in loop if collide with border, or tail
    # directional
    direction = RIGHT  # start right

    def update(self):
        self.head = pygame.Rect(self.x, self.y, SIZE, SIZE)
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
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # change directions
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
            snake.y -= SIZE
        elif snake.direction == DOWN:
            snake.y += SIZE
        elif snake.direction == RIGHT:
            snake.x += SIZE
        elif snake.direction == LEFT:
            snake.x -= SIZE
        snake.update()

        pygame.display.update()
        fpsClock.tick(FPS)


while __name__ == '__main__':
    main(snake, tail)
