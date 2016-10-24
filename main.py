# 21st Century Snakedown
# Python-pygame clone of the classic snake game
# Ning Yuan, ningyuan.sg@gmail.com, ningyuan.io
# With help from wailunoob's (wailunoob2@gmail.com) snake_game
# TODO: Add end game conditionals
# TODO: Add play again option
# TODO: Add score pop ups
# TODO: Add session high scores
# TODO: Add wasd controls
# TODO: Fix handling?

import pygame, sys
from pygame.locals import *
import random

FPS = 8
global SIZE
SIZE = 20
WINDOW_WIDTH = 360
xGrid = WINDOW_WIDTH // SIZE
WINDOW_HEIGHT = 480
yGrid = WINDOW_HEIGHT // SIZE
WINDOW_RES = (WINDOW_WIDTH, WINDOW_HEIGHT)
pygame.display.set_caption("21st Century Snakedown")
fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode(WINDOW_RES)
# COLOURS  R :  G :  B
WHITE  = (255, 255, 255)
GREY   = (100, 100, 100)
BLACK  = (  0,   0,   0)
ORANGE = (255, 128,   0)
UP = 'up'; DOWN = 'down'; LEFT = 'left'; RIGHT = 'right'


class Tail:
    history = [
            pygame.Rect(WINDOW_WIDTH//2 - 40, WINDOW_HEIGHT//2, SIZE, SIZE),
            pygame.Rect(WINDOW_WIDTH//2 - 20, WINDOW_HEIGHT//2, SIZE, SIZE)
            ]
    score = 0

    def draw(self):
        for each in self.history:
            pygame.draw.rect(DISPLAYSURF, WHITE, each)
tail = Tail()


class Snake:
    # spatial
    x = WINDOW_WIDTH // 2  # start x
    y = WINDOW_HEIGHT // 2  # start y
    head = pygame.Rect(x, y, SIZE, SIZE)  #pygame Rect Obj
    collide = False # turns True in loop if collide with border, or tail
    # directional
    direction = RIGHT  # start right
    change = RIGHT

    def update(self):
        self.head = pygame.Rect(self.x, self.y, SIZE, SIZE)
snake = Snake()


class Food:
    rX = random.randint(0, xGrid - 1) 
    rY = random.randint(0, yGrid - 1)
    point = pygame.Rect(rX * SIZE, rY * SIZE, SIZE, SIZE)

    def new(self):
        self.rX = random.randint(0, xGrid - 1)
        self.rY = random.randint(0, yGrid - 1)
        self.point = pygame.Rect(self.rX * SIZE, self.rY * SIZE, SIZE, SIZE)
food = Food()


def game(snake, tail):
    while True:
        DISPLAYSURF.fill(BLACK)
        pygame.draw.rect(DISPLAYSURF, WHITE, snake.head)
        tail.draw()
        pygame.draw.rect(DISPLAYSURF, ORANGE, food.point)

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
                    snake.change = UP
                elif event.key == pygame.K_DOWN and snake.direction != UP:
                    snake.change = DOWN
                elif event.key == pygame.K_LEFT and snake.direction != RIGHT:
                    snake.change = LEFT
                elif event.key == pygame.K_RIGHT and snake.direction != LEFT:
                    snake.change = RIGHT

        snake.direction = snake.change
        if snake.direction == UP:
            snake.y -= SIZE
        elif snake.direction == DOWN:
            snake.y += SIZE
        elif snake.direction == RIGHT:
            snake.x += SIZE
        elif snake.direction == LEFT:
            snake.x -= SIZE
        snake.update()

        # snake eats food
        if snake.head.collidepoint((food.point.centerx), (food.point.centery)):
            tail.score += 1

        # returns True if food is within snake
        def foodblock(snake, tail):
            foodintail = False
            for block in tail.history:
                if block.collidepoint((food.point.centerx), (food.point.centery)):
                    foodintail = True
            foodinhead = snake.head.collidepoint((food.point.centerx), (food.point.centery))
            return foodintail or foodinhead
        # if food is within snake, respawn food, and test again if it is within snake, and loop
        while foodblock(snake, tail):
            food.new()

        pygame.display.update()
        fpsClock.tick(FPS)


def main(snake, tail):
    pygame.init()
    game(snake, tail)


while __name__ == '__main__':
    main(snake, tail)
