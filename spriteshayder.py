import pygame as pg
import random
from settingshayder import *

# This is a pygame vector
vec = pg.math.Vector2

# This is the player class
class Player(pg.sprite.Sprite):
	def __init__(self,imagePath,game):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.image.load(imagePath)
		self.rect = self.image.get_rect()
		self.rect.center = (WIDTH / 2, HEIGHT / 2)

		# This is the players position
		self.pos = vec(WIDTH / 2, HEIGHT /2)

		# This is the players velocity
		self.vel = vec(0,0)

		# This is the players acceleration
		self.acc = vec(0,0)

		# This is the game class
		self.game = game

	def update(self):
		# This is the force of gravity acting on the player
		self.acc = vec(0,PLAYER_GRAV)

		# This is the acceleration acting on the velocity
		self.vel += self.acc

		# This is the players position changing
		self.pos += self.vel +0.5 * self.acc

		# This sets the players new position
		self.rect.midbottom = self.pos

# This is the tube class
class Tube(pg.sprite.Sprite):
	def __init__(self,x,y,w,h,color):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.Surface((w,h))
		self.image.fill(color)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

		# This is the tubes x velocity, giving the appearance of the player moving
		self.velX = -2

		# If a tube goes of the screen then it is 'killed'
		if self.rect.right < 0:
			self.kill()

	def update(self):
		# This is the cause of the tubes movement
		self.rect.x += self.velX

# This is the grounds class
class Ground(pg.sprite.Sprite):
	def __init__(self,x,y,w,h):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.Surface((w,h))
		self.image.fill(SAND)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
