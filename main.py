# Snakedown
# Python-pygame clone of the classic video game, Snake
# Ning Yuan, ningyuan.sg@gmail.com, ningyuan.io
# With help from wailunoob's (wailunoob2@gmail.com) snake_game
# TODO: Add end game screen
# TODO: Add play again option
# TODO: Add score pop ups
# TODO: Add session high scores
# TODO: Add death sounds
# TODO: Make snake blink on eat?

import pygame, sys
from pygame.locals import *
import random

pygame.init()

FPS = 8
SIZE = 20
WINDOW_WIDTH = 360
WINDOW_HEIGHT = 480
assert WINDOW_WIDTH % SIZE == 0 and WINDOW_HEIGHT % SIZE == 0
xGrid = WINDOW_WIDTH // SIZE
yGrid = WINDOW_HEIGHT // SIZE
TOPBORDER = pygame.Rect(0, -1, WINDOW_WIDTH, 1)
BOTTOMBORDER = pygame.Rect(0, WINDOW_HEIGHT, WINDOW_WIDTH, 1)
LEFTBORDER = pygame.Rect(-1, 0, 1, WINDOW_HEIGHT)
RIGHTBORDER = pygame.Rect(WINDOW_WIDTH, 0, 1, WINDOW_HEIGHT)
WINDOW_RES = (WINDOW_WIDTH, WINDOW_HEIGHT)
fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode(WINDOW_RES)
gameState = True
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
    drawcount = 0

    def draw(self):
        for each in self.history:
            pygame.draw.rect(DISPLAYSURF, WHITE, each)

    def drawDead(self):
        if self.drawcount % 3 == 0:
            for each in self.history:
                pygame.draw.rect(DISPLAYSURF, WHITE, each)
        else:
            for each in self.history:
                pygame.draw.rect(DISPLAYSURF, BLACK, each)
        self.drawcount += 1

    def new(self):
        self.history = [
                pygame.Rect(WINDOW_WIDTH//2 - 40, WINDOW_HEIGHT//2, SIZE, SIZE),
                pygame.Rect(WINDOW_WIDTH//2 - 20, WINDOW_HEIGHT//2, SIZE, SIZE)
                ]
        self.score = 0
tail = Tail()


class Snake:
    # spatial
    x = WINDOW_WIDTH // 2  # start x
    y = WINDOW_HEIGHT // 2  # start y
    head = pygame.Rect(x, y, SIZE, SIZE)  #pygame Rect Obj
    # directional
    direction = RIGHT  # start right
    change = RIGHT

    def update(self):
        self.head = pygame.Rect(self.x, self.y, SIZE, SIZE)

    def new(self):
        self.x = WINDOW_WIDTH // 2
        self.y = WINDOW_HEIGHT // 2
        self.update()
        self.direction = RIGHT
        self.change = RIGHT
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
    global gameState
    while gameState:
        DISPLAYSURF.fill(BLACK)
        pygame.display.set_caption("Snakedown")
        ''' TODO: Score display, use images instead of fonts
        scoreObj = pygame.font.Font('freesansbold.tff', 32)
        scoreSurfObj = scoreObj.render(str(score), True, GREY, GREY)
        scoreRectObj = scoreSurfObj.get_rect()
        scoreRectObj.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)
        DISPLAYSURF.blit(scoreSurfObj, scoreRectObj)
        '''
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
                if event.key in (K_UP, K_w) and snake.direction != DOWN:
                    snake.change = UP
                elif event.key in (K_DOWN, K_s) and snake.direction != UP:
                    snake.change = DOWN
                elif event.key in (K_LEFT, K_a) and snake.direction != RIGHT:
                    snake.change = LEFT
                elif event.key in (K_RIGHT, K_d) and snake.direction != LEFT:
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

        # lose conditionals
        headintail, headinwall = False, False
        for block in tail.history:
            if block.collidepoint((snake.x, snake.y)):
                headintail = True
        headintop = snake.head.top < TOPBORDER.bottom
        headinbottom = snake.head.bottom > BOTTOMBORDER.top
        headinleft = snake.head.left < LEFTBORDER.right
        headinright = snake.head.right > RIGHTBORDER.left
        headinwall = headintop or headinbottom or headinleft or headinright
        if headinwall or headintail:
            gameState = False

        pygame.display.update()
        fpsClock.tick(FPS)


def lose(snake, tail, food):
    global gameState
    while not gameState:
        DISPLAYSURF.fill(BLACK)
        pygame.display.set_caption("Snakedown")
        if tail.drawcount % 3 == 0:
            pygame.draw.rect(DISPLAYSURF, WHITE, snake.head)
        else:
            pygame.draw.rect(DISPLAYSURF, BLACK, snake.head)
        tail.drawDead()
        pygame.draw.rect(DISPLAYSURF, ORANGE, food.point)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # newgame
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameState = True
                    snake.new()
                    tail.new()
                    food.new()

        pygame.display.update()
        fpsClock.tick(FPS)
   

def main(snake, tail):
    while True:
        game(snake, tail)
        lose(snake, tail, food)


while __name__ == '__main__':
    main(snake, tail)
