#This program was written by Afsah Rabbani
#Cat's Big Adventure ICS4U Culminating Game

import pygame, os, random, time
from pygame.locals import *

#importing vectors to use for x and y motion
vec = pygame.math.Vector2

#set up the window
WINDOWWIDTH = 1000
WINDOWHEIGHT = 775

#set up the colors
BLACK = (0, 0, 0)
DARKGREEN = (0, 100, 0)

#properties of player movement: acceleration, friction, gravity
PLAYERACC = 0.7
PLAYERFRIC = -0.12
PLAYERGRAV = 0.8

#Platform List

PLIST = [(850, 735, "rblock.png"), (960, 740, "lblock.png"), (845, 600, "tree.png"), (630, 680, "rblock.png"),
         (740, 685, "lblock.png"), (470, 590, "littleblock.png"), (290, 500, "lfloatblock.png"),
         (160, 500, "rfloatblock.png"), (40, 605, "littleblock.png"),
         (415, 415, "floatrock.png"), (510, 340, "floatrock.png"), (605, 265, "floatrock.png"),
         (700, 190, "floatrock.png"), (605, 115, "flipfloatrock.png"), (517, 115, "lbridge.png"),
         (417, 116, "midbridge.png"), (329, 116, "rbridge.png"), (214, 116, "floatblock.png"),
         (84, 30, "floatrock.png"), (214, -70, "littleblock.png"), (350, -160, "floatrock.png"),
         (500, -260, "rfloatblock.png"), (610, -260, "lfloatblock.png"), (740, -360, "littleblock.png"),
         (875, -465, "littleblock.png"), (730, -560, "littleblock.png"), (642, -560, "lbridge.png"),
         (542, -560, "midbridge.png"), (454, -560, "rbridge.png"), (294, -555, "rblock.png"),
         (404, -547, "lblock.png"), (234, -493, "grassrock.png"), (174, -493, "grassrock.png"),
         (114, -493, "grassrock.png"), (112, -633, "tree.png"), (295, -735, "floatrock.png"),
         (375, -850, "floatrock.png"), (475, -960, "floatrock.png"), (645, -950, "rfloatblock.png"),
         (775, -950, "lfloatblock.png"), (645, -998, "floatrock.png"), (690, -1041, "stairblock.png"),
         (725, -1131, "caveblock.png"), (820, -1041, "stairblock.png"), (845, -998, "flipfloatrock.png"),
         (600, -1225, "stairblock.png"), (500, -1325, "stairblock.png"), (400, -1425, "stairblock.png"),
         (245, -1525, "caveblock.png"), (245, -1400, "stairblock.png"), (300, -1400, "stairblock.png"),
         (145, -1500, "stairblock.png"), (100, -1500, "stairblock.png"), (400, -1625, "stairblock.png"),
         (500, -1715, "floatrock.png"), (650, -1665, "rfloatblock.png"), (780, -1665, "lfloatblock.png"),
         (740, -1825, "tree.png"), (900, -1910, "grassrock.png"), (750, -2000, "grassrock.png"),
         (600, -2090, "grassrock.png"), (430, -2090, "grassrock.png"), (260, -2090, "grassrock.png"),
         (90, -2215, "littleblock.png"), (260, -2300, "floatrock.png"), (310, -2300, "rbridge.png"),
         (398, -2300, "midbridge.png"), (486, -2300, "lbridge.png"), (574, -2300, "rbridge.png"),
         (662, -2300, "midbridge.png"), (750, -2300, "lbridge.png")]

#Boss Platform

BOSSPLAT = [(260, -2300, "floatrock.png")]

#Next level platform

NEXTLEVPLAT = [(725, -1131, "caveblock.png")]

#End game platform

ENDGAMEPLAT = [(828, -2400, "caveblock.png")]

#Enemy List

ELIST = [(160, 435, "enemy1.png", 350), (280, 50, "enemy1.png", 605), (500, -330, "enemy1.png", 710),
         (424, -635, "enemy1.png", 730), (225, -1600, "enemy1.png", 305), (650, -1730, "enemy1.png", 710),
         (272, -1590, "flame.png", 650), (310, -2750, "boss.png", 550), (200, -2350, "flame.png", 550),
         (550, -2350, "flame.png", 800)]

#Coin list

COINLIST = [(691, 650, "coin.png"), (495, 555, "coin.png"), (180, 465, "coin.png"),
            (240, 465, "coin.png"), (300, 465, "coin.png"), (360, 465, "coin.png"),
            (63, 570, "coin.png"), (428, 375, "coin.png"), (523, 305, "coin.png"),
            (618, 230, "coin.png"), (713, 155, "coin.png"), (618, 75, "coin.png"),
            (400, 75, "coin.png"), (510, 75, "coin.png"), (260, 75, "coin.png"),
            (103, -5, "coin.png"), (242, -115, "coin.png"), (369, -200, "coin.png"),
            (525, -305, "coin.png"), (600, -305, "coin.png"), (675, -305, "coin.png"),
            (768, -405, "coin.png"), (903, -505, "coin.png"), (758, -600, "coin.png"),
            (570, -600, "coin.png"), (355, -595, "coin.png"), (314, -780, "coin.png"),
            (394, -895, "coin.png"), (494, -1005, "coin.png"), (755, -1176, "coin.png"),
            (605, -1270, "coin.png"), (505, -1375, "coin.png"), (405, -1465, "coin.png"),
            (275, -1577, "coin.png"), (150, -1550, "coin.png"), (105, -1550, "coin.png"),
            (405, -1667, "coin.png"), (519, -1767, "coin.png"), (760, -1847, "coin.png"),
            (912, -1955, "coin.png"), (762, -2045, "coin.png"), (612, -2135, "coin.png"),
            (442, -2135, "coin.png"), (272, -2135, "coin.png"), (116, -2260, "coin.png"),
            (338, -2345, "coin.png"), (426, -2345, "coin.png"), (514, -2345, "coin.png"),
            (602, -2345, "coin.png"), (690, -2345, "coin.png"), (778, -2345, "coin.png")]


#set up the frame rate
FRAMERATE = 50

def terminate():
    """ This function is called when the user closes the window or presses ESC """
    pygame.quit()
    os._exit(1)

def drawText(text, font, surface, x, y, textcolour):
    """ Draws the text on the surface at the location specified """
    textobj = font.render(text, 1, textcolour)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def display_menu(windowSurface):
    """ Displays the menu so the user can choose help or start """
    image = pygame.image.load("intro.png")
    windowSurface.blit(image, [0,0])
    pygame.display.update()
    helps = True #controls the help screen display 
    
    while helps:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

            elif event.type == KEYDOWN:
                if event.key == ord('2'):
                    HelpPage(windowSurface)

                #press back to go back to main menu
                elif event.key == K_BACKSPACE:
                    windowSurface.blit(image, [0,0])
                    pygame.display.update()

                #user presses 1 to start game
                elif event.key == ord('1'):
                    helps = False

            elif event.type == KEYUP:
                if event.key == K_ESCAPE:
                    terminate()
    

def HelpPage(windowSurface):
    """Displays the instructions"""
    image = pygame.image.load("help.png")
    windowSurface.blit(image, [0,0])
    pygame.display.update()

def GameOverScreen(windowSurface, filename):
    """Displays game over or game end screen"""
    image = pygame.image.load(filename)
    windowSurface.blit(image, [0,0])
    pygame.display.update()

def DrawLives(windowSurface, x, y, lives):
    """Displays lives on the screen"""
    for i in range(lives): #blits 3 live images on screen
        image = pygame.image.load("heart.png")
        windowSurface.blit(image, [x+i*40,y])

def CoinCount(windowSurface, coincount):
    """Displays number of coins collected on the screen"""
    image = pygame.image.load("coin.png")
    windowSurface.blit(image, [30, 10])
    basicFont = pygame.font.SysFont("Comic Sans MS", 25)
    if len(str(coincount)) > 1: #Position number differently based on size
        drawText(str(coincount), basicFont, windowSurface, 33, 50, DARKGREEN)
    else:
        drawText(str(coincount), basicFont, windowSurface, 41, 50, DARKGREEN)

def NextLevel(windowSurface, level):
    """Displays current level or BOSS on screen"""
    basicFont = pygame.font.SysFont("Comic Sans MS", 25)
    nexttext = "Level " + str(level)
    bosstext = "BOSS"
    if level < 3:
        drawText(nexttext, basicFont, windowSurface, 480, 10, DARKGREEN)
    elif level == 3:
        drawText(bosstext, basicFont, windowSurface, 480, 10, DARKGREEN)


def load_image(filename):
    """Load an image from a file.  Return the image and corresponding rectangle"""
    image = pygame.image.load(filename)
    image = image.convert_alpha()
    return image, image.get_rect()

class Player(pygame.sprite.Sprite):
    """The player controlled by the user"""
    def __init__(self, movespeed):  
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("cat1.png")
        self.flipped = True

        #Position the player in the centre of the screen
        self.rect.centerx = 50
        self.rect.centery = 200
        
        # set up movement variables
        self.moveLeft = False
        self.moveRight = False
        self.moveUp = False
        self.moveDown = False
        self.movespeed = movespeed

        #speed vectors
        self.velx = 0
        self.vely = 0
        #position vector
        self.pos = vec(950, 700)
        
        #defining velocity and acceleration
        self.vel = vec(0,0)
        self.acc = vec(0,0)

        self.grounded = False #when player is standing on platform
        self.lives = 3 #Number of lives
        self.hidetimer = pygame.time.get_ticks() #used to hide player upon enemy collision
        self.wait = 60 #Timer for collision detection and lives
        self.coincount = 0 #coins collected
        self.level = 1 #level


        #Animation variables
        self.walkingr = False
        self.walkingl = False
        self.jumping = False
        #Animation timing variables
        self.current_frame = 0
        self.last_update = 0


    def load_images(self):
        """Loads the image for each frame of player animation"""
        self.standing_frame = [load_image("cat1.png")]
        self.walk_frames_r = [load_image("cat2.png"), load_image("cat3.png"),
                              load_image("cat4.png")]


    def jump(self):
        """Allows the user to jump by setting a vertical velocity upwards"""
        if self.grounded == True:
            self.vel.y = -13
        
    def update(self):
        
        """Change the position of the player's rectangle"""
        #calling animate function
        self.animate()
        #set vertical acceleration according to gravity constant
        self.acc = vec(0,PLAYERGRAV)
        
        #setting acceleration based on direction
        if self.moveLeft and self.rect.left > 0:
            self.acc.x = -PLAYERACC
        elif self.moveRight and self.rect.right < WINDOWWIDTH:
            self.acc.x = PLAYERACC

        #accelerate in x direction and slow down due to friction
        self.acc.x += self.vel.x*PLAYERFRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 *self.acc

        #position referenced from bottom of player
        self.rect.midbottom = self.pos


    def animate(self):
        """Animates the player by setting image for each movement"""
        #current time
        now = pygame.time.get_ticks()

        #when walking right
        if self.walkingr:
            #if enough time has passed, change image
            if now - self.last_update > 350:
                self.last_update = now
                if self.current_frame == 0:
                    bottom = self.rect.bottom
                    self.image, self.rect = load_image("cat2.png")
                    self.rect.bottom = bottom
                    self.current_frame = 1
                elif self.current_frame == 1:
                    bottom = self.rect.bottom
                    self.image, self.rect = load_image("cat3.png")
                    self.rect.bottom = bottom
                    self.current_frame = 2
                elif self.current_frame == 2:
                    bottom = self.rect.bottom
                    self.image, self.rect = load_image("cat2.png")
                    self.rect.bottom = bottom
                    self.current_frame = 3
                elif self.current_frame == 3:
                    bottom = self.rect.bottom
                    self.image, self.rect = load_image("cat4.png")
                    self.rect.bottom = bottom
                    self.current_frame = 0

        #when walking left
        elif self.walkingl:
            #if enough time has passed, change image
            if now - self.last_update > 350:
                self.last_update = now
                if self.current_frame == 0:
                    bottom = self.rect.bottom
                    self.image, self.rect = load_image("cat2.png")
                    self.image = pygame.transform.flip(self.image, True, False)
                    self.rect.bottom = bottom
                    self.current_frame = 1
                elif self.current_frame == 1:
                    bottom = self.rect.bottom
                    self.image, self.rect = load_image("cat3.png")
                    self.image = pygame.transform.flip(self.image, True, False)
                    self.rect.bottom = bottom
                    self.current_frame = 2
                elif self.current_frame == 2:
                    bottom = self.rect.bottom
                    self.image, self.rect = load_image("cat2.png")
                    self.image = pygame.transform.flip(self.image, True, False)
                    self.rect.bottom = bottom
                    self.current_frame = 3
                elif self.current_frame == 3:
                    bottom = self.rect.bottom
                    self.image, self.rect = load_image("cat4.png")
                    self.image = pygame.transform.flip(self.image, True, False)
                    self.rect.bottom = bottom
                    self.current_frame = 0

        #when standing still          
        elif not self.walkingr and not self.walkingl:
            bottom = self.rect.bottom
            self.image, self.rect = load_image("cat1.png")
                
    def hide(self):
        """Hides the player upon hitting the enemy"""
        self.rect.center = (WINDOWWIDTH/2, WINDOWHEIGHT -2000)
      

class Platform(pygame.sprite.Sprite):
    """This class creates platforms"""
    def __init__(self, xpos, ypos, filename):
        """gets image and position coordinates and creates a platform"""
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename)
        self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos

class Enemy(pygame.sprite.Sprite):
    """This class creates the enemy"""
    def __init__(self, xpos, ypos, filename, end):
        """constructor creates enemy and sets movement variables"""
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename)
        self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        self.end = end #end of enemy path
        self.path = [self.rect.x, self.end] #enemy path
        self.vel = 3 #enemy velocity
        self.flipped = True  #determines when to flip enemy


    def Enmove(self):
        """Moves the enemy along a set path"""
        if self.vel > 0:
            if self.rect.x + self.vel < self.path[1]:
                self.rect.x += self.vel #Moving enemy towards end of path
            else:
                if self.flipped: #flip enemy and move along opposite direction
                    self.image = pygame.transform.flip(self.image, True, False)
                    self.flipped = False
                self.vel = -self.vel
        else:
            if self.rect.x - self.vel > self.path[0]:
                self.rect.x += self.vel #Moving enemy back to starting point
            else:
                if not self.flipped: #determining whether image should be flipped
                    self.image = pygame.transform.flip(self.image, True, False)
                    self.flipped = True 
                self.vel = -self.vel

class Coin(pygame.sprite.Sprite):
    """This class creates coins that the player can collect"""
    def __init__(self, xpos, ypos, filename):
        """Gets image and position coordinates and places coin"""
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename)
        self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos

class Game():
    """This class represents an instance of the game."""
 
    def __init__(self, stats):
        """Constructor. Create all our attributes and initialize
        the game. The stats provided customize the game."""

        #Set to True when game over
        self.game_over = False

        #Set to True when player beats the game
        self.game_complete = False

        #Controls time
        self.clock = pygame.time.Clock()
        
        #set up the player and groups
        self.all_sprites = pygame.sprite.Group()
    
        self.player = Player(stats[0])
        self.all_sprites.add(self.player)

        
        self.plist = pygame.sprite.Group() #create a platform group
        self.elist = pygame.sprite.Group() #create an enemy group
        self.clist = pygame.sprite.Group() #create a coin group

        self.nlist = pygame.sprite.Group() #creates nextlevel group
        self.endlist = pygame.sprite.Group() #endgame platform group

        self.blist = pygame.sprite.Group() #boss platform group

        #created boss platform and adding to groups
        for bossplat in BOSSPLAT:
            boss = Platform(*bossplat)
            self.all_sprites.add(boss)
            self.blist.add(boss)

        #creating next level platforms and adding to groups
        for levplat in NEXTLEVPLAT:
            nextplat = Platform(*levplat)
            self.all_sprites.add(nextplat)
            self.nlist.add(nextplat)

        #creating regular platforms and adding to groups
        for plat in PLIST:
            platform = Platform(*plat) #create platform for each set of variables in PLIST
            self.all_sprites.add(platform)
            self.plist.add(platform)
        
        #Creating coin sprites
        for c in COINLIST:
            coin = Coin(*c)
            self.all_sprites.add(coin)
            self.clist.add(coin)

        #creating enemy sprites
        for en in ELIST:
            enemy = Enemy(*en)
            self.all_sprites.add(enemy)
            self.elist.add(enemy)
            enemy.Enmove()

        #creating end game platform
        for end in ENDGAMEPLAT:
            endplat = Platform(*end)
            self.all_sprites.add(endplat)
            self.endlist.add(endplat)

        #set up the music
        self.pickUpSound = pygame.mixer.Sound('coin.wav')
        pygame.mixer.music.load('Adventure.OGG')
        self.gameOverSound = pygame.mixer.Sound('game over.wav')

        #play the background music
        pygame.mixer.music.play(-1, 0.0)
        self.musicPlaying = True

        
        

    def process_events(self, windowSurface):
        """Process all of the keyboard and mouse events."""
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                
                if event.key == K_LEFT or event.key == ord('a'):
                    self.player.moveRight = False
                    self.player.moveLeft = True
                    #set left animation to True
                    self.player.walkingl = True

                    #flip character to face left
                    if not self.player.flipped:
                        self.player.image = pygame.transform.flip(self.player.image, True, False)
                        self.player.flipped = True
                    
                elif event.key == K_RIGHT or event.key == ord('d'):
                    self.player.moveLeft = False
                    self.player.moveRight = True
                    #set right animation to True
                    self.player.walkingr = True

                    #flip character to face right
                    if self.player.flipped:
                        self.player.image = pygame.transform.flip(self.player.image, True, False)
                        self.player.flipped = False
                    

                elif event.key == K_UP or event.key == ord('w') or event.key == K_SPACE:
                    self.player.jump()
        
            elif event.type == KEYUP:
                if event.key == K_ESCAPE:
                    terminate()
                elif event.key == K_LEFT or event.key == ord('a'):
                    self.player.moveLeft = False
                    self.player.walkingl = False
                elif event.key == K_RIGHT or event.key == ord('d'):
                    self.player.moveRight = False
                    self.player.walkingr = False
                elif event.key == K_UP or event.key == ord('w'):
                    self.player.moveUp = False
                elif event.key == ord('m'):
                    #toggles background music
                    if self.musicPlaying:
                        pygame.mixer.music.stop()
                    else:
                        pygame.mixer.music.play(-1, 0.0)
                    self.musicPlaying = not self.musicPlaying

                  
            elif event.type == pygame.MOUSEBUTTONDOWN:
                #The user clicks to restart the game when it is over
                if self.game_over or self.game_complete:
                    #Display the menu, choose a level and start a new game
                    display_menu(windowSurface)
                    stats = [6]
                    self.__init__(stats)

 
    def run_logic(self):
        """ This method is run each time through the frame. It
        updates positions and checks for collisions. """
        
        #update the player's position
        self.player.update()

        for e in self.elist:
            e.Enmove() #move the enemy
            

        
        #check for collisions with platforms and set player's position accordingly
        plathits = pygame.sprite.spritecollide(self.player, self.plist, False)
        if plathits:
            if self.player.vel.y < 0: #If colliding from below, player moves down
                self.player.vel.y = -self.player.vel.y
            else:
                self.player.pos.y = plathits[0].rect.top #player moves to top
                self.player.vel.y = 0 #stop player from moving when on platform
                self.player.grounded = True #To determine whether or not player can jump          

        else:
            self.player.grounded = False #player cannot jump


        #Checking for enemy collision
        enhits = pygame.sprite.spritecollide(self.player, self.elist, False)
        
        #enemy collisions and lives
        for e in enhits:
            self.player.wait -= 5
            if self.player.wait == 0: #"invincibility" before life is lost    
                self.player.hide() #hide player
                self.player.lives -= 1
                self.player.wait = 90


        #Checking for coin collisions
        coinhits = pygame.sprite.spritecollide(self.player, self.clist, True)
        for c in coinhits:
            self.player.coincount += 1
            #play coin collect music
            if self.musicPlaying:
                self.pickUpSound.play()

        #checking whether player has collided with next level platform
        levhits = pygame.sprite.spritecollide(self.player, self.nlist, False)
        if levhits:
            self.player.level = 2

        #checking whether player has reached the boss
        bossplathits = pygame.sprite.spritecollide(self.player, self.blist, False)
        if bossplathits:
            self.player.level = 3


        #scrolling entire screen, player, and enemy upwards
        if self.player.rect.top <= WINDOWHEIGHT/4:
            self.player.pos.y += abs(self.player.vel.y) #player moves up when reaches 3/4 of screen
            #Likewise, all other sprites shift upwards. When a sprite is no longer on
            #the screen, it is deleted
            for plat in self.plist:
                plat.rect.y += abs(self.player.vel.y)
                if plat.rect.top >= WINDOWHEIGHT:
                    plat.kill()
            for e in self.elist:
                e.rect.y += abs(self.player.vel.y)
                if e.rect.top >= WINDOWHEIGHT:
                    e.kill()
            for c in self.clist:
                c.rect.y += abs(self.player.vel.y)
                if c.rect.top >= WINDOWHEIGHT:
                    c.kill()
            for n in self.nlist:
                n.rect.y += abs(self.player.vel.y)
                if n.rect.top >= WINDOWHEIGHT:
                    n.kill()
            for b in self.blist:
                b.rect.y += abs(self.player.vel.y)
                if b.rect.top >= WINDOWHEIGHT:
                    b.kill()
            for end in self.endlist:
                end.rect.y += abs(self.player.vel.y)
                if end.rect.top >= WINDOWHEIGHT:
                    end.kill()

        #checking if player has reached final platform. If so,
        #game_complete is set to True
        endhits = pygame.sprite.spritecollide(self.player, self.endlist, False)
        if endhits:
            self.game_complete = True

        #game over when all lives are lost or player falls down
        if self.player.lives == 0:
            self.game_over = True
            
        elif self.player.rect.top > WINDOWHEIGHT:
            self.game_over = True

  
    def display_frame(self, windowSurface):
        """Display everything to the screen for the game."""
        
        if self.game_over:
            # The user will click to restart the game
            GameOverScreen(windowSurface, "game over.png")
            basicFont = pygame.font.SysFont("Lunchtime Doubly So", 150)
            if len(str(self.player.coincount)) > 1:
                drawText(str(self.player.coincount), basicFont, windowSurface, 445, 400, DARKGREEN)
            else:
                drawText(str(self.player.coincount), basicFont, windowSurface, 470, 400, DARKGREEN)

        elif self.game_complete:
            #game complete. User clicks to restart
            GameOverScreen(windowSurface, "game complete.png")
            basicFont = pygame.font.SysFont("Lunchtime Doubly So", 100)
            drawText(str(self.player.coincount), basicFont, windowSurface, 530, 547, DARKGREEN)

        else:
            # draw the player and the platforms onto the surface
            self.all_sprites.draw(windowSurface)
            #Draw lives, level, and coins collected
            DrawLives(windowSurface, 850, 10, self.player.lives)
            CoinCount(windowSurface, self.player.coincount)
            NextLevel(windowSurface, self.player.level)

            #draw appropriate images for each level
            if self.player.level == 2:
                image = pygame.image.load("fireworks.png")
                windowSurface.blit(image, [420, 5])
                windowSurface.blit(image, [570, 5])
            elif self.player.level == 3:
                image = pygame.image.load("enemy1.png")
                windowSurface.blit(image, [400, 5])
                windowSurface.blit(image, [540, 5])
        
        # draw the window onto the screen
        pygame.display.update()


def main():
    """ Mainline for the program """

    #set the display, caption, and timer
    pygame.init()
    mainClock = pygame.time.Clock()
    windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
    pygame.display.set_caption("Cat's Big Adventure")

    #Display a menu, choose a level and instantiate a game
    display_menu(windowSurface)

    #initialize the game
    stats = [6]
    game = Game(stats)
        
    # run the game loop until the user quits
    while True:
        # Process events (keystrokes, mouse clicks, etc)
        game.process_events(windowSurface)

        # Update object positions, check for collisions
        game.run_logic()
        
        # Draw the current frame
        game.display_frame(windowSurface)

        #draw background image
        background_image = pygame.image.load("sky.png").convert()
        windowSurface.blit(background_image, [0, 0])
        
        mainClock.tick(FRAMERATE)
        
main()
