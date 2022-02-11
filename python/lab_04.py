import pygame as pg
import random as rd
from math import pi, radians, sin

from pygame.constants import BUTTON_LEFT
WIDTH = 800
HEIGHT = 600

BLUE = (145, 159, 245)
WHITE = (255, 255, 255)
W_WW = (244, 255, 255)
YELLOW = (239, 255, 0)
Y_B = (173, 216, 230)
SEA = (51, 0, 255)
BROWN = (117, 62, 20)
BLACK = (0, 0, 0)
GREY = (119, 119, 119)
RED = (245, 105, 180)
DARK_GREEN = (34, 139, 34)
SKY = (135, 206, 250)
GREEN = (60, 179, 113)
HOUSE = (204, 82, 0)
HOUSE1 = (200, 162, 200)


    
pg.init()
screen = pg.display.set_mode((800, 600))
pg.display.set_caption('CAR AND SUN')
clock = pg.time.Clock()
screen.fill(WHITE)

running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            pg.quit()
            
    pg.draw.arc(screen, (255,0,0), (100,100, 200,200), 0, pi/4, 5)
    #pg.draw.arc(screen, (255,0,0), (100,100, 200,200), pi/4, 0, 150)
    pg.display.update()
    clock.tick(90)