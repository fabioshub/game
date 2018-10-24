import pygame as pg
from settings import *
from pygame_functions import *
import random
from random import randint, choice
import pyganim
from tilemap import collide_hit_rect
import pytweening as tween
start_ticks=pg.time.get_ticks() #starter tick


vec = pg.math.Vector2



# class Player(pg.sprite.Sprite):
    # def __init__(self, game, x, y):
    #     self.groups = game.all_sprites, game.players
    #     pg.sprite.Sprite.__init__(self, self.groups)
    #     self.game = game
    #     self.image_orig = game.player_img
    #     self.image_orig.set_colorkey(BLACK)
    #     self.image = self.image_orig.copy()
    #     self.rect = self.image.get_rect()
    #     self.vol = vec(0, 0)
    #     self.pos = vec(x, y)
    #
    #     self.rot = 0
    #     self.nextlvl = False
    #
    # def get_keys(self):
    #     if keyPressed('up'):
    #         self.rot = 90
    #     if keyPressed('down'):
    #         self.rot = -90
    #     if keyPressed('left'):
    #         self.rot = 180
    #     if keyPressed('right'):
    #         self.rot = 0
    #
    #
    # def move(self, dx=0, dy=0):
    #     if not self.collide_with_walls(dx, dy):
    #         self.pos.x += dx
    #         self.pos.y += dy
    #     if self.collide_with_obj(dx, dy):
    #         self.game.objecto.kill()
    #         self.game.openblock.kill()
    #     if self.collide_with_exit(dx, dy):
    #         self.game.new1()
    #
    # def powerup(self):
    #     Wall1(self.game, self.pos.x, self.pos.y)
    #     # return False
    #
    #
    # def collide_with_walls(self, dx=0, dy=0):
    #     for wall in self.game.walls:
    #         if wall.x == self.pos.x + dx and wall.y == self.pos.y + dy:
    #             return True
    #     return False
    #
    # def collide_with_obj(self, dx=0, dy=0):
    #     for objecto in self.game.collect:
    #         if objecto.x == self.pos.x + dx and objecto.y == self.pos.y + dy:
    #             return True
    #     return False
    #
    # def collide_with_exit(self, dx=0, dy=0):
    #     for exitblock in self.game.exitblocks:
    #         if exitblock.x == self.pos.x + dx and exitblock.y == self.pos.y + dy:
    #             return True
    #     return False
    #
    #
    # def update(self):
    #     self.get_keys()
    #     self.image = pg.transform.rotate(self.image_orig, (self.rot))
    #     #self.pos += self.vol * self.game.dt
    #     self.rect.x = self.pos.x * TILESIZE
    #     self.rect.y = self.pos.y * TILESIZE

def collide_with_walls(sprite, group, dir):
    if dir == 'x':
        hits = pg.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if sprite.vel.x > 0:
                sprite.pos.x = hits[0].rect.left - sprite.hit_rect.width / 2
            if sprite.vel.x < 0:
                sprite.pos.x = hits[0].rect.right + sprite.hit_rect.width / 2
            sprite.vel.x = 0
            sprite.hit_rect.centerx = sprite.pos.x
    if dir == 'y':
        hits = pg.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if sprite.vel.y > 0:
                sprite.pos.y = hits[0].rect.top - sprite.hit_rect.height / 2
            if sprite.vel.y < 0:
                sprite.pos.y = hits[0].rect.bottom + sprite.hit_rect.height / 2
            sprite.vel.y = 0
            sprite.hit_rect.centery = sprite.pos.y


class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.spritesheet
        self.rect = self.image.get_rect()
        self.hit_rect = MOB_HIT_RECT.copy()
        self.hit_rect.center = self.rect.center
        self.vel = vec(0, 0)
        self.pos = vec(x, y) * TILESIZE
        self.rect.center = self.pos
        self.rot = 0
        self.normal()

    def normal(self):
        self.player_speeds = 300

    def unnormal(self):
        pass

    def get_keys(self):
        self.rot_speed = 0
        self.vel = vec(0, 0)

        if keyPressed('up'):
            self.rot = 90
            self.vel = vec(self.player_speeds, 0).rotate(-self.rot)
        if keyPressed('down'):
            self.rot = -90
            self.vel = vec(self.player_speeds, 0).rotate(-self.rot)
        if keyPressed('left'):
            self.rot = 180
            self.vel = vec(self.player_speeds, 0).rotate(-self.rot)

        if keyPressed('right'):
            self.vel = vec(self.player_speeds, 0).rotate(-self.rot)
            self.rot = 0

    def update(self):
        self.get_keys()
        self.rot = (self.rot + self.rot_speed * self.game.dt) % 360
        self.image = pg.transform.rotate(self.game.spritesheet, self.rot)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.pos += self.vel * self.game.dt
        self.hit_rect.centerx = self.pos.x
        collide_with_walls(self, self.game.walls, 'x')
        self.hit_rect.centery = self.pos.y
        collide_with_walls(self, self.game.walls, 'y')
        self.rect.center = self.hit_rect.center

# class Mob1212(pg.sprite.Sprite):
#     def __init__(self, game, x, y):
#         self.groups = game.all_sprites, game.mobs
#         pg.sprite.Sprite.__init__(self, self.groups)
#         self.game = game
#         self.image_orig = game.mob_img
#         self.image_orig.set_colorkey(BLACK)
#         self.image = self.image_orig.copy()
#         self.rect = self.image.get_rect()
#         self.vol = vec(0, 0)
#         self.pos = vec(x, y)
#         self.x = x
#         self.y = y
#         self.rot = 0
#
#     def move(self, dx=0, dy=0):
#         if not self.collide_with_walls(dx, dy):
#             self.pos.x += dx
#             self.pos.y += dy
#         if self.collide_with_mob(dx, dy):
#             self.game.show_death_screen()
#
#         if dx == 1:
#             self.rot = 0
#
#         if dx == -1:
#             self.rot = 180
#
#         if dy == 1:
#             self.rot = -90
#
#         if dy == -1:
#             self.rot = 90
    #
    # def collide_with_walls(self, dx=0, dy=0):
    #     for wall in self.game.walls:
    #         if wall.x == self.pos.x + dx and wall.y == self.pos.y + dy:
    #             return True
    #     return False
    #
    # def collide_with_mob(self, dx=0, dy=0):
    #     for player in self.game.players:
    #         if player.pos.x == self.pos.x + dx and player.pos.y == self.pos.y + dy:
    #             return True
    #     return False
    #
    # def update(self):
    #
    #
    #     self.image = pg.transform.rotate(self.image_orig, (self.rot))
    #     self.rect.x = self.pos.x * TILESIZE
    #     self.rect.y = self.pos.y * TILESIZE
    #
    #


class objecto(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.collect
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image_orig = game.obj_img
        self.image_orig.set_colorkey(BLACK)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.vol = vec(0, 0)
        self.pos = vec(x, y)
        self.x = x
        self.y = y
        self.tween = tween.easeInOutSine
        self.tweeny = tween.easeInOutBounce
        self.step = 0
        self.dir = 1


    def update(self):
        self.rect.x = self.pos.x * TILESIZE
        self.rect.y = self.pos.y * TILESIZE
                # bobbing motion
        offset = BOB_RANGE1 * (self.tween(self.step / BOB_RANGE1) - 0.5)
        self.rect.centery = self.rect.y + offset * self.dir
        # offset2 = BOB_RANGE * (self.tweeny(self.step / BOB_RANGE) - 0.5)
        # self.rect.centerx = self.rect.x + offset2 * self.dir
        self.step += BOB_SPEED1
        if self.step > BOB_RANGE1:
            self.step = 0
            self.dir *= -1


class exitblock(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.exitblocks
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image_orig = game.obj_img
        self.image_orig.set_colorkey(BLACK)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.vol = vec(0, 0)
        self.pos = vec(x, y)
        self.x = x
        self.y = y


    def update(self):
        self.rect.x = self.pos.x * TILESIZE
        self.rect.y = self.pos.y * TILESIZE


class door1(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image_orig = game.door1_img
        self.image_orig.set_colorkey(BLACK)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.vol = vec(0, 0)
        self.pos = vec(x, y)
        self.x = x
        self.y = y
        self.tween = tween.easeInOutSine
        self.step = 0
        self.dir = 1


    def update(self):
        self.rect.x = self.pos.x * TILESIZE
        self.rect.y = self.pos.y * TILESIZE
        offset = BOB_RANGE * (self.tween(self.step / BOB_RANGE) - 0.5)
        self.rect.centerx = self.rect.x + offset * self.dir +16
        self.step += BOB_SPEED
        if self.step > BOB_RANGE:
            self.step = 1
            self.dir *= -1

class door2(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image_orig = game.door2_img
        self.image_orig.set_colorkey(BLACK)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.vol = vec(0, 0)
        self.pos = vec(x, y)
        self.x = x
        self.y = y
        self.tween = tween.easeInOutSine
        self.step = 0.2
        self.dir = 1


    def update(self):
        self.rect.x = self.pos.x * TILESIZE
        self.rect.y = self.pos.y * TILESIZE
        offset = BOB_RANGE * (self.tween(self.step / BOB_RANGE) - 0.5)
        self.rect.centerx = self.rect.x + offset * self.dir +16
        self.step += BOB_SPEED
        if self.step > BOB_RANGE:
            self.step = 0
            self.dir *= -1

class wallmoving(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image_orig = game.wall_img
        self.image_orig.set_colorkey(BLACK)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.vol = vec(0, 0)
        self.pos = vec(x, y)
        self.x = x
        self.y = y
        self.tween = tween.easeInOutSine
        self.step = 0
        self.dir = 1


    def update(self):
        self.rect.x = self.pos.x * TILESIZE
        self.rect.y = self.pos.y * TILESIZE
        offset = BOB_RANGE * (self.tween(self.step / BOB_RANGE) - 0.5)
        self.rect.centery = self.rect.y + offset * self.dir +16
        self.step += BOB_SPEED2
        if self.step > BOB_RANGE:
            self.step = 1
            self.dir *= -1



class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):

        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        #self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image = game.wall_img

        #self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        self.pos = vec(x, y) * TILESIZE


# class bg(pg.sprite.Sprite):
#     def __init__(self, game, x, y):
#
#         self.groups = game.all_sprites, game.bg
#         pg.sprite.Sprite.__init__(self, self.groups)
#         self.game = game
#         #self.image = pg.Surface((TILESIZE, TILESIZE))
#         self.image = pg.Surface((TILESIZE, TILESIZE))
#         self.image.fill(YELLOW)
#         #self.image.fill(YELLOW)
#         self.rect = self.image.get_rect()
#         self.x = x
#         self.y = y
#         self.rect.x = x * TILESIZE
#         self.rect.y = y * TILESIZE


class wall1(pg.sprite.Sprite):
    def __init__(self, game, x, y):

        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        # self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image = game.wall_img

        #self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.pos = vec(x, y) * TILESIZE
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        self.tween = tween.easeInOutSine
        self.step = 0
        self.dir = 1

    def update(self):
        self.rect.x = self.pos.x * TILESIZE
        self.rect.y = self.pos.y * TILESIZE
        offset = BOB_RANGE * (self.tween(self.step / BOB_RANGE) - 0.5)
        self.rect.centery = self.rect.y + offset * self.dir +16
        self.step += BOB_SPEED2
        if self.step > BOB_RANGE:
            self.step = 1
            self.dir *= -1




class mob(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.mobs
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        # seconds=(pg.time.get_ticks()-start_ticks)/100 #calculate how many seconds
    # endticks = (pg.time.get_ticks - startticks) / 1000
        self.image = game.mob_img1


        self.rect = self.image.get_rect()
        self.hit_rect = MOB_HIT_RECT.copy()
        self.hit_rect.center = self.rect.center
        self.pos = vec(x, y) * TILESIZE
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.rect.center = self.pos
        self.rot = 0



    def avoid_mobs(self):
        for mob in self.game.mobs:
            if mob != self:
                dist = self.pos - mob.pos
                if 0 < dist.length() < AVOID_RADIUS:
                    self.acc += dist.normalize()

    def avoid_walls(self):
        for wall1 in self.game.walls:
            dist = self.pos - wall1.pos
            if 0 < dist.length() < AVOID_RADIUSWALLS:
                self.acc += dist.normalize()

    def update(self):
        target_dist = self.game.player.pos - self.pos
        if target_dist.length_squared() < DETECT_RADIUS**2:
            self.rot = (self.game.player.pos - self.pos).angle_to(vec(1, 0))
            self.image = pg.transform.rotate(self.game.mob_img1, self.rot)
            self.rect = self.image.get_rect()
            self.rect.center = self.pos
            self.acc = vec(2, 1).rotate(-self.rot)
            self.avoid_walls()
            self.avoid_mobs()
            self.acc.scale_to_length(MOB_SPEED)
            self.acc += self.vel * -1
            self.vel += self.acc * self.game.dt
            self.pos += self.vel * self.game.dt + 0.5 * self.acc * self.game.dt ** 1.3
            self.hit_rect.centerx = self.pos.x
            collide_with_walls(self, self.game.walls, 'x')
            self.hit_rect.centery = self.pos.y
            collide_with_walls(self, self.game.walls, 'y')
            self.rect.center = self.hit_rect.center
anitime =+ 1
