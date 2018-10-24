import sys
import math
import pygame
import random
from pygame.locals import *
from gameobjects import Vector2

def demigame():
    WIDTH = 800
    HEIGHT = 600
    FPS = 60

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    pygame.init()
    pygame.mixer.init()
    screen      = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("It's starting to look like something")
    clock       = pygame.time.Clock()
    spawn_timer = 200
    playerpos   = [0, 0]
    difference  = [0, 0]

    class Player(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.load_images()
            self.image      = self.standing_frames[1]
            self.clock      = pygame.time.Clock()
            self.rect       = self.image.get_rect()
    #        self.rect       = pygame.Rect(0, 0, 30, 22)

    # (7, 10, 16, 40)
    #        pygame.draw.rect(self.image, GREEN, self.rect)
            self.pos        = Vector2(WIDTH/2, HEIGHT/2)
            self.rect.x     = WIDTH/2
            self.rect.y     = HEIGHT/2
            self.speed      = 180
            self.angle      = 12

            self.moving     = False
            self.last_update = pygame.time.get_ticks()
            self.frame_rate = 150
            self.frame      = 0

        def load_images(self):
            self.standing_frames = [asset_images.subsurface((34, 70), (30, 44)),
                                    asset_images.subsurface((76, 70), (30, 44)),
                                    asset_images.subsurface((120, 70), (30, 44)),
                                    asset_images.subsurface((120, 14), (30, 44)),
                                    asset_images.subsurface((76, 14), (30, 44)),
                                    asset_images.subsurface((34, 14), (30, 44))]
            self.move_down       = [asset_images.subsurface((34, 392),(30, 44)),
                                    asset_images.subsurface((66, 392),(30, 44)),
                                    asset_images.subsurface((76, 70),(30, 44)),
                                    asset_images.subsurface((98, 392),(30, 44)),
                                    asset_images.subsurface((130, 392),(30, 44))]
            self.move_right       = [asset_images.subsurface((34, 496),(30, 44)),
                                    asset_images.subsurface((66, 496),(30, 44)),
                                    asset_images.subsurface((120, 70), (30, 44)),
                                    asset_images.subsurface((98, 496),(30, 44)),
                                    asset_images.subsurface((130, 496),(30, 44))]
            self.move_left        = []
            for frame in self.move_right:
                self.move_left.append(pygame.transform.flip(frame, True, False))

            self.move_rightback   = [asset_images.subsurface((34, 548),(30, 44)),
                                    asset_images.subsurface((66, 548),(30, 44)),
                                    asset_images.subsurface((120, 14), (30, 44)),
                                    asset_images.subsurface((98, 548),(30, 44)),
                                    asset_images.subsurface((130, 548),(30, 44))]
            self.move_leftback    = []
            for frame in self.move_rightback:
                self.move_leftback.append(pygame.transform.flip(frame, True, False))

            self.move_up           = [asset_images.subsurface((34, 444),(30, 44)),
                                    asset_images.subsurface((66, 444),(30, 44)),
                                    asset_images.subsurface((76, 14), (30, 44)),
                                    asset_images.subsurface((98, 444),(30, 44)),
                                    asset_images.subsurface((130, 444),(30, 44))]

        def update(self):
            key = pygame.key.get_pressed()
            now = pygame.time.get_ticks()
            mouse = pygame.mouse.get_pos()
            self.direction = Vector2(0, 0)
            if key[pygame.K_d]:
                self.direction.x += 1
            if key[pygame.K_a]:
                self.direction.x -= 1
            if key[pygame.K_w]:
                self.direction.y -= 1
            if key[pygame.K_s]:
                self.direction.y += 1

            self.direction.normalize()

            timepass = self.clock.tick(60)

            oldrectx = self.rect.x
            oldrecty = self.rect.y
            self.pos.x += self.direction.x * self.speed * (timepass / 1000)
            self.pos.y += self.direction.y * self.speed * (timepass / 1000)
            self.rect.x = self.pos.x
            self.rect.y = self.pos.y
            difference[0] = (self.rect.x - oldrectx)
            difference[1] = (self.rect.y - oldrecty)
            playerpos[0]  = (self.rect.x + (self.image.get_width() / 2))
            playerpos[1]  = (self.rect.y + (self.image.get_height() / 2))


            ##########################################################################
            #                     Mouse Angle & Sprite update                        #
            ##########################################################################
            offset      = ((mouse[1] - self.pos.y - (self.image.get_height() / 2)),
                           (mouse[0] - self.pos.x - (self.image.get_width() / 2)))
            self.angle  = 135 - math.degrees(math.atan2(*offset))
    #        print(self.angle)

            if difference[0] == 0 and difference[1] == 0:
                if self.angle >= -45 and self.angle <= 15:
                    self.image = self.standing_frames[0]
                if self.angle > 15 and self.angle < 75:
                    self.image = self.standing_frames[1]
                if self.angle >= 75 and self.angle <= 135:
                    self.image = self.standing_frames[2]

                if self.angle > 135 and self.angle < 195:
                    self.image = self.standing_frames[3]
                if self.angle >= 195 and self.angle <= 255:
                    self.image = self.standing_frames[4]
                if self.angle > 255 and self.angle < 315:
                    self.image = self.standing_frames[5]

            if difference[0] != 0 or difference[1] != 0:
                self.moving = True
            else:
                self.moving = False

            if self.moving:
                if now - self.last_update > self.frame_rate:
                    self.last_update = now
                    self.frame = (self.frame + 1) % len(self.move_down)
                    if self.angle >= -45 and self.angle <= 15:
                        self.image = self.move_left[self.frame]
                    if self.angle > 15 and self.angle < 75:
                        self.image = self.move_down[self.frame]
                    if self.angle >= 75 and self.angle <= 135:
                        self.image = self.move_right[self.frame]

                    if self.angle > 135 and self.angle < 195:
                        self.image = self.move_rightback[self.frame]
                    if self.angle >= 195 and self.angle <= 255:
                        self.image = self.move_up[self.frame]
                    if self.angle > 255 and self.angle < 315:
                        self.image = self.move_leftback[self.frame]


            """
            if self.angle >= -45 and self.angle <= 15:
                self.image = asset_images.subsurface((34, 70), (30, 44))
            if self.angle > 15 and self.angle < 75:
                self.image = asset_images.subsurface((76, 70), (30, 44))
            if self.angle >= 75 and self.angle <= 135:
                self.image = asset_images.subsurface((120, 70), (30, 44))
    
            if self.angle > 135 and self.angle < 195:
                self.image = asset_images.subsurface((120, 14), (30, 44))
            if self.angle >= 195 and self.angle <= 255:
                self.image = asset_images.subsurface((76, 14), (30, 44))
            if self.angle > 255 and self.angle < 315:
                self.image = asset_images.subsurface((34, 14), (30, 44))
            """



        """
            if (key[pygame.K_s] or key[pygame.K_a] or key[pygame.K_w] or key[pygame.K_d]) and now - self.last_update > self.frame_rate:
                self.last_update = now
                if self.angle > 15 and self.angle < 75:
                    self.frame += 1
                    if self.frame == 1:
                        self.image = asset_images.subsurface((34, 392),(30, 44))
                    if self.frame == 2:
                        self.image = asset_images.subsurface((66, 392),(30, 44))
                    if self.frame == 3:
                        self.image = asset_images.subsurface((76, 70),(30, 44))
                    if self.frame == 4:
                        self.image = asset_images.subsurface((98, 392),(30, 44))
                    if self.frame == 5:
                        self.frame = 0
                        self.image = asset_images.subsurface((130, 392),(30, 44))
        """

        def shoot(self):
            bullet      = Playerbullet((((self.pos.x + self.image.get_width()/2)),
                                        (self.pos.y + self.image.get_height()/2)), (self.angle))
            all_sprites.add(bullet)
            bullets.add(bullet)

        def animate(self):
            now = pygame.time.get_ticks()
            if difference[0] != 0 or difference[1] != 0:
                self.moving = True
            else:
                self.moving = False

            if self.moving:
                if now - self.last_update > self.frame_rate:
                    self.last_update = now
                    self.frame = (self.frame + 1) % len(self.move_down)
                    self.image = self.move_down[self.frame]


        def dodge(self):
            self.pos.x += 30
            self.pos.y += 30
            self.rect.x = self.pos.x
            self.rect.y = self.pos.y
    class Arms(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.original_img = asset_images.subsurface((310, 110), (52, 12))
            self.image      = self.original_img.copy()
            self.clock      = pygame.time.Clock()
            self.rect       = self.image.get_rect()

            self.rect.x     = (WIDTH/2) - 12
            self.rect.y     = (HEIGHT/2)+26
            self.speed      = 180

        def update(self):
            mouse = pygame.mouse.get_pos()
            self.rect.x += difference[0]
            self.rect.y += difference[1]

            offset = (mouse[1]-self.rect.centery, mouse[0]-self.rect.centerx)
            self.angle = 180-math.degrees(math.atan2(*offset))

            if self.angle > 90 and self.angle < 270:
                self.original_img = asset_images.subsurface((310, 92), (52, 14))
            if self.angle < 90 or self.angle > 270:
                self.original_img = asset_images.subsurface((310, 110), (52, 12))

            self.image = pygame.transform.rotate(self.original_img, self.angle)
            self.rect = self.image.get_rect(center=self.rect.center)
    class Mob(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = asset_images.subsurface((112, 132), (46, 94))
            self.rect = self.image.get_rect()

            self.spawnpoint = (random.randint(WIDTH / 10, WIDTH - (WIDTH / 10)), 100)
            self.pos = Vector2(self.spawnpoint[0], self.spawnpoint[1])
            self.rect.x = self.spawnpoint[0]
            self.rect.y = self.spawnpoint[1]
            self.health = 5
            self.clock = pygame.time.Clock()
            self.timer = 0
            self.shoottimer = 0

            self.standing = random.randint(60, 200)
            self.shoot = self.standing + 20


        def update(self):
            timepass = self.clock.tick(60)

            offset = ((playerpos[1] - self.pos.y - (self.image.get_height() / 2)),
                      (playerpos[0] - self.pos.x - (self.image.get_width() / 2)))
            self.angle = 135 - math.degrees(math.atan2(*offset))

            if self.shoottimer == self.shoot:
                bullet = Enemybullet(((self.pos.x + self.image.get_width() / 2),
                                      (self.pos.y + self.image.get_height() / 2)), self.angle)
                all_sprites.add(bullet)
                enemybullets.add(bullet)

            if self.shoottimer == self.shoot + 20:
                self.shoottimer = 0

            self.timer += 1
            self.shoottimer += 1
    class Mob2(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = asset_images.subsurface((30, 132), (40, 22))
            self.rect = self.image.get_rect()

            self.spawnpoint = (random.randint(WIDTH / 10, WIDTH - (WIDTH / 10)), random.randint(HEIGHT / 10, HEIGHT - (HEIGHT / 10)))
            self.pos = Vector2(self.spawnpoint[0], self.spawnpoint[1])
            self.rect.x = self.spawnpoint[0]
            self.rect.y = self.spawnpoint[1]
            self.speed = random.randint(50, 70)
            self.health = 1
            self.clock = pygame.time.Clock()
            self.direction = Vector2(0, 0)
            self.timer      = 0
            self.shoottimer = 0

            self.standing   = random.randint(60, 200)
            self.shoot      = self.standing + 20


        def update(self):
            self.direction = Vector2(playerpos[0], playerpos[1])- self.pos
            if self.direction.x < 40 and self.direction.x > -40:
                self.direction.x = 0
            if self.direction.y < 40 and self.direction.y > -40:
                self.direction.y = 0
            self.direction.normalize()

            timepass = self.clock.tick(60)

            offset = ((playerpos[1] - self.pos.y - (self.image.get_height() / 2)),
                      (playerpos[0] - self.pos.x - (self.image.get_width() / 2)))
            self.angle = 135 - math.degrees(math.atan2(*offset))

            if self.shoottimer > self.standing:
                self.direction = Vector2(0, 0)

            if self.shoottimer == self.shoot:
                bullet = Enemybullet(((self.pos.x + self.image.get_width() / 2),
                                    (self.pos.y + self.image.get_height() / 2)), self.angle)
                all_sprites.add(bullet)
                enemybullets.add(bullet)

            if self.shoottimer == self.shoot + 20:
                self.shoottimer = 0


            self.pos.x += self.direction.x * self.speed * (timepass / 1000)
            self.pos.y += self.direction.y * self.speed * (timepass / 1000)
            self.rect.x = self.pos.x
            self.rect.y = self.pos.y
            self.timer += 1
            self.shoottimer += 1

            if self.timer >= 10:
                self.image = asset_images.subsurface((30, 158), (40, 22))
            if self.timer >= 20:
                self.image = asset_images.subsurface((30, 132), (40, 22))
            if self.timer >= 30:
                self.image = asset_images.subsurface((30, 184), (40, 22))
            if self.timer >= 40:
                self.image = asset_images.subsurface((30, 132), (40, 22))
                self.timer = 0


            if self.pos.x <= 20:
                self.pos.x = 20
                self.direction.x = -self.direction.x
            if self.pos.x >= (WIDTH - 20 - self.image.get_width()):
                self.pos.x = (WIDTH - 19 - self.image.get_width())
                self.direction.x = -self.direction.x
            if self.pos.y <= 136:
                self.pos.y = 136
                self.direction.y = -self.direction.y
            if self.pos.y >= (HEIGHT - 20 - self.image.get_height()):
                self.pos.y = (HEIGHT - 19 - self.image.get_height())
                self.direction.y = -self.direction.y
    class Mob2_spawn(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image  = asset_images.subsurface((28, 286), (28, 20))
            self.clock  = pygame.time.Clock()
            self.rect   = self.image.get_rect()
            self.rect.x = 500
            self.rect.y = 500
            self.timer  = 0

        def update(self):
    #        if spawn_timer == 30:
    #            self.image = asset_images.subsurface((28, 286), (28, 20))
            if self.timer == 10:
                self.image = asset_images.subsurface((68, 280), (44, 28))
            if self.timer == 20:
                self.image = asset_images.subsurface((114, 266), (48, 42))
            if self.timer == 30:
                self.image = asset_images.subsurface((110, 326), (58, 38))
                self.timer = 0

            self.timer += 1
    class Eye(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image  = asset_images.subsurface((178, 130), (128, 96))
            self.clock  = pygame.time.Clock()
            self.rect   = self.image.get_rect()
            self.rect.x = 400 - 64
            self.rect.y = 20
            self.pos    = Vector2(336, 20)
            self.timer  = 0

        def update(self):
            offset = ((playerpos[1] - self.pos.y - (self.image.get_height() / 2)),
                      (playerpos[0] - self.pos.x - (self.image.get_width() / 2)))
            self.angle = 135 - math.degrees(math.atan2(*offset))
            self.timer += 1

            if self.timer > 160 or self.timer < 20 and spawn_timer > 170:
                self.image = asset_images.subsurface((178, 234), (128, 96))
            else:
                self.image = asset_images.subsurface((178, 130), (128, 96))
            if self.timer >= 180 and spawn_timer > 170:
                bullet = Eyebullet(((self.pos.x + self.image.get_width() / 2),
                                       (self.pos.y + self.image.get_height() / 2)), self.angle)
                all_sprites.add(bullet)
                eyebullets.add(bullet)
                self.timer = 0
    class Eyelid(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image  = asset_images.subsurface((434, 130), (128, 96))
            self.clock  = pygame.time.Clock()
            self.rect   = self.image.get_rect()
            self.rect.x = 400 - 64
            self.rect.y = 20

        def update(self):
            if spawn_timer == 30:
                self.image = asset_images.subsurface((434, 234), (128, 96))
            if spawn_timer == 35:
                self.image = asset_images.subsurface((306, 234), (128, 96))
            if spawn_timer == 40:
                self.image = asset_images.subsurface((306, 130), (128, 96))

            if spawn_timer == 150:
                self.image = asset_images.subsurface((306, 234), (128, 96))
            if spawn_timer == 155:
                self.image = asset_images.subsurface((434, 234), (128, 96))
            if spawn_timer > 160:
                self.image = asset_images.subsurface((434, 130), (128, 96))
    class Playerbullet(pygame.sprite.Sprite):
        def __init__(self, location, angle):
            pygame.sprite.Sprite.__init__(self)
            self.image      = asset_images.subsurface((190, 28), (8, 8))
            self.rect       = self.image.get_rect(center=location)

    #        pygame.draw.rect(self.image, RED, self.rect)
    #        pygame.draw.rect(self.image, RED, (1, 1, 6, 6))
            self.angle      = -math.radians(angle - 135)
            self.move       = [self.rect.x, self.rect.y]
            self.speed_mag  = 6
            self.speed      = (self.speed_mag * math.cos(self.angle),
                               self.speed_mag * math.sin(self.angle))
            self.done = False

        def update(self):
            self.move[0] += self.speed[0]
            self.move[1] += self.speed[1]
            self.rect.topleft = self.move

            if self.move[0] <= 0 or self.move[0] >= 1000:
                self.kill()
            if self.move[1] <= 120 or self.move[1] >= 1000:
                bang = Playerbulletexplos(self.rect.center)
                all_sprites.add(bang)
                self.kill()
    class Playerbulletexplos(pygame.sprite.Sprite):
        def __init__(self, center):
            pygame.sprite.Sprite.__init__(self)
            self.image = asset_images.subsurface((188, 16), (12, 12))
            self.rect = self.image.get_rect()
            self.rect.center = center
            self.last_update = pygame.time.get_ticks()
            self.frame_rate  = 100
            self.frame       = 1

        def update(self):
            now = pygame.time.get_ticks()
            if now - self.last_update > self.frame_rate:
                self.last_update = now
                if self.frame >= 2:
                    self.kill()
                else:
                    self.frame += 1
                    center = self.rect.center
                    self.image = asset_images.subsurface((186, 0), (16, 16))
                    self.rect = self.image.get_rect()
                    self.rect.center = center
    class Enemybullet(pygame.sprite.Sprite):
        def __init__(self, location, angle):
            pygame.sprite.Sprite.__init__(self)
            self.image      = asset_images.subsurface((170, 22), (14, 14))
            self.rect       = self.image.get_rect(center=location)

            self.angle      = -math.radians(angle - 135)
            self.move       = [self.rect.x, self.rect.y]
            self.speed_mag  = 6
            self.speed      = (self.speed_mag * math.cos(self.angle),
                               self.speed_mag * math.sin(self.angle))
            self.done = False

        def update(self):
            self.move[0] += self.speed[0]
            self.move[1] += self.speed[1]
            self.rect.topleft = self.move

            if self.move[0] <= 0 or self.move[0] >= 1000:
                self.kill()
            if self.move[1] <= 120 or self.move[1] >= 1000:
                bang = Enemybulletexplos(self.rect.center)
                all_sprites.add(bang)
                self.kill()
    class Enemybulletexplos(pygame.sprite.Sprite):
        def __init__(self, center):
            pygame.sprite.Sprite.__init__(self)
            self.image = asset_images.subsurface((172, 6), (14, 14))
            self.rect = self.image.get_rect()
            self.rect.center = center
            self.last_update = pygame.time.get_ticks()
            self.frame_rate  = 100
            self.frame       = 1

        def update(self):
            now = pygame.time.get_ticks()
            if now - self.last_update > self.frame_rate:
                self.last_update = now
                if self.frame >= 3:
                    self.kill()
                else:
                    self.frame += 1
                    center = self.rect.center
                    if self.frame == 2:
                        self.image = asset_images.subsurface((150, 22), (18, 18))
                    if self.frame == 3:
                        self.image = asset_images.subsurface((150, 0), (22, 22))
                    self.rect = self.image.get_rect()
                    self.rect.center = center
    class Eyebullet(pygame.sprite.Sprite):
        def __init__(self, location, angle):
            pygame.sprite.Sprite.__init__(self)
            self.image = asset_images.subsurface((206, 12), (38, 38))
            self.rect = self.image.get_rect(center=location)

            self.angle = -math.radians(angle - 135)
            self.move = [self.rect.x, self.rect.y]
            self.speed_mag = 6
            self.speed = (self.speed_mag * math.cos(self.angle),
                          self.speed_mag * math.sin(self.angle))
            self.done = False

        def update(self):
            self.move[0] += self.speed[0]
            self.move[1] += self.speed[1]
            self.rect.topleft = self.move

            if self.move[0] <= 0 or self.move[0] >= 1000:
                self.kill()
            if self.move[1] <= 0 or self.move[1] >= 1000:
                self.kill()
    class Eyebulletexplos(pygame.sprite.Sprite):
        def __init__(self, center):
            pygame.sprite.Sprite.__init__(self)
            self.image = asset_images.subsurface((346, 12), (38, 38))
            self.rect = self.image.get_rect()
            self.rect.center = center
            self.last_update = pygame.time.get_ticks()
            self.frame_rate  = 100
            self.frame       = 1

        def update(self):
            now = pygame.time.get_ticks()
            if now - self.last_update > self.frame_rate:
                self.last_update = now
                if self.frame >= 4:
                    self.kill()
                else:
                    self.frame += 1
                    center = self.rect.center
                    if self.frame == 2:
                        self.image = asset_images.subsurface((388, 12), (38, 38))
                    if self.frame == 3:
                        self.image = asset_images.subsurface((430, 12), (38, 38))
                    if self.frame == 4:
                        self.image = asset_images.subsurface((472, 8), (46, 46))
                    self.rect = self.image.get_rect()
                    self.rect.center = center

    def draw_ammo(screen, x, y, ammo):
        for i in range(ammo):
            img         = asset_images.subsurface((192, 42), (6, 12))
            img_rect    = img.get_rect()
            if i <= 4:
                img_rect.x  = x
                img_rect.y  = y + 17 * i
            if i > 4:
                img_rect.x = x + 10
                img_rect.y = y + 17 * (i-5)
            screen.blit(img, img_rect)

    def draw_health(screen, x, y, health):
        for i in range(health):
            img         = asset_images.subsurface((260, 36), (22, 22))
            img_rect    = img.get_rect()
            img_rect.x  = x + 22 * i
            img_rect.y  = y
            screen.blit(img, img_rect)

    def show_go_screen():
        screen.blit(FONT2.render("HELLO  ", True, (128, 128, 128)), (WIDTH/2, HEIGHT/4))
        pygame.display.flip()
        waiting = True
        while waiting:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    import Mainmenu
                    Mainmenu.menugame()
    #                pygame.quit()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        waiting = False


    ##########################################################################
    #                          In-Game Constants                             #
    ##########################################################################
    #shooting_sound  = pygame.mixer.Sound("22 Pistol.wav")

    background      = pygame.image.load("Demi Game Background.png").convert()
    background_rect = background.get_rect()
    overlay         = pygame.image.load("Demi Game Background Overlay.png").convert_alpha()
    overlay_rect    = overlay.get_rect()
    asset_images    = pygame.image.load("Demi Game Sprites.png").convert_alpha()

    FONT            = pygame.font.Font("ARCADECLASSIC.ttf", 14)
    FONT2           = pygame.font.Font("ARCADECLASSIC.ttf", 20)

    """
    all_sprites = pygame.sprite.Group()
    mobs        = pygame.sprite.Group()
    mobs2       = pygame.sprite.Group()
    mobs2spawn  = pygame.sprite.Group()
    walleye     = Eye()
    walleyelid  = Eyelid()
    bullets     = pygame.sprite.Group()
    enemybullets = pygame.sprite.Group()
    eyebullets  = pygame.sprite.Group()
    player      = Player()
    arms        = Arms()
    all_sprites.add(player)
    all_sprites.add(arms)
    all_sprites.add(walleye)
    all_sprites.add(walleyelid)
    
    ammo                = 10
    health              = 6
    score               = 0
    invincible_timer    = 45
    kills               = 0
    spawn_number        = 3
    """
    game_over           = True
    running             = True
    reloading           = False
    SHOOTING            = USEREVENT + 1
    RELOADING           = USEREVENT + 2



    ##########################################################################
    #                           Wave Spawning                                #
    ##########################################################################
    """
    #for i in range(spawn_number):
    #    m = Mob()
    #    all_sprites.add(m)
    #    mobs.add(m)
    
    for i in range(spawn_number):
    #    m   = Mob()
        m2  = Mob2()
    #    all_sprites.add(m)
        all_sprites.add(m2)
        mobs2.add(m2)
    #    mobs.add(m)
    """


    ##########################################################################
    #                               Game Loop                                #
    ##########################################################################

    while running:
        if game_over:
            show_go_screen()
            game_over   = False
            all_sprites = pygame.sprite.Group()
            mobs        = pygame.sprite.Group()
            mobs2       = pygame.sprite.Group()
            mobs2spawn  = pygame.sprite.Group()
            walleye     = Eye()
            walleyelid  = Eyelid()
            bullets     = pygame.sprite.Group()
            enemybullets = pygame.sprite.Group()
            eyebullets  = pygame.sprite.Group()
            player      = Player()
            arms        = Arms()
            all_sprites.add(player)
            all_sprites.add(arms)
            all_sprites.add(walleye)
            all_sprites.add(walleyelid)

            ammo = 10
            health = 6
            score = 0
            invincible_timer = 45
            kills = 0
            spawn_number = 3

            for i in range(spawn_number):
                m  = Mob()
                m2 = Mob2()
                #m2s = Mob2_spawn()
                all_sprites.add(m)
                all_sprites.add(m2)
                #all_sprites.add(m2s)
                #mobs2spawn.add(m2s)
                mobs2.add(m2)
                mobs.add(m)

        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                import Mainmenu
                Mainmenu.menugame()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and ammo < 10:
                    pygame.time.set_timer(RELOADING, 1000)
                    reloading = True

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
                pygame.time.set_timer(SHOOTING, 300)
                if ammo >= 1 and not reloading:
                    player.shoot()
                    ammo -= 1

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and not game_over:
                pygame.time.set_timer(SHOOTING, 0)

            if event.type == SHOOTING and ammo >= 1 and not reloading and not game_over:
                player.shoot()
                ammo -= 1

            if event.type == RELOADING:
                ammo = 10
                reloading = False
                pygame.time.set_timer(RELOADING, 0)


        all_sprites.update()



    ##########################################################################
    #                     Collision Player                                   #
    ##########################################################################

        contact = pygame.sprite.spritecollide(player, mobs2, False, pygame.sprite.collide_rect_ratio(0.8))
        if contact and invincible_timer > 45:
            for h in contact:
                h.speed = -h.speed
            health -= 1
            invincible_timer = 0

        contact2 = pygame.sprite.spritecollide(player, mobs, False, pygame.sprite.collide_rect_ratio(0.8))
        if contact2 and invincible_timer > 45:
            health -= 1
            invincible_timer = 0

        contactbullet = pygame.sprite.spritecollide(player, enemybullets, False, pygame.sprite.collide_rect_ratio(0.8))
        if contactbullet:
            for h in contactbullet:
                expl = Enemybulletexplos(h.rect.center)
                all_sprites.add(expl)
                h.kill()
                if invincible_timer > 45:
                    health -= 1
                    invincible_timer = 0

        contactbulleteye = pygame.sprite.spritecollide(player, eyebullets, False, pygame.sprite.collide_rect_ratio(0.8))
        if contactbulleteye:
            for h in contactbulleteye:
                expl = Eyebulletexplos(h.rect.center)
                all_sprites.add(expl)
                h.kill()
                if invincible_timer > 45:
                    health -= 1
                    invincible_timer = 0

        if health <= 0:
            game_over = True



    ##########################################################################
    #                     Collision bullets and mobs                         #
    ##########################################################################

        bullethit = pygame.sprite.groupcollide(bullets, mobs, False, False, pygame.sprite.collide_rect_ratio(0.8))
        for hit in bullethit:
            expl = Playerbulletexplos(hit.rect.center)
            all_sprites.add(expl)

        bullethit = pygame.sprite.groupcollide(bullets, mobs2, False, False, pygame.sprite.collide_rect_ratio(0.8))
        for hit in bullethit:
            expl = Playerbulletexplos(hit.rect.center)
            all_sprites.add(expl)


        mob1 = pygame.sprite.groupcollide(mobs, bullets, False, True, pygame.sprite.collide_rect_ratio(0.8))
        for h in mob1:
            h.health -= 1
            if h.health <= 0:
                score += 10
                h.kill()
                kills += 1

        mob2 = pygame.sprite.groupcollide(mobs2, bullets, False, True, pygame.sprite.collide_rect_ratio(0.8))
        for h in mob2:
            h.health -= 1
            if h.health <= 0:
                score += 10
                h.kill()
                kills += 1



    ##########################################################################
    #                            Wave Spawning                               #
    ##########################################################################

        if kills == spawn_number:
            kills = 0
            spawn_timer = 0

        if spawn_timer == 180:
            spawn_number += 2
            for i in range(spawn_number):
    #            m = Mob()
    #            all_sprites.add(m)
    #            mobs.add(m)
                m2 = Mob2()
                all_sprites.add(m2)
                mobs2.add(m2)


        spawn_timer += 1
        invincible_timer += 1




    ##########################################################################
    #                           Draw & Rendering                             #
    ##########################################################################

        screen.fill(BLACK)
        screen.blit(background, background_rect)
        screen.blit(asset_images.subsurface((152, 44), (26, 14)), (player.rect.x + 2, player.rect.y + 36))
        all_sprites.draw(screen)
        if reloading:
            screen.blit(FONT.render("RELOADING", True, (128, 128, 128)), (player.pos.x - 19, player.pos.y - 14))
            screen.blit(FONT.render("RELOADING", True, (255, 255, 255)), (player.pos.x - 20, player.pos.y - 15))
        screen.blit(overlay, overlay_rect)
        screen.blit(FONT2.render("SCORE  " + str(score), True, (128, 128, 128)), (679, 26))
        screen.blit(FONT2.render("SCORE  " + str(score), True, (255, 255, 255)), (680, 25))
        screen.blit(asset_images.subsurface((296, 6), (24, 72)), (700, 450))
        draw_ammo(screen, WIDTH-60, (HEIGHT/2)+147, ammo)
        draw_health(screen, 50, 20, health)
        pygame.display.flip()

    pygame.quit()