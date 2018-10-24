import pygame as pg
import sys
from os import path
from pygame_functions import *
from settings import *
from sprites import *
from tilemap import *
import random
import time

def aix(self):
    self.loopy = pygame.USEREVENT + 1
    pygame.time.set_timer(self.loopy, 100)
    self.loopx = pygame.USEREVENT + 2
    pygame.time.set_timer(self.loopx, 100)
    self.xnieuw = 0

def ailoop(self):
    for event in pg.event.get():
        if event.type == self.loopy and self.xnieuw <= 10:

            print ("1")
            self.mob.move(dx=1)
            self.mob.move(dx=(random.randint(0, 1)))
            self.mob.move(dy=1)
            self.mob.move(dy=(random.randint(0, 1)))
            self.mob1.move(dx=-1)
            self.mob1.move(dx=(random.randint(-1, 0)))
            self.mob1.move(dy=1)
            self.mob1.move(dy=(random.randint(-1, 0)))
            self.xnieuw += 1

        if event.type == self.loopx and self.xnieuw >= 10 and self.xnieuw <= 20:
            print ("2")
            self.mob.move(dx=-1)
            self.mob.move(dx=(random.randint(-1, 0)))
            self.mob.move(dy=-1)
            self.mob.move(dy=(random.randint(-1, 0)))
            self.mob1.move(dx=1)
            self.mob1.move(dx=(random.randint(0, 1)))
            self.mob1.move(dy=-1)
            self.mob1.move(dy=(random.randint(0, 1)))
            self.xnieuw += 1

        if self.xnieuw > 20:
            self.xnieuw = 0
