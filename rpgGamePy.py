#pygame library
import pygame

#Screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
#ScreenColor as RGB codes
WHITE_COLOR = (255,255,255)
BLACK_COLOR = (0,0,0)

#Create window with specified sizes
game_screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
#Set window color to white
game_screen.fill(WHITE_COLOR)


