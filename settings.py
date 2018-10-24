import pygame as pg



# define some colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
ROOD = (48, 15, 11)
# game settings
WIDTH = 1024   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 768  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 80
TITLE = "HAUNTED DUNGEON"
BGCOLOR = DARKGREY


TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE


WALL_IMG = 'tile_07.png'
MOB_IMG = 'bruin.png'
OBJECTO_IMG = 'key1.png'
DOOR1_IMG = 'door1.png'
DOOR2_IMG = 'door2.png'
SPRITESHEETIMG = 'Demi_Game_Sprites.png'


# Player settings
PLAYER_SPEED = 300
PLAYER_ROT_SPEED = 250
PLAYER_IMG = 'manBlue_gun.png'
PLAYER_HIT_RECT = pg.Rect(0, 0, 15, 15)

# Mob settings

MOB_SPEED = 250
AVOID_RADIUS = 120
AVOID_RADIUSWALLS = 40
DETECT_RADIUS = 600

MOB_HIT_RECT = pg.Rect(0, 0, 30, 30)

MUZZLE_FLASHES = ['whitePuff15.png', 'whitePuff16.png', 'whitePuff17.png',
                  'whitePuff18.png']
FLASH_DURATION = 40
BOB_RANGE = 13
BOB_SPEED2 = 0.5
BOB_SPEED = 1
BOB_RANGE1 = 13
BOB_SPEED1 = 0.8

# Sounds
BG_MUSIC = 'DST-RailJet-LongSeamlessLoop.ogg'
PLAYER_HIT_SOUNDS = ['pain/8.wav', 'pain/9.wav', 'pain/10.wav', 'pain/11.wav']
ZOMBIE_MOAN_SOUNDS = ['brains2.wav', 'brains3.wav', 'zombie-roar-1.wav', 'zombie-roar-2.wav',
                      'zombie-roar-3.wav', 'zombie-roar-5.wav', 'zombie-roar-6.wav', 'zombie-roar-7.wav']
ZOMBIE_HIT_SOUNDS = ['splat-15.wav']
WEAPON_SOUNDS_GUN = ['sfx_weapon_singleshot2.wav']
EFFECTS_SOUNDS = {'level_start': 'level_start.wav',
                  'health_up': 'health_pack.wav'}
