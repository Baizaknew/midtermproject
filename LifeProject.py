# please click "space" when you start the code.
import pygame
from copy import deepcopy
from random import randint

RES = WIDTH, HEIGHT = 1550, 800
NAME = 20
width, height = WIDTH // NAME, HEIGHT // NAME
FPS = 15

pygame.init()
polygon = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

next_field = [[0 for i in range (width)] for j in range(height)]
current_field = [[randint(0,1) for i in range (width )] for j in range(height)]

def cell(current_field, x, y):
    count = 0
    for j in range(y-1, y+2):
        for i in range(x-1, x+2):
            if current_field[j][i]:
                count +=1

    if current_field[y][x]:
        count -=1
        if count ==2 or count ==3:
            return 1
        return 0
    else:
        if count ==3:
            return 1
        return 0

zz = 1
while zz!=0:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                zz = 0
clock.tick(30)


while True:

    polygon.fill(pygame.Color('black'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # рисуем сетку
    [pygame.draw.line(polygon, pygame.Color('darkslategray'), (x,0), (x, HEIGHT)) for x in range(0, WIDTH, NAME)]
    [pygame.draw.line(polygon, pygame.Color('darkslategray'), (0,y), (WIDTH, y)) for y in range(0, HEIGHT, NAME)]
    # строим жизнь
    for x in range(1, width-1):
        for y in range(1, height-1):
            if current_field[y][x]:
                pygame.draw.rect(polygon,pygame.Color('green2'), (x*NAME+2, y*NAME+2, NAME-2, NAME-2))
            next_field[y][x]= cell(current_field, x, y)
    current_field = deepcopy(next_field)

    pygame.display.flip()
    clock.tick(FPS)

