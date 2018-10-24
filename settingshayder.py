import random
import pygame as pg
pg.mixer.init()
# Settings
WIDTH, HEIGHT = 800, 600
TITLE = "Dark Jumper"
FPS = 60

# Colors
# Primary Colors
RED = (255,0,0)
GREEN = (25,255,0)
BLUE = (0,0,255)

# Secondary Colors
YELLOW = (255,255,0)
CYAN = (0,255,255)
MAGENTA = (255,0,255)

# Other Colors
WHITE = (255,255,255)
BLACK = (0,0,0)

# Player Properties
PLAYER_GRAV = 0.52
BIRD_PATH = ["assets/images/flappybird.png","assets/images/flappybird2.png","assets/images/flappybird3.png"]

#Sounds Properties
FLAP_SOUND = pg.mixer.Sound("assets/audio/wing.ogg")
HIT_SOUND = pg.mixer.Sound("assets/audio/hit.ogg")
POINT_SOUND = pg.mixer.Sound("assets/audio/point.ogg")
SWOOSH_SOUND = pg.mixer.Sound("assets/audio/swoosh.ogg")

#Tube Properties
TUBE_COLOR = (107, 44, 38)
TUBE_X = 800
TUBE_Y = 0
TUBE_WIDTH = 100

# Background
Background = pg.image.load("assets/images/skybackground.png")
SAND = (81, 30, 21)
