#! /usr/bin/python
import pygame, LEVEL
import time
from pygame import *
from LEVEL import *

def renzogame():
    pygame.init()

    WIN_WIDTH = 1920
    WIN_HEIGHT = 1000
    HALF_WIDTH = int(WIN_WIDTH / 2)
    HALF_HEIGHT = int(WIN_HEIGHT / 2)

    DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
    screen = pygame.display.set_mode(DISPLAY, pygame.FULLSCREEN)
    DEPTH = 32
    FLAGS = 0
    CAMERA_SLACK = 30



    pygame.mixer.music.load("Hero_s_Theme.mp3")


    red = (255,0,0)
    white =(255,255,255)

    global cameraX, cameraY
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)
    pygame.display.set_caption("WEBRUNNAH")
    timer = pygame.time.Clock()
    pygame.mixer.music.play(-1)

    SPRITESHEET = pygame.image.load('SpritesOne.png')
    Manstil2 = SPRITESHEET.subsurface((34,392),(30,44))
    Manstil2 = pygame.transform.scale(Manstil2, (70,64*2))

    Manstil3 = SPRITESHEET.subsurface((66,392),(30,44))
    Manstil3 = pygame.transform.scale(Manstil3, (70,64*2))

    Manstil4 = SPRITESHEET.subsurface((98,392),(30,44))
    Manstil4 = pygame.transform.scale(Manstil4, (70,64*2))

    Manstil5 = SPRITESHEET.subsurface((130,392),(30,44))
    Manstil5 = pygame.transform.scale(Manstil5, (70,64*2))

    Manrechts = SPRITESHEET.subsurface((34,496),(30,44))
    Manrechts = pygame.transform.scale(Manrechts, (70,64*2))

    Manrechts2 = SPRITESHEET.subsurface((66,496),(30,44))
    Manrechts2 = pygame.transform.scale(Manrechts2, (70,64*2))

    Manrechts3 = SPRITESHEET.subsurface((98,496),(30,44))
    Manrechts3 = pygame.transform.scale(Manrechts3, (70,64*2))

    Manrechts4 = SPRITESHEET.subsurface((130,496),(30,44))
    Manrechts4 = pygame.transform.scale(Manrechts4, (70,64*2))

    Manlinks = SPRITESHEET.subsurface((34,496),(30,44))
    Manlinks = pygame.transform.scale(Manrechts, (70,64*2))
    Manlinks = pygame.transform.flip(Manlinks, True, False)

    Manlinks2 = SPRITESHEET.subsurface((66,496),(30,44))
    Manlinks2 = pygame.transform.scale(Manrechts2, (70,64*2))

    Manlinks3 = SPRITESHEET.subsurface((98,496),(30,44))
    Manlinks3 = pygame.transform.scale(Manrechts3, (70,64*2))
    Manlinks3 = pygame.transform.flip(Manlinks3, True, False)

    Manlinks4 = SPRITESHEET.subsurface((130,496),(30,44))
    Manlinks4 = pygame.transform.scale(Manrechts4, (70,64*2))
    Manlinks4 = pygame.transform.flip(Manlinks4, True, False)

    Spin = SPRITESHEET.subsurface((30,158),(40,22))
    Spin = pygame.transform.scale(Spin, (64*2,64))

    Spin2 = SPRITESHEET.subsurface((30,132),(40,22))
    Spin2 = pygame.transform.scale(Spin2, (64*2,64))

    Spin3 = SPRITESHEET.subsurface((30,184),(40,22))
    Spin3 = pygame.transform.scale(Spin3, (64*2,64))












    smallfont = pygame.font.Font(None, 30)
    medfont = pygame.font.Font(None, 50)
    largefont = pygame.font.Font(None, 80)




    def text_objects(text, color, size):
        if size == "small":
            textSurface = smallfont.render(text, True, color)
        elif size == "medium":
            textSurface = medfont.render(text, True, color)
        elif size == "large":
            textSurface = largefont.render(text, True, color)

        return textSurface, textSurface.get_rect()

    def message_to_screen(msg,color, y_displace=0, size = "small"):
        textSurf, textRect = text_objects(msg,color , size)
        textRect.center = HALF_WIDTH, HALF_HEIGHT + y_displace
        screen.blit(textSurf, textRect)
        #screen_text = font.render(msg, True , color)
        #screen.blit(screen_text, [HALF_WIDTH, HALF_HEIGHT])



    def game_intro():

        intro = True
        while intro:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        intro = False
                    if event.key == pygame.K_q:
                        pygame.mixer.music.stop()
                        import Mainmenu
                        Mainmenu.menugame()
    #                   pygame.quit()
    #                    quit()
            message_to_screen("Welcome to webrunner!", red, -120, size="large")
            message_to_screen("The spiders are chasing you! Get out as fast as possible", white, -40 , size= "small")
            message_to_screen("Watch out! Don't touch the spiders and the spikes, if you touch them you die...", white, size= "small")
            message_to_screen("Use the arrows on your keyboard to move", white, 40)
            message_to_screen("Press c to start or q to quit", white, 80)
            pygame.display.update()
            timer.tick(15)


    def main():

        start_ticks=pygame.time.get_ticks()

        up = down = left = right = running = False
        #bg = Surface((32,32))
        #bg.convert()
        #bg.fill(Color("#000000"))
        bg = Surface((WIN_WIDTH,WIN_HEIGHT)).convert()
        Game_Over = False

        entities = pygame.sprite.Group()
        enemies = pygame.sprite.Group()
        player = Player(64, 32*19)
        platforms = []
        enemy = Enemy(64*14, 64*20)
        enemy2 = Enemy(64*55, 64*21)
        enemy3 = Enemy (64*170, 64*15)
        enemy4 = Enemy (64*172, 64*15)
        enemies.add(enemy)
        enemies.add(enemy2)
        enemies.add(enemy3)
        enemies.add(enemy4)


        x = y = 0
        level

        # build the level
        for row in level:
            for col in row:
                if col == "P":
                    p = Platform(x, y)
                    platforms.append(p)
                    entities.add(p)
                if col == "E":
                    e = ExitBlock(x, y)
                    platforms.append(e)
                    entities.add(e)
                if col == "S":
                    s = Enemy(x, y)
                    platforms.append(s)
                    entities.add(s)

                x += 32*2
            y += 32*2
            x = 0

        total_level_width  = len(level[0])*(32*2)
        total_level_height = len(level)*(32*2)
        camera = Camera(complex_camera, total_level_width, total_level_height)
        entities.add(player)
        entities.add(enemy)
        entities.add(enemy2)
        entities.add(enemy3)
        entities.add(enemy4)


        while 1 and not player.win and not Game_Over:
            timer.tick(60)


            for e in pygame.event.get():
                #if e.type == QUIT:
                    #raise SystemExit,
                #if e.type == KEYDOWN and e.key == K_ESCAPE:
                    #raise SystemExit,
                if e.type == KEYDOWN and e.key == K_UP:
                    up = True
                if e.type == KEYDOWN and e.key == K_DOWN:
                    down = True
                if e.type == KEYDOWN and e.key == K_LEFT:
                    left = True
                if e.type == KEYDOWN and e.key == K_RIGHT:
                    right = True
                if e.type == KEYDOWN and e.key == K_SPACE:
                    running = True

                if e.type == KEYUP and e.key == K_UP:
                    up = False
                if e.type == KEYUP and e.key == K_DOWN:
                    down = False
                if e.type == KEYUP and e.key == K_RIGHT:
                    right = False
                if e.type == KEYUP and e.key == K_LEFT:
                    left = False

            # draw background
            #for y in range(32):
                #for x in range(32):
                    #screen.blit(bg, (x * 32, y * 32))

            screen.blit(bg,(0,0))
            camera.update(player)
            seconds = (((pygame.time.get_ticks()-start_ticks-2000)/1000))
            timeplayed(seconds)
            highscore(highscore)

            # update player, draw everything else
            player.update(up, down, left, right, running, platforms,enemies)
            for e in entities:
                screen.blit(e.image, camera.apply(e))
            enemy.update(platforms)
            enemy2.update(platforms)
            enemy3.update(platforms)
            enemy4.update(platforms)

            pygame.display.update()

            while player.finish:
                message_to_screen("You lose!",red, -40, size= "large")
                message_to_screen("press c to try again or q to quit",white)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            pygame.mixer.music.stop()
                            import Mainmenu
                            Mainmenu.menugame()
    #                        pygame.quit()
    #                        quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_c:
                            main()


            #message_to_screen("You Lose, try harder next time", red)
            #pygame.display.update()


            while player.win:
                message_to_screen("You made it!", red, -40, size="large")
                message_to_screen("Your score is " + str(int(100000/seconds)), white)
                message_to_screen("If you want to improve your score press c. If you want to quit press q",white, 40)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            pygame.mixer.music.stop()
                            import Mainmenu
                            Mainmenu.menugame()
    #                        pygame.quit()
    #                        quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_c:
                            main()





    class Camera(object):
        def __init__(self, camera_func, width, height):
            self.camera_func = camera_func
            self.state = Rect(0, 0, width, height)

        def apply(self, target):
            return target.rect.move(self.state.topleft)

        def update(self, target):
            self.state = self.camera_func(self.state, target.rect)




    def simple_camera(camera, target_rect):
        l, t, _, _ = target_rect
        _, _, w, h = camera
        return Rect(-l+HALF_WIDTH, -t+HALF_HEIGHT, w, h)

    def complex_camera(camera, target_rect):
        l, t, _, _ = target_rect
        _, _, w, h = camera
        l, t, _, _ = -l+HALF_WIDTH, -t+HALF_HEIGHT, w, h

        l = min(0, l)                           # stop scrolling at the left edge
        l = max(-(camera.width-WIN_WIDTH), l)   # stop scrolling at the right edge
        t = max(-(camera.height-WIN_HEIGHT), t) # stop scrolling at the bottom
        t = min(0, t)                           # stop scrolling at the top
        return Rect(l, t, w, h)

    def highscore(highscore):
        font = pygame.font.Font(None, 40)
        text = font.render("Fastest time: 47,668", True, red)
        screen.blit(text, (64,96))

    def timeplayed(count):
        font = pygame.font.Font(None, 40)
        text = font.render("Time: " +str(count),True, red)
        screen.blit(text, (64,64))


    class Entity(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)

    class Player(Entity):
        def __init__(self, x, y):
            Entity.__init__(self)
            self.xvel = 0
            self.yvel = 0
            self.onGround = False
            self.image = Manstil2
            #self.image = Manneutraal.convert_alpha()
            #self.image = pygame.transform.scale(Manneutraal, (70,64*2))
            #self.image = Surface((32,32))
            #self.image.fill(Color("#0000FF"))
            #self.image.convert()
            self.rect= Rect(x, y, 65, 64*2)
            self.finish = False
            self.win = False
            self.faceright = True
            self.airborne = True
            self.counter = 0


        def update(self, up, down, left, right, running, platforms,enemies):
            if up:
                # only jump if on the ground
                if self.onGround: self.yvel -= 11
            if down:
                pass
            if running:
                self.xvel = 12
            if left:
                self.xvel = -8
            if right:
                self.xvel = 8
            if right and left:
                self.xvel = 0
            if not self.onGround:
                # only accelerate with gravity if in the air
                self.yvel += 0.3
                # max falling speed
                if self.yvel > 100: self.yvel = 100
            if not(left or right):
                self.xvel = 0
            # increment in x direction
            self.rect.left += self.xvel


            # do x-axis collisions
            self.collide(self.xvel, 0, platforms,enemies)
            # increment in y direction
            self.rect.top += self.yvel
            # assuming we're in the air
            self.onGround = False
            # do y-axis collisions
            self.collide(0, self.yvel, platforms, enemies)
            if self.rect.top > (64*27):
                self.win = True
            self.walkloop_right()
            self.walkloop_left()



        def collide(self, xvel, yvel, platforms,enemies):
            for p in platforms:
                if pygame.sprite.collide_rect(self, p):
                    if isinstance(p, ExitBlock):
                        self.finish = True

                    if xvel > 0:
                        self.rect.right = p.rect.left
                        print ("collide right")
                    if xvel < 0:
                        self.rect.left = p.rect.right
                        print ("collide left")
                    if yvel > 0:
                        self.rect.bottom = p.rect.top
                        self.onGround = True
                        self.yvel = 0
                    if yvel < 0:
                        self.rect.top = p.rect.bottom
                        self.yvel = 0
            for e in enemies:
                if pygame.sprite.collide_rect(self,e):
                    self.finish = True






        def walkloop_right(self):
            if self.xvel > 0 :
                if self.counter == 8:
                    self.image = Manrechts3
                    #self.image = pygame.image.load('hooman.voor2.png').convert_alpha()
                    #self.image = pygame.transform.scale(self.image, (70,64*2))
                elif self.counter == 16:
                    self.image = Manrechts4
                    #self.image = pygame.image.load('hooman.stil2.png').convert_alpha()
                    #self.image = pygame.transform.scale(self.image, (70,64*2))
                elif self.counter == 24:
                    self.image = Manrechts3
                    #self.image = pygame.image.load('hooman.achter2.png').convert_alpha()
                    #self.image = pygame.transform.scale(self.image, (70,64*2))
                elif self.counter == 32:
                    self.image = Manrechts4
                    self.counter = 0
                self.counter += 1
            if self.xvel == 0:
                if self.counter == 8:
                    self.image = Manstil2

                elif self.counter == 16:
                    self.image = Manstil3

                elif self.counter == 24:
                    self.image = Manstil4
                elif self.counter == 32:
                    self.image = Manstil5
                    self.counter = 0
                self.counter += 1
        def walkloop_left(self):

            if self.xvel == -8 :
                if self.counter == 8:
                    self.image = Manlinks3
                elif self.counter == 16:
                    self.image = Manlinks4
                elif self.counter == 24:
                    self.image = Manlinks3
                elif self.counter == 32:
                    self.image = Manlinks4
                    self.counter = 0
                self.counter += 1






    class Spritesheet:
        def __init__(self,filename):
            self.spritesheet = SPRITESHEET

        def get_image(self, x, y, width, height):
            image = pg.Surface((width, height))
            image.blit(SPRITESHEET, (0,0), (x, y, width, height))
            return image

    class Enemy (Entity):
        def __init__(self, x, y):
                Entity.__init__(self)
                #self.image = pygame.image.load('spider3.png').convert_alpha()
                self.image = Spin
                #self.image = pygame.transform.scale(self.image, (32*4, 32*2))
                # self.image = Surface((32,32))
                # self.image.fill(Color("#0000FF"))
                # self.image.convert()
                self.rect = Rect(x, y, 32 * 4, 32 * 2)
                self.yvel = 0
                self.onGround = False
                self.xvel = 4
                self.counter = 0





        def update (self,platforms):

                self.rect.left += self.xvel
                self.rect.top += self.yvel
                self.collide(self.xvel, 0, platforms)

                self.collide(0, self.yvel, platforms)
                if not self.onGround:
                    # only accelerate with gravity if in the air
                    self.yvel += 0.3
                    # max falling speed
                    if self.yvel > 100: self.yvel = 100
                self.walkloop_right()


        def collide(self, xvel, yvel, platforms):
            for p in platforms:

                if pygame.sprite.collide_rect(self, p):
                    if isinstance(p, ExitBlock):
                        pass

                    if xvel > 0:
                        self.rect.right = p.rect.left
                        self.xvel = -4
                    if xvel < 0:
                        self.rect.left = p.rect.right
                        self.xvel = 4
                    if yvel > 0:
                        self.rect.bottom = p.rect.top
                        self.onGround = True
                        self.yvel = 0
                    if yvel < 0:
                        self.rect.top = p.rect.bottom

        def walkloop_right(self):
                 if self.xvel != 0:
                    if self.counter == 8:
                        self.image = Spin
                    elif self.counter == 16:
                        self.image = Spin3
                    elif self.counter == 24:
                        self.image = Spin
                    elif self.counter == 32:
                        self.image = Spin3
                        self.counter = 0
                    self.counter += 1






    class Platform(Entity):
        def __init__(self, x, y):
            Entity.__init__(self)
            #self.image = Surface((32, 32))
            self.image = pygame.image.load('DOOS2.JPG').convert()
            self.image = pygame.transform.scale(self.image, (32*2,32*2))
            #self.image.convert()
            #self.image.fill(Color("#DDDDDD"))
            self.rect = Rect(x, y, 32*2, 32*2)

        def update(self):
            pass

    class ExitBlock(Platform):
        def __init__(self, x, y):
            Platform.__init__(self, x, y)
            self.image = pygame.image.load('spikeblock.png').convert()
            self.image = pygame.transform.scale(self.image, (32*2,32*2))
            self.rect = Rect(x, y, 64, 64)

    game_intro()
    #if __name__ == "__main__":
    main()



