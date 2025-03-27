#remove the "hello from pygame community" message
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
#import pygame
import pygame
#import all constant values from constants.py
from constants import *

def main():
    #initialize all the pygame modules
    pygame.init()
    #set the screen size useing pygame.display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while(True):
        #check if the window is being close, exits the program if so
        for event in pygame.event.get(): #gets all the events from the queue
            if event.type == pygame.QUIT: #pygame.QUIT means the user hit the 'X' on the game window
                return
        #fill the surface with a solid color, in this case black
        screen.fill((0, 0, 0))
        #refresh/update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()