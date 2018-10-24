import pygame as pg
import random
from settingshayder import *
from spriteshayder import *

def haydergame():

    # This is the game class
    pg.mixer.music.load("assets/audio/Two Steps from Hell - Heart of Courage.mp3")
    class Game:
        def __init__(self):
            # Initialize Pygame and Create Window
            self.running = True
            pg.init()
            pg.mixer.init()
            self.screen = pg.display.set_mode((WIDTH,HEIGHT), pg.FULLSCREEN)
            pg.display.set_caption(TITLE)
            self.clock = pg.time.Clock()
            pg.mixer.music.play(-1)


        def new(self):
            # Start a New Game
            self.img = 0
            self.total_frames = 0

            # Groups
            self.all_sprites = pg.sprite.Group()
            self.groundGroup = pg.sprite.Group()
            self.tubes = pg.sprite.Group()

            # Player Object
            self.player = Player(BIRD_PATH[self.img],self)
            self.all_sprites.add(self.player)

            # Player score
            self.PLAYER_SCORE = 0

            # Ground Object
            self.ground = Ground(0,550,800,50)
            self.groundGroup.add(self.ground)
            self.all_sprites.add(self.ground)

            # Tube object and properties
            TUBE_HEIGHT = random.randint(100,300)
            TUBE_GAP = random.randint(150,250)
            self.tubeTop = Tube(TUBE_X,TUBE_Y,TUBE_WIDTH,TUBE_HEIGHT,TUBE_COLOR)
            self.tubeBottom = Tube(TUBE_X,TUBE_HEIGHT+TUBE_GAP,TUBE_WIDTH,HEIGHT-50-(TUBE_HEIGHT+TUBE_GAP),TUBE_COLOR)
            self.tubes.add(self.tubeBottom)
            self.tubes.add(self.tubeTop)
            self.all_sprites.add(self.tubeTop)
            self.all_sprites.add(self.tubeBottom)

            #High scores file
            self.highscoreFile = open("assets/highscore.txt","r+")
            self.read = self.highscoreFile.readlines()




        def run(self):
            # Game Loop
            self.playing = True
            while self.playing:
                self.clock.tick(FPS)
                self.events()
                self.update()
                self.draw()

        def update(self):
            # Game Loop - Update

            self.total_frames += 1

            #This is the all sprites group
            self.all_sprites.update()

            # This spawns a new random set of tubes when the tubes reach 320px and if the tube reaches that point the bird gains point
            if self.tubeBottom.rect.x == 320:
                self.PLAYER_SCORE += 1
                POINT_SOUND.play()
                TUBE_HEIGHT = random.randint(100,300)
                TUBE_GAP = random.randint(150,250)
                self.tubeTop = Tube(TUBE_X,TUBE_Y,TUBE_WIDTH,TUBE_HEIGHT,TUBE_COLOR)
                self.tubeBottom = Tube(TUBE_X,TUBE_HEIGHT+TUBE_GAP,TUBE_WIDTH,HEIGHT-50-(TUBE_HEIGHT+TUBE_GAP),TUBE_COLOR)
                self.tubes.add(self.tubeBottom)
                self.tubes.add(self.tubeTop)
                self.all_sprites.add(self.tubeTop)
                self.all_sprites.add(self.tubeBottom)

            # This checks if the current score of the players is bigger than the one in the highscore file
            if int(self.read[0]) < int(self.PLAYER_SCORE):
                self.highscoreFile.seek(0)
                self.highscoreFile.truncate()
                self.highscoreFile.write(str(self.PLAYER_SCORE))
                self.highscoreFile.close()
                self.highscoreFile = open("assets/highscore.txt","r+")
                self.read = self.highscoreFile.readlines()



        def events(self):
            # Game Loop - Events
            for event in pg.event.get():
                # Check for closing window
                if event.type == pg.QUIT:
                    import Mainmenu
                    Mainmenu.menugame()
    #                pg.quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        self.player.vel.y = -10
                        FLAP_SOUND.play()
                        self.player.image = pg.image.load(BIRD_PATH[self.img])
                        self.img +=1
                        if self.img > 2:
                            self.img = 0


            groundCollide = pg.sprite.spritecollide(self.player,self.groundGroup,False)

            # This detects if the player has collided with the ground
            if groundCollide:
                HIT_SOUND.play()
                self.playing = False


            # This detects if the player has collided with the tube
            tubeCollide = pg.sprite.spritecollide(self.player,self.tubes,False)
            if tubeCollide:
                HIT_SOUND.play()
                self.playing = False

            if self.player.rect.y < 0:
                self.playing = False



        def  draw(self):
            # Game Loop - draw
            # Drawing
            self.screen.fill((42,13,10))
            # This draws the background
            #self.screen.blit(Background, [0,0])

            # This draws all sprites to the screen
            self.all_sprites.draw(self.screen)

            # This draws the current score to the screen
            self.display_text(("Score   " + str(self.PLAYER_SCORE)), 10 - 2, 10 + 2, 30, (128, 128, 128))
            self.display_text(("Score   " + str(self.PLAYER_SCORE)), 10, 10, 30, WHITE)

            # This draws the highscore to the screen
            self.display_text("Highscore   " + self.read[0], 200 - 2, 10 + 2, 30, (128, 128, 128))
            self.display_text("Highscore   " + self.read[0], 200, 10, 30, WHITE)

            #After everything has been drawn, flip the display
            pg.display.flip()



        def show_go_screen(self):
            # Game Over Screen
            gameStart = False
            SWOOSH_SOUND.play()
            while not gameStart:
                self.display_text("You  lost", (WIDTH / 3)+ 88, (HEIGHT / 3) + 42, 36, (128, 25, 22))
                self.display_text("You  lost", (WIDTH / 3)+ 90, (HEIGHT / 3) + 40, 36, (220, 25, 22))
                self.display_text("Press      S      to   try   again", (WIDTH/3) - 2, (HEIGHT / 2) + 2, 30, (128, 128, 128))
                self.display_text("Press      S      to   try   again", WIDTH / 3, HEIGHT / 2, 30, WHITE)
                self.display_text("or      Q      for   main   menu", (WIDTH / 3) + 8, (HEIGHT / 2) + 22, 30, (128, 128, 128))
                self.display_text("or      Q      for   main   menu", (WIDTH / 3) + 10, (HEIGHT / 2) + 20, 30, WHITE)
                pg.display.flip()
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        gameStart = True
                        self.running = False
                    if event.type == pg.KEYDOWN and event.key == pg.K_s:
                        gameStart = True
                    elif event.type == pg.KEYDOWN and event.key == pg.K_q:
                        gameStart = True
                        self.running = False

        def show_start_screen(self):
            # Game Over Screen
            gameStart = False
            while not gameStart:
                self.screen.fill((42, 13, 10))
                #self.screen.blit(Background, [0,0])
                self.display_text("Dark jumper", (WIDTH / 3) + 43, (HEIGHT / 3) + 2, 37, (128, 25, 22))
                self.display_text("Dark jumper", (WIDTH / 3) + 45, (HEIGHT / 3), 37, (220, 25, 22))
                self.display_text("Press      S      to   Start", (WIDTH/7) + 170 - 2, (HEIGHT / 2) + 2, 30, (128, 128, 128))
                self.display_text("Press      S      to   Start", (WIDTH/7) + 170, (HEIGHT / 2), 30, WHITE)
                self.display_text("Press    space    to   jump", (WIDTH/7) + 150 - 2, (HEIGHT / 2) + 30 + 2, 30, (128, 128, 128))
                self.display_text("Press    space    to   jump", (WIDTH/7) + 150, (HEIGHT / 2) + 30, 30, WHITE)

                pg.display.flip()
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        gameStart = True
                        self.running = False
                    if event.type == pg.KEYDOWN and event.key == pg.K_s:
                        gameStart = True



        def display_text(self,message,x,y,size,color):
            # This function helps me display text to the screen.
            font = pg.font.Font("ARCADECLASSIC.ttf", size)
            text = font.render(message,False,color)
            self.screen.blit(text,(x,y))
            #font = pg.font.SysFont("Comic Sans Ms", size)
            #text = font.render(message,False,color)
            #self.screen.blit(text,(x,y))

    # This is the game object
    g = Game()

    # This shows the start screen
    g.show_start_screen()

    # This loop is for the whole program
    while g.running:
        # This is a new game
        g.new()

        # This runs the game loop
        g.run()

        # This shows the game over screen
        g.show_go_screen()

    pg.mixer.music.stop()
    #import Mainmenu
    #Mainmenu.menugame()
