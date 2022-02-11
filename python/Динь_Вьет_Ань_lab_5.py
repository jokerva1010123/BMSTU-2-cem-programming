import pygame as pg
import random as rd

SIZE = WIDTH, HEIGHT = 800, 600 #the width and height of our screen
BACKGROUND_COLOR = pg.Color('white') #The background colod of our window
FPS = 0.5 #Frames per second

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
N_B = (160, 82, 45)
h = 600
w = 800
class MySprite(pg.sprite.Sprite):
    def __init__(self):
        super(MySprite, self).__init__()

        self.images = []
        self.images.append(pg.image.load('images/walk1.png'))
        self.images.append(pg.image.load('images/walk2.png'))
        self.images.append(pg.image.load('images/walk3.png'))
        self.images.append(pg.image.load('images/walk4.png'))
        self.images.append(pg.image.load('images/walk5.png'))
        self.images.append(pg.image.load('images/walk6.png'))
        self.images.append(pg.image.load('images/walk7.png'))
        self.images.append(pg.image.load('images/walk8.png'))
        self.images.append(pg.image.load('images/walk9.png'))
        self.images.append(pg.image.load('images/walk10.png'))

        self.index = 0

        self.image = self.images[self.index]

        self.rect = pg.Rect(0, 400, 0, 0)

    def update(self):
        if(self.rect.x < w):
            self.rect.x += 1
        else:
            self.rect.x = -150
        self.index += 1

        if self.index >= len(self.images)*10:
            self.index = 0
        
        self.image = self.images[(self.index)//10]

class Car(pg.sprite.Sprite):
    def __init__(self, x, filename):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(filename).convert_alpha()
        self.image = pg.transform.scale(self.image, (200, 140))
        self.rect = self.image.get_rect(center=(x, 450))
    def update(self):
        if self.rect.x < w:
            self.rect.x += 2
        else:
            self.rect.x = 0

def draw_sky():
    pg.draw.rect(screen, SKY, (0, 0, 800, 600 - 130))

'''Отрисовка солнца с лучами(обстрактными)'''
def draw_sun():
    pg.draw.circle(screen, Y_B, (10, 10), 200)
    pg.draw.circle(screen, YELLOW, (10, 10), 90)
    
'''Отрисовка дороги.'''
def draw_road():
    pg.draw.rect(screen, GREY,(0, h - 130, w, h))
    pg.draw.line(screen, WHITE, (0, h - 65), (w, h - 65), 2)
    for i in range(5):
        pg.draw.rect(screen, WHITE,(600, h - 125 + (i * 30), 80, 20))

'''Отрислвка деревьев.'''        
def draw_tree():
    for i in range(5):
        pg.draw.rect(screen, BROWN,(130 * i + 10, 330, 20, 140))
        if (i % 2 == 0):
            pg.draw.circle(screen, DARK_GREEN, (130 * i + 20, 350), 50)
        else:
            pg.draw.circle(screen, GREEN, (130 * i + 20, 350), 50)

def draw_cloud(start_x, w):
    pg.draw.circle(screen, W_WW, (start_x + 90, 125), 48)
    pg.draw.circle(screen, W_WW, (start_x + 130, 120), 40)
    pg.draw.circle(screen, W_WW, (start_x + 50, 130), 30)
    pg.draw.circle(screen, W_WW, (start_x + 170, 130), 25)

def draw_cloud1(start_x, w):
    pg.draw.ellipse(screen, W_WW, (start_x, 100, w, 60))
    pg.draw.circle(screen, W_WW, (start_x + 90, 125), 48)
    pg.draw.circle(screen, W_WW, (start_x + 130, 120), 40)
    pg.draw.circle(screen, W_WW, (start_x + 50, 130), 30)
    pg.draw.circle(screen, W_WW, (start_x + 170, 135), 20)

def draw_house():
    pg.draw.rect(screen, HOUSE,(620, h - 300, 150, 170))
    pg.draw.polygon(screen, N_B, [(620, h - 300),
                                  (695, h - 350),
                                  (770, h - 300)])
    pg.draw.rect(screen, HOUSE1, (660, h - 250, 75, 120))
pg.init()
screen = pg.display.set_mode(SIZE)
my_sprite = MySprite()
my_group = pg.sprite.Group(my_sprite)
clock = pg.time.Clock()
screen.fill(SKY)
pg.display.flip()
def main():
    car1 = Car(100, 'car2.png')
    cstart = rd.randint(0, 200)
    cstart1 = rd.randint(200, 600)
    cstart2 = rd.randint(500, 800)
    cwidth = 250
    cwidth1 = 200
    cwidth2 = 200
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
        draw_sky()
        draw_road()
        draw_tree()
        draw_house()
        draw_sun()

        draw_cloud(cstart, cwidth)
        draw_cloud1(cstart1, cwidth1)
        draw_cloud(cstart2, cwidth2)
        screen.blit(car1.image, car1.rect)
        cstart -= 1
        cstart1 -= 2
        cstart2 -= 1
        if cstart <= -250:
            cstart = w + 200
        if cstart1 <= -250:
            cstart1 = w + 200
        if cstart2 <= -250:
            cstart2 = w + 200
        if car1.rect.x < w:
            car1.rect.x += 5
        else:
            car1.rect.x = -200

        my_group.update()
        my_group.draw(screen)
        pg.display.update()
        clock.tick(90)

if __name__ == '__main__':
    main()