#IMPORTING PYGAME LIBRARY
import pygame
#IMPORTING EVERYTHING FROM CONFIG, TEXT, BUTTON, IMAGE, SHAPE AND SLIDER IN MODULES FOLDER
from modules.config import *
from modules.text import *
from modules.button import *
from modules.image import *
from modules.shape import *
from modules.slider import *

#MENU CLASS
class Menu:
    #INITIALIZE OF MENU
    def __init__(self, game):
        #SETTING GAME
        self.game = game
        #SETTING SCREEN FROM GAME
        self.screen = self.game.screen
        #SETTING WINDOW WITH WIDTH AND HEIGHT FROM CONFIG
        self.window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        #SETTING TEXT CLASS FROM TEXT
        self.text = Text
        #SETTING BUTTON CLASS FROM BUTTON
        self.button = Button
        #SETTING IMAGE CLASS FROM IMAGE
        self.image = Image
        #SETTING SHAPE CLASS FROM SHAPE
        self.shape = Shape
        #SETTING SLIDER CLASS FROM SLIDER
        self.slider = Slider
        #SETTING BIG FONTSIZE FROM CONFIG
        self.bfontsize = BIG_FONTSIZE
        #SETTING CENTER WIDTH AND CENTER HEIGHT FROM CONFIG
        self.cw = CENTER_W
        self.ch = CENTER_H
        #SETTING SHAPES FROM CONFIG
        self.r = RECT
        self.c = CIRCLE
        #SETTING COLORS FROM CONFIG
        self.black = BLACK
        self.white = WHITE
        self.green = GREEN
        self.dgreen = DARK_GREEN
        self.blue = BLUE
        self.red = RED
        self.ngray = NORMAL_GRAY
        #SETTING BACKGROUND COLOR
        self.bg_color = self.white

    #UPDATE PROCEDURE
    def update(self):
        #FILLING WINDOW WITH BACKGROUND COLOR
        self.window.fill(self.bg_color)
        #CALLING DRAW PROCEDURE
        self.draw()
        #UPDATING PYGAME DISPLAY
        pygame.display.update()

    #DRAW PROCEDURE
    def draw(self):
        #DO NOTHING
        pass
        
    #DRAW WINDOW PROCEDURE
    def draw_window(self):
        #RENDERING WINDOW IN SCREEN
        self.screen.blit(self.window, (0, 0))