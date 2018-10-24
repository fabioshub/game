import sys
import math
import pygame
import random
from pygame.locals import *
from gameobjects import Vector2

def menugame():
    MENUWIDTH = 800
    MENUHEIGHT = 600
    FPS = 60

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    pygame.init()
    pygame.mixer.init()
    menuscreen      = pygame.display.set_mode((MENUWIDTH, MENUHEIGHT), pygame.FULLSCREEN)
    pygame.display.set_caption("It's starting to look like something")
    clock       = pygame.time.Clock()

    animetime   = pygame.time.get_ticks()
    animetime2  = pygame.time.get_ticks()
    animetime3  = pygame.time.get_ticks()
    animetime4  = pygame.time.get_ticks()
    animetime5  = pygame.time.get_ticks()
    animetime6  = pygame.time.get_ticks()

    last_update = pygame.time.get_ticks()
    last_update2 = pygame.time.get_ticks()
    last_update3 = pygame.time.get_ticks()
    last_update4 = pygame.time.get_ticks()
    last_update5 = pygame.time.get_ticks()
    last_update6 = pygame.time.get_ticks()
    frame_rate  = 250
    frame       = 0
    text        = ""
    closerto1   = False
    closerto2   = False
    closerto3   = False
    playerpos   = [0, 0]
    difference  = [0, 0]

    class MenuPlayer(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.load_images()
            self.image      = self.standing_frames[1]
            self.clock      = pygame.time.Clock()
            self.rect       = self.image.get_rect()
    #        self.rect       = pygame.Rect(0, 0, 30, 22)

    # (7, 10, 16, 40)
    #        pygame.draw.rect(self.image, GREEN, self.rect)
            self.pos        = Vector2(MENUWIDTH/2, MENUHEIGHT/2)
            self.rect.x     = MENUWIDTH/2
            self.rect.y     = MENUHEIGHT/2
            self.speed      = 180

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

            if self.pos.x < 204:
                self.pos.x = 205
            if self.pos.x > 566:
                self.pos.x = 565
            if self.pos.y > 418:
                self.pos.y = 417
            if self.pos.y < 90:
                self.pos.y = 91

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
    class Cabinet1(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image  = asset_images.subsurface((262, 382), (40, 56))
            self.clock  = pygame.time.Clock()
            self.rect   = self.image.get_rect()
            self.rect.x = 276 - 40
            self.rect.y = 80
            self.timer  = 0
    class Cabinet1ON(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = asset_images.subsurface((306, 382), (40, 56))
            self.rect = self.image.get_rect()
            self.rect.topleft = (276 - 40, 80)
            self.last_update = pygame.time.get_ticks()
            self.frame_rate  = 250
            self.frame       = 0
            self.active      = True

        def update(self):
            now = pygame.time.get_ticks()
            if now - self.last_update > self.frame_rate:
                self.last_update = now
                if self.frame == 2:
                    self.active = False
                    self.kill()
                else:
                    self.frame += 1
                    center = self.rect.center
                    if self.frame == 1:
                        self.image = asset_images.subsurface((306, 382), (40, 56))
                    if self.frame == 2:
                        self.image = asset_images.subsurface((350, 382), (40, 56))
                    self.rect = self.image.get_rect()
                    self.rect.center = center
    class CabinetOutline(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image  = asset_images.subsurface((212, 450), (44, 60))
            self.clock  = pygame.time.Clock()
            self.rect   = self.image.get_rect()
            self.rect.x = 274 - 40
            self.rect.y = 78
            self.last_update = pygame.time.get_ticks()
            self.frame_rate = 0
            self.frame = 0
            self.active = True

        def update(self):
            now = pygame.time.get_ticks()
            if now - self.last_update > self.frame_rate:
                self.last_update = now
                if self.frame == 2:
                    self.active = False
                    self.kill()
                else:
                    self.frame += 1
                    center = self.rect.center
                    if self.frame == 1:
                        self.image = asset_images.subsurface((212, 450), (44, 60))
                    if self.frame == 2:
                        self.image = asset_images.subsurface((212, 450), (44, 60))
                    self.rect = self.image.get_rect()
                    self.rect.center = center
    class Cabinet2(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image  = asset_images.subsurface((262, 450), (40, 56))
            self.clock  = pygame.time.Clock()
            self.rect   = self.image.get_rect()
            self.rect.x = 327 - 40
            self.rect.y = 80
            self.timer  = 0
    class Cabinet2ON(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = asset_images.subsurface((306, 450), (40, 56))
            self.rect = self.image.get_rect()
            self.rect.topleft = (327 - 40, 80)
            self.last_update = pygame.time.get_ticks()
            self.frame_rate  = 250
            self.frame       = 0
            self.active      = True

        def update(self):
            now = pygame.time.get_ticks()
            if now - self.last_update > self.frame_rate:
                self.last_update = now
                if self.frame == 2:
                    self.active = False
                    self.kill()
                else:
                    self.frame += 1
                    center = self.rect.center
                    if self.frame == 1:
                        self.image = asset_images.subsurface((306, 450), (40, 56))
                    if self.frame == 2:
                        self.image = asset_images.subsurface((350, 450), (40, 56))
                    self.rect = self.image.get_rect()
                    self.rect.center = center
    class CabinetOutline2(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image  = asset_images.subsurface((212, 450), (44, 60))
            self.clock  = pygame.time.Clock()
            self.rect   = self.image.get_rect()
            self.rect.x = 325 - 40
            self.rect.y = 78
            self.last_update = pygame.time.get_ticks()
            self.frame_rate = 0
            self.frame = 0
            self.active = True

        def update(self):
            now = pygame.time.get_ticks()
            if now - self.last_update > self.frame_rate:
                self.last_update = now
                if self.frame == 2:
                    self.active = False
                    self.kill()
                else:
                    self.frame += 1
                    center = self.rect.center
                    if self.frame == 1:
                        self.image = asset_images.subsurface((212, 450), (44, 60))
                    if self.frame == 2:
                        self.image = asset_images.subsurface((212, 450), (44, 60))
                    self.rect = self.image.get_rect()
                    self.rect.center = center
    class Cabinet3(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image  = pygame.transform.flip(asset_images.subsurface((262, 516), (40, 62)), True, False)
            self.clock  = pygame.time.Clock()
            self.rect   = self.image.get_rect()
            self.rect.x = 520
            self.rect.y = 80
            self.timer  = 0
    class Cabinet3ON(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.transform.flip(asset_images.subsurface((306, 516), (40, 62)), True, False)
            self.rect = self.image.get_rect()
            self.rect.topleft = (520, 80)
            self.last_update = pygame.time.get_ticks()
            self.frame_rate  = 250
            self.frame       = 0
            self.active      = True

        def update(self):
            now = pygame.time.get_ticks()
            if now - self.last_update > self.frame_rate:
                self.last_update = now
                if self.frame == 2:
                    self.active = False
                    self.kill()
                else:
                    self.frame += 1
                    center = self.rect.center
                    if self.frame == 1:
                        self.image = pygame.transform.flip(asset_images.subsurface((306, 516), (40, 62)), True, False)
                    if self.frame == 2:
                        self.image = pygame.transform.flip(asset_images.subsurface((350, 516), (40, 62)), True, False)
                    self.rect = self.image.get_rect()
                    self.rect.center = center
    class CabinetOutline3(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image  = pygame.transform.flip(asset_images.subsurface((212, 514), (44, 66)), True, False)
            self.clock  = pygame.time.Clock()
            self.rect   = self.image.get_rect()
            self.rect.x = 518
            self.rect.y = 78
            self.last_update = pygame.time.get_ticks()
            self.frame_rate = 0
            self.frame = 0
            self.active = True

        def update(self):
            now = pygame.time.get_ticks()
            if now - self.last_update > self.frame_rate:
                self.last_update = now
                if self.frame == 2:
                    self.active = False
                    self.kill()
                else:
                    self.frame += 1
                    center = self.rect.center
                    if self.frame == 1:
                        self.image = pygame.transform.flip(asset_images.subsurface((212, 514), (44, 66)), True, False)
                    if self.frame == 2:
                        self.image = pygame.transform.flip(asset_images.subsurface((212, 514), (44, 66)), True, False)
                    self.rect = self.image.get_rect()
                    self.rect.center = center
    class Cabinetdud(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image  = asset_images.subsurface((218, 382), (40, 56))
            self.clock  = pygame.time.Clock()
            self.rect   = self.image.get_rect()
            self.rect.x = 250 - 40
            self.rect.y = 80
            self.timer  = 0
    class Cabinetdud2(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image  = asset_images.subsurface((218, 382), (40, 56))
            self.clock  = pygame.time.Clock()
            self.rect   = self.image.get_rect()
            self.rect.x = 301 - 40
            self.rect.y = 80
            self.timer  = 0

    class Grating(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image  = asset_images.subsurface((4, 228), (68, 48))
            self.clock  = pygame.time.Clock()
            self.rect   = self.image.get_rect()
            self.rect.x = 250
            self.rect.y = 300
            self.timer  = 0
    class GratingActive(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = asset_images.subsurface((4, 278), (68, 48))
            self.rect = self.image.get_rect()
            self.rect.topleft = (250, 300)
            self.last_update = pygame.time.get_ticks()
            self.frame_rate  = 250
            self.frame       = 0
            self.active      = True

        def update(self):
            now = pygame.time.get_ticks()
            if now - self.last_update > self.frame_rate:
                self.last_update = now
                if self.frame == 3:
                    self.active = False
                    self.kill()
                else:
                    self.frame += 1
                    center = self.rect.center
                    if self.frame == 1:
                        self.image = asset_images.subsurface((4, 328), (68, 48))
                    if self.frame == 2:
                        self.image = asset_images.subsurface((74, 228), (68, 48))
                    if self.frame == 3:
                        self.image = asset_images.subsurface((4, 328), (68, 48))
                    self.rect = self.image.get_rect()
                    self.rect.center = center
    class GratingOutline(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image  = asset_images.subsurface((74, 278), (72, 52))
            self.clock  = pygame.time.Clock()
            self.rect   = self.image.get_rect()
            self.rect.x = 248
            self.rect.y = 298
            self.last_update = pygame.time.get_ticks()
            self.frame_rate = 0
            self.frame = 0
            self.active = True

        def update(self):
            now = pygame.time.get_ticks()
            if now - self.last_update > self.frame_rate:
                self.last_update = now
                if self.frame == 2:
                    self.active = False
                    self.kill()
                else:
                    self.frame += 1
                    center = self.rect.center
                    if self.frame == 1:
                        self.image = asset_images.subsurface((74, 278), (72, 52))
                    if self.frame == 2:
                        self.image = asset_images.subsurface((74, 278), (72, 52))
                    self.rect = self.image.get_rect()
                    self.rect.center = center

    class Door(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image  = asset_images.subsurface((466, 440), (56, 70))
            self.clock  = pygame.time.Clock()
            self.rect   = self.image.get_rect()
            self.rect.x = 401
            self.rect.y = 50
            self.timer  = 0
    class DoorActive(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = asset_images.subsurface((466, 440), (56, 70))
            self.rect = self.image.get_rect()
            self.rect.topleft = (401, 50)
            self.last_update = pygame.time.get_ticks()
            self.frame_rate  = 250
            self.frame       = 0
            self.active      = True

        def update(self):
            now = pygame.time.get_ticks()
            if now - self.last_update > self.frame_rate:
                self.last_update = now
                if self.frame == 5:
                    self.active = False
                    self.kill()
                else:
                    self.frame += 1
                    center = self.rect.center
                    if self.frame == 1:
                        self.image = asset_images.subsurface((524, 368), (56, 70))
                    if self.frame == 2:
                        self.image = asset_images.subsurface((466, 368), (56, 70))
                    if self.frame == 3:
                        self.image = asset_images.subsurface((408, 368), (56, 70))
                    if self.frame == 4:
                        self.image = asset_images.subsurface((466, 368), (56, 70))
                    if self.frame == 5:
                        self.image = asset_images.subsurface((524, 368), (56, 70))
                    self.rect = self.image.get_rect()
                    self.rect.center = center
    class DoorOutline(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image  = asset_images.subsurface((524, 440), (60, 74))
            self.clock  = pygame.time.Clock()
            self.rect   = self.image.get_rect()
            self.rect.x = 399
            self.rect.y = 48
            self.last_update = pygame.time.get_ticks()
            self.frame_rate = 0
            self.frame = 0
            self.active = True

        def update(self):
            now = pygame.time.get_ticks()
            if now - self.last_update > self.frame_rate:
                self.last_update = now
                if self.frame == 2:
                    self.active = False
                    self.kill()
                else:
                    self.frame += 1
                    center = self.rect.center
                    if self.frame == 1:
                        self.image = asset_images.subsurface((524, 440), (60, 74))
                    if self.frame == 2:
                        self.image = asset_images.subsurface((524, 440), (60, 74))
                    self.rect = self.image.get_rect()
                    self.rect.center = center

    class Door2(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image  = pygame.transform.flip(asset_images.subsurface((466, 440), (56, 70)), True, False)
            self.clock  = pygame.time.Clock()
            self.rect   = self.image.get_rect()
            self.rect.x = 343
            self.rect.y = 50
            self.timer  = 0
    class DoorActive2(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.transform.flip(asset_images.subsurface((466, 440), (56, 70)), True, False)
            self.rect = self.image.get_rect()
            self.rect.topleft = (343, 50)
            self.last_update = pygame.time.get_ticks()
            self.frame_rate  = 250
            self.frame       = 0
            self.active      = True

        def update(self):
            now = pygame.time.get_ticks()
            if now - self.last_update > self.frame_rate:
                self.last_update = now
                if self.frame == 5:
                    self.active = False
                    self.kill()
                else:
                    self.frame += 1
                    center = self.rect.center
                    if self.frame == 1:
                        self.image = pygame.transform.flip(asset_images.subsurface((524, 368), (56, 70)), True, False)
                    if self.frame == 2:
                        self.image = pygame.transform.flip(asset_images.subsurface((466, 368), (56, 70)), True, False)
                    if self.frame == 3:
                        self.image = pygame.transform.flip(asset_images.subsurface((408, 368), (56, 70)), True, False)
                    if self.frame == 4:
                        self.image = pygame.transform.flip(asset_images.subsurface((466, 368), (56, 70)), True, False)
                    if self.frame == 5:
                        self.image = pygame.transform.flip(asset_images.subsurface((524, 368), (56, 70)), True, False)
                    self.rect = self.image.get_rect()
                    self.rect.center = center
    class DoorOutline2(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image  = pygame.transform.flip(asset_images.subsurface((524, 440), (60, 74)), True, False)
            self.clock  = pygame.time.Clock()
            self.rect   = self.image.get_rect()
            self.rect.x = 341
            self.rect.y = 48
            self.last_update = pygame.time.get_ticks()
            self.frame_rate = 0
            self.frame = 0
            self.active = True

        def update(self):
            now = pygame.time.get_ticks()
            if now - self.last_update > self.frame_rate:
                self.last_update = now
                if self.frame == 2:
                    self.active = False
                    self.kill()
                else:
                    self.frame += 1
                    center = self.rect.center
                    if self.frame == 1:
                        self.image = pygame.transform.flip(asset_images.subsurface((524, 440), (60, 74)), True, False)
                    if self.frame == 2:
                        self.image = pygame.transform.flip(asset_images.subsurface((524, 440), (60, 74)), True, False)
                    self.rect = self.image.get_rect()
                    self.rect.center = center


    def show_go_screen():
        menuscreen.blit(FONT2.render("USE      W      A      S      D      TO   MOVE ", True, (128, 128, 128)), ((MENUWIDTH/2 - 50 - 50), MENUHEIGHT/4))
        menuscreen.blit(FONT2.render("USE   THE   MOUSE   TO   LOOK   AROUND ", True, (128, 128, 128)), ((MENUWIDTH / 2 - 70 - 80), (MENUHEIGHT / 4)+ 20))
        menuscreen.blit(FONT2.render("AND    E    TO   INTERACT   WITH   OBJECTS", True, (128, 128, 128)), ((MENUWIDTH / 2 - 85 - 80), (MENUHEIGHT / 4) + 40))

        menuscreen.blit(FONT2.render("PRESS  SPACE  TO   START", True, (220, 25, 22)), ((MENUWIDTH / 2 - 85 - 20), (MENUHEIGHT / 4) + 200))
        pygame.display.flip()
        waiting = True
        while waiting:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type ==  pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYUP:
                    if event.key == K_SPACE:
                        waiting = False


    ##########################################################################
    #                          In-Game Constants                             #
    ##########################################################################
    #shooting_sound  = pygame.mixer.Sound("22 Pistol.wav")

    background      = pygame.image.load("Demi Game Background Menu.png").convert()
    background_rect = background.get_rect()
    overlay         = pygame.image.load("Demi Game Background Menu Overlay.png").convert_alpha()
    overlay_rect    = overlay.get_rect()
    asset_images    = pygame.image.load("Demi Game Sprites.png").convert_alpha()

    FONT            = pygame.font.Font("ARCADECLASSIC.ttf", 36)
    FONT2           = pygame.font.Font("ARCADECLASSIC.ttf", 24)


    game_over           = True
    menurunning             = True
    playing             = False



    ##########################################################################
    #                               Game Loop                                #
    ##########################################################################
    while playing:
        pygame.time.wait()


    while menurunning:
        if game_over:
            show_go_screen()
            game_over   = False
            cabinet1    = pygame.sprite.LayeredUpdates()
            cabinet1on  = pygame.sprite.LayeredUpdates()
            cabinet2    = pygame.sprite.LayeredUpdates()
            cabinet2on  = pygame.sprite.LayeredUpdates()
            cabinet3    = pygame.sprite.LayeredUpdates()
            cabinet3on  = pygame.sprite.LayeredUpdates()
            cabinetoutline = pygame.sprite.LayeredUpdates()

            grating     = pygame.sprite.LayeredUpdates()
            gratingactive = pygame.sprite.LayeredUpdates()
            gratingline = pygame.sprite.LayeredUpdates()

            door        = pygame.sprite.LayeredUpdates()
            dooractive  = pygame.sprite.LayeredUpdates()
            dooroutline = pygame.sprite.LayeredUpdates()

            door2        = pygame.sprite.LayeredUpdates()
            dooractive2  = pygame.sprite.LayeredUpdates()
            dooroutline2 = pygame.sprite.LayeredUpdates()

            all_sprites = pygame.sprite.LayeredUpdates()
            menuplayer      = MenuPlayer()
            all_sprites.add(menuplayer, layer=10)

            for i in range(1):
                c1 = Cabinet1()
                c2 = Cabinet2()
                c3 = Cabinet3()
                c4 = Cabinetdud()
                c5 = Cabinetdud2()
                gr = Grating()
                dr = Door()
                dr2 = Door2()
    #            c1on = Cabinet1ON()
                all_sprites.add(c1, layer=3)
                all_sprites.add(c4, layer=4)
                all_sprites.add(c2, layer=1)
                all_sprites.add(c5, layer=2)
                all_sprites.add(c3, layer=0)
                all_sprites.add(gr, layer=0)
                all_sprites.add(dr, layer=0)
                all_sprites.add(dr2, layer=0)
    #            all_sprites.add(c1on)
    #            all_sprites.add(c2)

                cabinet1.add(c1, layer=4)
                cabinet2.add(c2, layer=1)
                cabinet3.add(c3, layer=0)
                grating.add(gr, layer=0)
                door.add(dr, layer=0)
                door2.add(dr2, layer=0)
    #            cabinet1on.add(c1on)
    #            cabinet2.add(c2)


        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                menurunning = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e and contact and closerto1:
                    import Game
                    Game.jeffreygame()
                if event.key == pygame.K_e and contact2 and closerto2:
                    import pacman
                    pacman.hyejingame()
                if event.key == pygame.K_e and contact3 and closerto3:
                    import flappybirdhayder
                    flappybirdhayder.haydergame()
                if event.key == pygame.K_e and contact4:
                    import main
                    main.fabiogame()
                if event.key == pygame.K_e and contact5 and closerto5:
                    import DemiGame2
                    DemiGame2.demigame()
                if event.key == pygame.K_e and contact6 and closerto4:
                    import platformwebrun
                    platformwebrun.renzogame()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()




        all_sprites.update()


        if playerpos[0] < (250 + 30) and playerpos[0] > (250 - 30):
            closerto1 = True
        else:
            closerto1 = False

        if playerpos[0] < (300 + 30) and playerpos[0] > (280):
            closerto2 = True
        else:
            closerto2 = False

        if playerpos[0] < (520 + 45) and playerpos[0] > (520 - 30):
            closerto3 = True
        else:
            closerto3 = False

        if playerpos[0] < (389) and playerpos[0] > (300):
            closerto4 = True
        else:
            closerto4 = False

        if playerpos[0] < (500) and playerpos[0] > (410):
            closerto5 = True
        else:
            closerto5 = False



    ##########################################################################
    #                     Collision Player                                   #
    ##########################################################################

        contact = pygame.sprite.spritecollide(menuplayer, cabinet1, False, pygame.sprite.collide_rect_ratio(1.0))
        if contact and closerto1:
            now = pygame.time.get_ticks()
            text = "Jeffrey"
            outline = CabinetOutline()
            all_sprites.add(outline, layer=3)
            if now - last_update > frame_rate:
                last_update = now
                if now - animetime > 750:
                    anime = Cabinet1ON()
                    all_sprites.add(anime, layer=3)
                    animetime = now

        contact2 = pygame.sprite.spritecollide(menuplayer, cabinet2, False, pygame.sprite.collide_rect_ratio(1.0))
        if contact2 and closerto2:
            now = pygame.time.get_ticks()
            text = "Heyjin"
            outline = CabinetOutline2()
            all_sprites.add(outline, layer=1)
            if now - last_update2 > frame_rate:
                last_update2 = now
                if now - animetime2 > 750:
                    anime = Cabinet2ON()
                    all_sprites.add(anime, layer=1)
                    animetime2 = now

        contact3 = pygame.sprite.spritecollide(menuplayer, cabinet3, False, pygame.sprite.collide_rect_ratio(1.0))
        if contact3 and closerto3:
            now = pygame.time.get_ticks()
            text = "Hayder"
            outline = CabinetOutline3()
            all_sprites.add(outline, layer=0)
            if now - last_update3 > frame_rate:
                last_update3 = now
                if now - animetime3 > 750:
                    anime = Cabinet3ON()
                    all_sprites.add(anime, layer=0)
                    animetime3 = now

        contact4 = pygame.sprite.spritecollide(menuplayer, grating, False, pygame.sprite.collide_rect_ratio(1.0))
        if contact4:
            now = pygame.time.get_ticks()
            text = "Fabio"
            outline = GratingOutline()
            all_sprites.add(outline, layer=0)
            if now - last_update4 > frame_rate:
                last_update4 = now
                if now - animetime4 > 1000:
                    anime = GratingActive()
                    all_sprites.add(anime, layer=0)
                    animetime4 = now

    #    """
        contact5 = pygame.sprite.spritecollide(menuplayer, door, False, pygame.sprite.collide_rect_ratio(1.0))
        if contact5 and closerto5:
            now = pygame.time.get_ticks()
            text = "Demi"
            outline = DoorOutline()
            all_sprites.add(outline, layer=0)
            if now - last_update5 > frame_rate:
                last_update = now
                if now - animetime5 > 1500:
                    anime = DoorActive()
                    all_sprites.add(anime, layer=0)
                    animetime5 = now

        contact6 = pygame.sprite.spritecollide(menuplayer, door2, False, pygame.sprite.collide_rect_ratio(1.0))
        if contact6 and closerto4:
            now = pygame.time.get_ticks()
            text = "Renzo"
            outline = DoorOutline2()
            all_sprites.add(outline, layer=0)
            if now - last_update6 > frame_rate:
                last_update = now
                if now - animetime6 > 1500:
                    anime = DoorActive2()
                    all_sprites.add(anime, layer=0)
                    animetime6 = now

    #    """

        if not contact and not contact2 and not contact3 and not contact4 and not contact5 and not contact6:
            text = ""


    ##########################################################################
    #                           Draw & Rendering                             #
    ##########################################################################

        menuscreen.fill(BLACK)
        menuscreen.blit(background, background_rect)
        menuscreen.blit(asset_images.subsurface((152, 44), (26, 14)), (menuplayer.rect.x + 2, menuplayer.rect.y + 36))
        all_sprites.draw(menuscreen)
        menuscreen.blit(overlay, overlay_rect)
        menuscreen.blit(FONT.render(text, True, (128, 25, 22)), ((MENUWIDTH/2) - (len(text) * 9), 500))
        menuscreen.blit(FONT.render(text, True, (220, 25, 22)), ((MENUWIDTH/2) - (len(text) * 9) + 1, 499))
        if len(text) > 0:
            menuscreen.blit(FONT2.render("Press     E     to   Start", True, (128, 128, 128)), ((MENUWIDTH / 2) - 100, 535))
            menuscreen.blit(FONT2.render("Press     E     to   Start", True, (255, 255, 255)), ((MENUWIDTH / 2) - 100 + 1, 534))
        pygame.display.flip()

    pygame.quit()

menugame()