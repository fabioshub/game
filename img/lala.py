from pygame_functions import *
from settings import *

import pygame as pg
import sys
from os import path
from pygame_functions import *
from settings import *
from sprites import *
from tilemap import *
import random
import time
vec = pg.math.Vector2

sys.path.insert(0, '/path/to/application/app/folder')

import file







screenSize (WIDTH, HEIGHT)
setBackgroundColour("green")

ja = makeLabel("startmenu", 50, (WIDTH/2)-200, HEIGHT/2, fontColour='black', font='Arial', background='clear')


nee = 0
while nee != 30:
    dil = makeSprite("img/tyn.png")
    transformSprite(dil, 0, 2)
    moveSprite(dil, (WIDTH/2)-300, HEIGHT/2 - nee )
    showSprite(dil)

    ja = [10,20,30]
    for x in ja:
        nee = x

    print (nee)


boxy = makeTextBox((WIDTH/2)-200, HEIGHT*1/3, 400, 0, "type fabio of demi", 5, 50)
showLabel(boxy)
wachtwoord = textBoxInput(boxy)
if wachtwoord == "fabio":
    import main

if wachtwoord == "demi":
    import
else:
    hideLabel(boxy)
    boxy = makeTextBox((WIDTH/2)-200, HEIGHT/2+20, 400, 0, "type fabio of demi", 5, 50)
    showLabel(boxy)
    wachtwoord = textBoxInput(boxy)


endWait()
