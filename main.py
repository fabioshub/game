import pygame as pg
import sys
from os import path
from pygame_functions import *
from settings import *
from sprites import *
from tilemap import *
import random
import time
import pyganim

def fabiogame():

    scorecounter = 0

    # vec = pg.math.Vector2

    def draw_player_health(surf, x, y):

        BAR_LENGTH = 350
        BAR_HEIGHT = 60
        fill = 1 * BAR_LENGTH
        outline_rect = pg.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
        fill_rect = pg.Rect(x, y, fill, BAR_HEIGHT)
        col = BLACK
        pg.draw.rect(surf, col, fill_rect)
        pg.draw.rect(surf, WHITE, outline_rect, 3)




    class Game:
        def __init__(self):
            pg.init()
            self.running = True
            self.screen = pg.display.set_mode((WIDTH, HEIGHT), pg.FULLSCREEN)
            self.mobmovement()
            self.clock = pg.time.Clock()
            pg.key.set_repeat(1, 150)
            self.load_data()




        def draw_text(self, text, font_name, size, color, x, y, align="nw"):
            font = pg.font.Font(font_name, size)
            text_surface = font.render(text, True, color)
            text_rect = text_surface.get_rect()
            if align == "nw":
                text_rect.topleft = (x, y)
            if align == "ne":
                text_rect.topright = (x, y)
            if align == "sw":
                text_rect.bottomleft = (x, y)
            if align == "se":
                text_rect.bottomright = (x, y)
            if align == "n":
                text_rect.midtop = (x, y)
            if align == "s":
                text_rect.midbottom = (x, y)
            if align == "e":
                text_rect.midright = (x, y)
            if align == "w":
                text_rect.midleft = (x, y)
            if align == "center":
                text_rect.center = (x, y)
            self.screen.blit(text_surface, text_rect)


        def load_data(self):
            game_folder = path.dirname(__file__)
            img_folder = path.join(game_folder, 'img')
            renzo_folder = path.join(game_folder, 'renzo')

            snd_folder = path.join(game_folder, 'snd')
            music_folder = path.join(game_folder, 'music')
            self.map = Map(path.join(game_folder, 'map.txt'))
            self.map1 = Map(path.join(game_folder, 'map1.txt'))
            self.title_font1 = "ARCADECLASSIC.ttf"
            self.title_font = path.join(img_folder, 'yas.TTF')
            self.timer_font = path.join(img_folder, 'YAAS.TTF')
            self.player_img = pg.image.load(path.join(img_folder, PLAYER_IMG)).convert_alpha()
            self.player_img = pg.transform.scale(self.player_img, (TILESIZE, TILESIZE))
            self.wall_img = pg.image.load(path.join(img_folder, WALL_IMG)).convert_alpha()
            self.wall_img = pg.transform.scale(self.wall_img, (TILESIZE, TILESIZE))
            self.door1_img = pg.image.load(path.join(img_folder, DOOR1_IMG)).convert_alpha()
            self.door1_img = pg.transform.scale(self.door1_img, (TILESIZE, TILESIZE))
            self.door2_img = pg.image.load(path.join(img_folder, DOOR2_IMG)).convert_alpha()
            self.door2_img = pg.transform.scale(self.door2_img, (TILESIZE, TILESIZE))
            self.mob_img = pg.image.load(path.join(img_folder, MOB_IMG)).convert_alpha()
            self.mob_img = pg.transform.scale(self.mob_img, (TILESIZE, TILESIZE))
            self.obj_img = pg.image.load(path.join(img_folder, OBJECTO_IMG)).convert_alpha()
            self.obj_img = pg.transform.scale(self.obj_img, (TILESIZE, TILESIZE))
            self.spritesheet = pg.image.load(path.join(img_folder, SPRITESHEETIMG)).convert_alpha()
            self.spritesheet = self.spritesheet.subsurface((174, 404),(32, 32))
            self.spritesheet = pg.transform.scale(self.spritesheet, (TILESIZE, TILESIZE))
            self.mob_img1 = pg.image.load(path.join(img_folder, SPRITESHEETIMG)).convert_alpha()
            self.mob_img1 = self.mob_img1.subsurface((30, 158),(40, 22))
            self.mob_img1 = pg.transform.scale(self.mob_img1, (TILESIZE, TILESIZE))
            self.mob_img1 = pg.transform.rotate(self.mob_img1, 90)
            self.mob_img2 = pg.image.load(path.join(img_folder, SPRITESHEETIMG)).convert_alpha()
            self.mob_img2 = self.mob_img2.subsurface((30, 132),(40, 22))
            self.mob_img2 = pg.transform.scale(self.mob_img2, (TILESIZE, TILESIZE))
            self.mob_img2 = pg.transform.rotate(self.mob_img2, 90)
            self.mob_img3 = pg.image.load(path.join(img_folder, SPRITESHEETIMG)).convert_alpha()
            self.mob_img3 = self.mob_img3.subsurface((30, 184),(40, 22))
            self.mob_img3 = pg.transform.scale(self.mob_img3, (TILESIZE, TILESIZE))
            self.mob_img3 = pg.transform.rotate(self.mob_img3, 90)


            self.gun_flashes = []
            for img in MUZZLE_FLASHES:
                self.gun_flashes.append(pg.image.load(path.join(img_folder, img)).convert_alpha())
             # Sound loading
            pg.mixer.music.load(path.join(music_folder, BG_MUSIC))
            self.effects_sounds = {}
            for type in EFFECTS_SOUNDS:
                self.effects_sounds[type] = pg.mixer.Sound(path.join(snd_folder, EFFECTS_SOUNDS[type]))
            self.weapon_sounds = {}
            self.weapon_sounds['gun'] = []
            for snd in WEAPON_SOUNDS_GUN:
                self.weapon_sounds['gun'].append(pg.mixer.Sound(path.join(snd_folder, snd)))
            self.zombie_moan_sounds = []
            for snd in ZOMBIE_MOAN_SOUNDS:
                s = pg.mixer.Sound(path.join(snd_folder, snd))
                s.set_volume(0.2)
                self.zombie_moan_sounds.append(s)
            self.player_hit_sounds = []
            for snd in PLAYER_HIT_SOUNDS:
                self.player_hit_sounds.append(pg.mixer.Sound(path.join(snd_folder, snd)))
            self.zombie_hit_sounds = []
            for snd in ZOMBIE_HIT_SOUNDS:
                self.zombie_hit_sounds.append(pg.mixer.Sound(path.join(snd_folder, snd)))

        def new(self):
            # initialize all variables and do all the setup for a new game
            self.all_sprites = pg.sprite.Group()
            self.walls = pg.sprite.Group()
            self.mobs = pg.sprite.Group()
            self.players = pg.sprite.Group()
            self.collect = pg.sprite.Group()
            self.exitblocks = pg.sprite.Group()
            self.openblocks = pg.sprite.Group()

            self.bg = pg.sprite.Group()
            self.walls10 = pg.sprite.Group()
            self.items = pg.sprite.Group()

            spawn_time = pg.time.get_ticks()
            randomx = randint(6, 47)
            randomy = randint(79, 87)
            randomy2 = randint(63, 70)
            randomy3 = randint(38, 46)
            randomy4 = randint(21, 28)
            lista = [randomy, randomy2, randomy3, randomy4]
            layera = random.choice(lista)
            self.objecto = objecto(self, randomx, layera)



            for row, tiles in enumerate(self.map.data):
                for col, tile in enumerate(tiles):
                    if tile == '2':
                        Wall(self, col, row)
                    if tile == '1':
                        Wall(self, col, row)
                    if tile == 'P':
                        self.player = Player(self, col, row)
                    if tile == 'A':
                        self.mob = mob(self, col, row)
                    if tile == '3':
                        self.wallmoving = wallmoving(self, col, row)
                    # if tile == 'B':
                    #     self.mob1 = Mob(self, col, row)
                    # if tile == 'C':
                    #     self.mob2 = Mob(self, col, row)
                    # if tile == 'D':
                    #     self.mob3 = Mob(self, col, row)

                    # if tile == 'O':
                    #     self.objecto = objecto(self, col, row)
                    if tile == 'E':
                        self.exitblock = exitblock(self, col, row)
                    if tile == 'Q':
                        self.door1 = door1(self, col, row)
                    if tile == 'W':
                        self.door2 = door2(self, col, row)

            self.camera = Camera(self.map.width, self.map.height)







        def run(self):
            # game loop - set self.playing = False to end the game
            self.startuitleg()
            self.playing = True
            self.scorecounter = 0
            pg.mixer.music.play(loops=-1)
            while self.playing:
                self.dt = self.clock.tick(FPS) / 1000
                self.events()
                self.update()
                self.draw()

                #self.spawnobj()


        def startuitleg(self):
            pg.display.set_caption(TITLE)
            self.screen.fill(DARKGREY)
#            self.draw_text("Voordat je begint: ", self.title_font1, 70, WHITE,
#                           WIDTH / 2, HEIGHT* 1 / 3, align="center")
            self.draw_text("Doors   behind   you    are   closed", self.title_font1, 30, WHITE,
                            WIDTH / 2, HEIGHT* 2 / 4, align="center")
            self.draw_text("find   the   key   and   return", self.title_font1, 20, WHITE,
                           WIDTH / 2, (HEIGHT * 3 / 5 + 20) - 20, align="center")
            self.draw_text("open    up   the    way    to    make    progress", self.title_font1, 20, WHITE,
                           WIDTH / 2, (HEIGHT * 2 / 3 + 20) - 50, align="center")

            self.draw_text("Use   the   arrow   keys   to    move", self.title_font1, 20, WHITE,
                           WIDTH / 2, (HEIGHT * 3 / 5 + 20) + 25, align="center")
            self.draw_text("to   Dodge   enemies", self.title_font1, 20, WHITE,
                           WIDTH / 2, (HEIGHT * 2 / 3 + 20) - 5, align="center")

            self.draw_text("press    s    to   start", self.title_font1, 20, RED,
                           WIDTH / 2, (HEIGHT * 4 / 5 + 20) - 40, align="center")
            pg.display.flip()
            waiting = True
            while waiting:
                self.clock.tick(FPS)
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        waiting = False
                        pg.quit()
                        sys.exit()
                        #self.quit()
                    if keyPressed('s'):
                        waiting = False
                    if keyPressed('esc'):
                        self.quit()

            """
            pg.display.flip()
            waiting = True
            while waiting:
                self.clock.tick(FPS)
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        waiting = False
                        self.quit()
                    if keyPressed('right'):
                        waiting = False
                        self.effects_sounds['health_up'].play()

                        self.startuitleg2()
                    if keyPressed('esc'):
                        self.quit()
            """
        """    
        def startuitleg2(self):
            pg.display.set_caption(TITLE)
            self.screen.fill(DARKGREY)
            self.draw_text("Zodra je langs de wormen bent", self.title_font1, 70, WHITE,
                           WIDTH / 2, HEIGHT* 1 / 3, align="center")
            self.draw_text("zal het level herstarten", self.title_font1, 60, WHITE,
                            WIDTH / 2, HEIGHT* 2 / 4, align="center")
            self.draw_text("Met de sleutel op een andere locatie ", self.title_font1, 40, WHITE,
                           WIDTH / 2, HEIGHT * 3 / 5 + 20, align="center")
            self.draw_text("Hoe meer je er vindt, hoe hoger je score", self.title_font1, 40, WHITE,
                           WIDTH / 2, HEIGHT * 2 / 3 + 20, align="center")
            self.draw_text("DRUK OP DE SPATIEBAR OM TE STARTEN OM TE BEGINNEN", self.title_font1, 40, RED,
                           WIDTH / 2, HEIGHT * 4 / 5 + 20, align="center")
            pg.display.flip()
            waiting = True
            while waiting:
                self.clock.tick(FPS)
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        waiting = False
                        self.quit()
                    if keyPressed('space'):
                        waiting = False
                    if keyPressed('esc'):
                        self.quit()
        """

        def quit(self):
            #self.playing = False
            #self.running = False
            #print(self.running)
            pg.key.set_repeat()
            pygame.mixer.music.stop()
            import Mainmenu
            Mainmenu.menugame()
#            pg.quit()
#            sys.exit()

        def update(self):
            # update portion of the game loop
            self.all_sprites.update()
            self.variex = False


            # mobs hit player
            hits = pg.sprite.spritecollide(self.player, self.mobs, False, collide_hit_rect)
            for hit in hits:
                # self.player.health -= MOB_DAMAGE
                hit.vel = vec(0, 0)
                # if self.player.health <= 0:
                pass
            if hits:
                # self.player.pos += vec(20, 0).rotate(-hits[0].rot)
                # self.mob.kill()
                self.new()
                self.quitscreen()
            hits1 = pg.sprite.spritecollide(self.player, self.collect, False, collide_hit_rect)
            for hit in hits1:
                pass
            if hits1:
                self.effects_sounds['health_up'].play()
                self.objecto.kill()
                self.door1.kill()
                self.door2.kill()


            hits2 = pg.sprite.spritecollide(self.player, self.exitblocks, False, collide_hit_rect)
            for hit in hits2:
                pass
            if hits2:
                self.new()

                self.scorecounter += 1

            self.camera.update(self.player)

        def textincorner(self):
            self.draw_text("1", self.title_font1, 50, WHITE,
                            WIDTH / 2, HEIGHT * 2 / 3, align="center")
            pg.display.flip()

        def mobmovement(self):
            self.loopy = pygame.USEREVENT + 1
            pygame.time.set_timer(self.loopy, 140)
            self.loopx = pygame.USEREVENT + 2
            pygame.time.set_timer(self.loopx, 160)
            self.xnieuw = 0
            self.ani = pygame.USEREVENT + 3
            pygame.time.set_timer(self.ani, 800)
            self.ani1 = pygame.USEREVENT + 4
            pygame.time.set_timer(self.ani1, 500)
            self.ani10 = pygame.USEREVENT + 5
            pygame.time.set_timer(self.ani10, 3000)
            self.ynieuw = 0


        def draw_grid(self):
            for x in range(0, WIDTH, TILESIZE):
                pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
            for y in range(0, HEIGHT, TILESIZE):
                pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

        def draw(self):
            pg.display.set_caption(TITLE)
            self.screen.fill(ROOD)
            # self.draw_grid()
            # self.all_sprites.draw(self.screen)
            for sprite in self.all_sprites:
                self.screen.blit(sprite.image, self.camera.apply(sprite))
            #draw_player_health(self.screen, 10, 10)
            self.score()
            if self.variex:
                self.goback()
            # if self.new():
            #     self.draw_text("self.clock.get_fps())", self.title_font, 50, WHITE,
            #                     WIDTH * 1/8, HEIGHT * 1/8, align="center")


            pg.display.flip()

        def events(self):
            # catch all events here
            #sike = 0
            for event in pg.event.get():
                if keyPressed('p'):
                    self.show_go_screen()
                if event.type == self.ani1 and self.ynieuw <=20:
                    # print('hou je bek')

                    self.count = (random.randint(1, 86))
                    for x in range((random.randint(1, 15)), (random.randint(15, 30))):
                        self.wall1 = wall1(self, x, self.count)
                    self.ynieuw += 1

                if event.type == self.ani1 and self.ynieuw >= 100 and self.ynieuw <= 200:
                    # print('hou je bek')

                    self.count = (random.randint(1, 86))
                    for x in range((random.randint(30, 45)), (random.randint(45, 63))):
                        self.wall1 = wall1(self, x, self.count)
                    self.ynieuw += 1
                # if event.type == self.ani1 and self.ynieuw <=5:
                if event.type == self.ani1 and self.ynieuw >= 200 and self.ynieuw <= 300:
                    # print('hou je bek11')
                    self.count = (random.randint(1, 57))
                    for y in range((random.randint(1, 28)), (random.randint(28, 48))):
                        self.wall1 = wall1(self, self.count, y)
                    self.ynieuw += 1
                if event.type == self.ani1 and self.ynieuw >= 300 and self.ynieuw <= 400:
                    # print('hou je bakkes')
                    self.count = (random.randint(1, 57))
                    for y in range((random.randint(48, 68)), (random.randint(68, 80))):
                        self.wall1 = wall1(self, self.count, y)
                    self.ynieuw += 1
                if self.ynieuw > 400:
                    self.ynieuw = 0

                # if event.type == self.ani10:

                    # print('dikke teef')

                # if event.type == self.loopy and self.xnieuw <= 5:
                #     print ("1")
                #     self.mob.move(dx=1)
                #     self.mob.move(dx=(random.randint(-1, 1)))
                #     # self.mob.move(dy=1)
                #     # self.mob.move(dy=(random.randint(0, 1)))
                #     # self.mob1.move(dx=-1)
                #     # self.mob1.move(dx=(random.randint(-1, 0)))
                #     self.mob1.move(dy=1)
                #     self.mob1.move(dy=(random.randint(0, 1)))
                #     self.mob2.move(dx=-1)
                #     self.mob2.move(dx=(random.randint(-1, 0)))
                #     self.mob3.move(dy=1)
                #     self.mob3.move(dy=(random.randint(0, 1)))
                #     self.xnieuw += 1
                #
                # if event.type == self.loopx and self.xnieuw >= 5 and self.xnieuw <= 10:
                #     print ("2")
                #     # self.mob.move(dx=-1)
                #     # self.mob.move(dx=(random.randint(-1, 0)))
                #     self.mob.move(dy=-1)
                #     self.mob.move(dy=(random.randint(-1, 0)))
                #     self.mob1.move(dx=1)
                #     self.mob1.move(dx=(random.randint(0, 1)))
                #     # self.mob1.move(dy=-1)
                #     # self.mob1.move(dy=(random.randint(-1, 0)))
                #     self.mob3.move(dx=-1)
                #     self.mob3.move(dx=(random.randint(-1, 0)))
                #     self.mob2.move(dy=1)
                #     self.mob2.move(dy=(random.randint(-1, 1)))
                #     self.xnieuw += 1
                #
                #
                #
                # if event.type == self.loopx and self.xnieuw >= 10 and self.xnieuw <= 15:
                #     print ("3")
                #     self.mob.move(dx=-1)
                #     self.mob.move(dx=(random.randint(-1, 0)))
                #     # self.mob.move(dy=-1)
                #     # self.mob.move(dy=(random.randint(-1, 0)))
                #     # self.mob1.move(dx=1)
                #     # self.mob1.move(dx=(random.randint(0, 1)))
                #     self.mob1.move(dy=-1)
                #     self.mob1.move(dy=(random.randint(-1, 0)))
                #     self.mob2.move(dx=1)
                #     self.mob2.move(dx=(random.randint(-1, 1)))
                #     self.mob3.move(dy=-1)
                #     self.mob3.move(dy=(random.randint(-1, 0)))
                #     self.xnieuw += 1
                #
                # if event.type == self.loopx and self.xnieuw >= 15 and self.xnieuw <= 20:
                #     print ("4")
                #     # self.mob.move(dx=-1)
                #     # self.mob.move(dx=(random.randint(-1, 0)))
                #     self.mob.move(dy=1)
                #     self.mob.move(dy=(random.randint(-1, 1)))
                #     self.mob1.move(dx=-1)
                #     self.mob1.move(dx=(random.randint(-1, 0)))
                #     # self.mob1.move(dy=-1)
                #     # self.mob1.move(dy=(random.randint(-1, 0)))
                #     self.mob3.move(dx=1)
                #     self.mob3.move(dx=(random.randint(0, 1)))
                #     self.mob2.move(dy=-1)
                #     self.mob2.move(dy=(random.randint(-1, 0)))
                #     self.xnieuw += 1
                # # if event.type == self.loopy and self.xnieuw >= 20 and self.xnieuw <= 25:
                # #     print('ja')
                # if self.xnieuw > 20:
                #     self.xnieuw = 0

                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if keyPressed('c'):
                    self.goback()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        #import startmenu
                        self.quit()



        def score(self):

            counter = str(self.scorecounter)
            # prit (counter)
            draw_player_health(self.screen, 10, HEIGHT / 17 - 30)
            self.draw_text("score   ", self.title_font1, 50, WHITE,
                           WIDTH / 7, HEIGHT / 17, align="center")
            self.draw_text(counter, self.title_font1, 50, RED,
                           WIDTH * 3 / 10, HEIGHT / 17, align="center")
            # self.wait_for_key()


        def goback(self):
            draw_player_health(self.screen, 10, HEIGHT / 15 - 30)
            self.draw_text("Ga terug naar de deur!", self.title_font1, 20, WHITE,
                           WIDTH / 6, HEIGHT / 7, align="center")
            pg.display.flip()



        def show_death_screen(self):
            self.draw_text("toets o om opnieuw te beginnen", self.title_font1, 50, WHITE,
                           WIDTH / 2, HEIGHT * 2 / 3, align="center")

            pg.display.flip()
            self.wait_for_key()
            g.new()
            g.run()

        def show_go_screen(self):
            self.draw_text("PAUZE", self.title_font1, 100, RED,
                           WIDTH / 2, HEIGHT * 1 / 3, align="center")
            self.draw_text("toets de spatiebar om te hervatten", self.title_font1, 50, WHITE,
                           WIDTH / 2, HEIGHT * 2 / 3, align="center")

            pg.display.flip()
            waiting = True
            while waiting:
                self.clock.tick(FPS)
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        waiting = False
                        #self.quit()
                        pg.quit()
                        sys.exit()
                    if keyPressed('space'):
                        waiting = False


        def quitscreen(self):
            self.screen.fill(DARKGREY)
            self.draw_text("GAME OVER!", self.title_font1, 50, WHITE,
                           WIDTH / 2, HEIGHT / 3, align="center")
            self.draw_text("YOUR   SCORE   IS", self.title_font1, 50, WHITE,
                           WIDTH / 2, (HEIGHT / 3) + 35, align="center")
            self.draw_text(str(self.scorecounter), self.title_font1, 150, RED,
                           WIDTH / 2, HEIGHT / 2, align="center")
            self.draw_text("PRESS   SPACE   TO   RETURN   TO    MAIN   MENU", self.title_font1, 50, WHITE,
                           WIDTH / 2, HEIGHT * 2 / 3, align="center")
            pg.display.flip()
            self.wait_for_key()




        def wait_for_key(self):
            # pg.event.wait()
            waiting = True
            while waiting:
                self.clock.tick(FPS)
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        waiting = False
                        #self.quit()
                        pg.quit()
                        sys.exit()
                    if keyPressed('space'):
                        waiting = False
                        self.quit()
                    # if keyPressed('space'):
                    #     waiting = False
                    #     self.new()



    # create the game object
    g = Game()
    # g.show_start_screen()
    while g.running:
        g.new()
        g.run()

        #g.show_go_screen()

    pg.mixer.music.stop()
