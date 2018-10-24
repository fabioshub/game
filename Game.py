import pygame
import random
from os import path

def jeffreygame():

    WIDTH = 500
    HEIGHT = 600

    FPS = 60

    FONT_NAME = "arial"
    HS_FILE = "highscore.txt"

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    PURPLE = (255, 0, 255)

    pygame.init()
    pygame.mixer.init()
    pygame.mouse.set_visible(True)
    running = True
    game_over = True
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    pygame.display.set_caption("GhostBuster")
    recimage = pygame.image.load("rectangle.png")
    asset_images = pygame.image.load("Demi Game Sprites.png")
    background = pygame.image.load("background 6.jpg")
    background_rect = background.get_rect()
    #player_img = pygame.image.load("Player.png")
    ghost_img = pygame.image.load("Ghost2.png")
    clock = pygame.time.Clock()
#    font_name = pygame.font.match_font("arial")
    font_name = "ARCADECLASSIC.ttf"
    pygame.mixer.music.load("backgroundsound.mp3")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(loops=-1)
    pygame.mixer.music.load("backgroundsound2.mp3")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(loops=-1)

    def draw_text(surf, text, size, x, y, color):
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surf. blit(text_surface, text_rect)

    class Player(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = asset_images.subsurface((76, 14),(30, 44))
    #        self.image = pygame.transform.scale(player_img, (60, 40))
    #        self.image.set_colorkey(WHITE)
            self.rect = self.image.get_rect()
            self.radius = 22
            self.rect.centerx = WIDTH / 2
            self.rect.bottom = HEIGHT - 10
            self.speedx = 0

        def update(self):
            self.speedx = 0
            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_LEFT]:
                self.speedx = -7
            if keystate[pygame.K_RIGHT]:
                self.speedx = 7
            self.rect.x += self.speedx
            if self.rect.right > WIDTH:
                self.rect.right = WIDTH
            if self.rect.left < 0:
                self.rect.left = 0

        def shoot(self):
            bullet = Bullet(self.rect.centerx, self.rect.top)
            all_sprites.add(bullet)
            bullets.add(bullet)

    class Mob(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = asset_images.subsurface((166, 62),(54, 68))
            self.rect = self.image.get_rect()
            self.radius = 12
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -50)
            self.speedy = random.randrange(1, 5)

        def update(self):
            self.rect.y += self.speedy
            #if self.rect.top > HEIGHT + 10:
            #Mainmenu
            #Mainmenu.menugame()
            #game_over = True
            #quit()
    class Bullet(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = asset_images.subsurface((170, 22), (14, 14))
    #        self.image = pygame.Surface((10 , 20))
    #        self.image.fill(PURPLE)
            self.rect = self.image.get_rect()
            self.rect.bottom = (y + 14)
            self.rect.centerx = x
            self.speedy = -10

        def update(self):
            self.rect.y += self.speedy
            if self.rect.bottom < 0:
                self.kill()

    class Bullethit(pygame.sprite.Sprite):
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

    class Enemyboom(pygame.sprite.Sprite):
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

    class EnemyCollider(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = recimage
            self.rect = self.image.get_rect()
            self.rect.x = 0
            self.rect.y = 610

    def show_go_screen():
        screen.fill((48, 15, 11))
        #screen.blit(background, background_rect)
        draw_text(screen, "GhostBuster", 70, (WIDTH / 2) - 2, (HEIGHT / 4) + 2, (128, 25, 22))
        draw_text(screen, "GhostBuster", 70, (WIDTH / 2), (HEIGHT / 4), (220, 25, 22))
        draw_text(screen, "Use   the   Arrow   keys   to   move", 25, (WIDTH / 2) - 1, (HEIGHT / 2) + 1, (128, 128, 128))
        draw_text(screen, "Use   the   Arrow   keys   to   move", 25, (WIDTH / 2), (HEIGHT / 2), WHITE)
        draw_text(screen, "Spacebar   to   Shoot", 25, (WIDTH / 2) - 1, (HEIGHT / 2) + 20 + 1, (128, 128, 128))
        draw_text(screen, "Spacebar   to   Shoot", 25, (WIDTH / 2), (HEIGHT / 2) + 20, WHITE)
        draw_text(screen, "Press    S    to   start", 18, (WIDTH / 2) - 1, (HEIGHT * 3 / 4) + 1, (128, 128, 128))
        draw_text(screen, "Press    S    to   start", 18, (WIDTH / 2), (HEIGHT * 3 / 4), WHITE)
        draw_text(screen, "Press    Esc    for   Main   Menu", 18, (WIDTH / 2) - 1, (HEIGHT * 4 / 5) + 1, (128, 128, 128))
        draw_text(screen, "Press    Esc    for   Main   Menu", 18, (WIDTH / 2), (HEIGHT * 4 / 5), WHITE)
        pygame.display.flip()
        waiting = True
        while waiting:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        pygame.mixer.music.stop()
                        import Mainmenu
                        Mainmenu.menugame()
                        #quit()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_s:
                        waiting = False

#    game_over = True
#    while running:
    while running:
        if game_over:
            show_go_screen()
            game_over = False
            all_sprites = pygame.sprite.Group()
            mobs = pygame.sprite.Group()
            bullets = pygame.sprite.Group()
            rectangle = EnemyCollider()
            player = Player()
            all_sprites.add(rectangle)
            all_sprites.add(player)
            for i in range(5):
                m = Mob()
                all_sprites.add(m)
                mobs.add(m)
            score = 0

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shoot()

        all_sprites.update()


        bullethit = pygame.sprite.groupcollide(bullets, mobs, False, False, pygame.sprite.collide_rect_ratio(0.8))
        for h in bullethit:
            expl = Bullethit(h.rect.center)
            all_sprites.add(expl)


        hits = pygame.sprite.groupcollide(mobs, bullets, True, True, pygame.sprite.collide_rect_ratio(0.8))
        for hit in hits:
            score += 1
            expl = Enemyboom(hit.rect.center)
            all_sprites.add(expl)
            m = Mob()
            all_sprites.add(m)
            mobs.add(m)

        hitfloor = pygame.sprite.spritecollide(rectangle, mobs, False)
        if hitfloor:
            game_over = True

        hits = pygame.sprite.spritecollide(player, mobs, False)
        if hits:
            game_over = True



        screen.fill((48, 15, 11))
        #screen.blit(background, background_rect)
        all_sprites.draw(screen)
        draw_text(screen, str(score), 18, (WIDTH / 2) - 2, 10 + 2, (128, 128, 128))
        draw_text(screen, str(score), 18, (WIDTH / 2), 10, WHITE)
        draw_text(screen, "highscore   423", 18, (WIDTH / 5) - 2, 10 + 2, (128, 128, 128))
        draw_text(screen, "highscore   423", 18, (WIDTH / 5), 10, WHITE)


        pygame.display.flip()


    pygame.mixer.music.stop()
#    pygame.quit()
#    import Mainmenu
#    Mainmenu.menugame()