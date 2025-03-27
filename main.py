#remove the "hello from pygame community" message
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
#import pygame
import pygame
#import all constant values from constants.py
from constants import *
#import circleshape.py
from circleshape import CircleShape

def main():
    #initialize all the pygame modules
    pygame.init()
    #set the screen size useing pygame.display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #main game clock
    game_clock = pygame.time.Clock()
    #delta variable
    dt = 0
    #game loop
    while True :
        #check if the window is being close, exits the program if so
        for event in pygame.event.get(): #gets all the events from the queue
            if event.type == pygame.QUIT: #pygame.QUIT means the user hit the 'X' on the game window
                return
        #fill the surface with a solid color, in this case black
        screen.fill((0, 0, 0))
        #refresh/update the display
        pygame.display.flip()
        #wait for 1/60th of a second, aka 1 frame at 60fps
        #save the ammount of time since last frame, divide by 1000 to convert from millis to sec
        dt = (game_clock.tick(60) / 1000)

if __name__ == "__main__":
    main()