#pygame library
import pygame
#pygame init for using pygame library
pygame.init()

#Screen properties
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Crossy RPG Game"
#ScreenColor as RGB codes
WHITE_COLOR = (255,255,255)
BLACK_COLOR = (0,0,0)
#For fps 
clock= pygame.time.Clock()
TICK_RATE = 144
is_Game_Over = False

#Create window with specified sizes
game_screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
#Set window color to white
game_screen.fill(WHITE_COLOR)
#Set window title
pygame.display.set_caption(SCREEN_TITLE)
#main loop to keep game running and screen updates
while not is_Game_Over:

    #loot to get all event happening in screen
    for event in pygame.event.get():

        #For printing events
        #print(event)

        #if we have a quit type event then exit the game loop
        if event.type == pygame.QUIT:
            is_Game_Over = True
    #update all game graphics
    pygame.display.update()
    #tick the clock to update everythig within the game
    clock.tick(TICK_RATE)


#Quit pygame and the program
pygame.quit()
quit()
