#remove the "hello from pygame community" message
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
#import pygame
import pygame
#import all constant values from constants.py
from constants import *
#import circleshape.py
from circleshape import CircleShape
#import Player and Shot
from player import *
#import Asteroid
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    #initialize all the pygame modules
    pygame.init()
    #set the screen size useing pygame.display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #main game clock
    game_clock = pygame.time.Clock()
    #delta variable
    dt = 0
    #grouping
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    #construct the asteroid field
    asteroid_field = AsteroidField()
    #construct the player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT/2)
    #game loop
    while True :
        #check if the window is being close, exits the program if so
        for event in pygame.event.get(): #gets all the events from the queue
            if event.type == pygame.QUIT: #pygame.QUIT means the user hit the 'X' on the game window
                return
        
        #update all updatables, this is where keyboard input is processed
        updatable.update(dt)

        #check for collisions
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision(shot) and asteroid.collided == False and shot.collided == False:
                    asteroid.split()
                    shot.collided = True
            if asteroid.collision(player) and asteroid.collided == False:
                player.collided = True

        #fill the surface with a solid color, in this case black
        screen.fill((0, 0, 0))
        #draw drawables i.e. player
        for item in drawable:
            item.draw(screen)

        #refresh/update the display
        pygame.display.flip()

        for object in drawable:
            if object.collided == True:
                object.kill()
        if player.collided == True:
            print("Game Over!")
            return

        #wait for 1/60th of a second, aka 1 frame at 60fps
        #save the ammount of time since last frame, divide by 1000 to convert from millis to sec
        dt = (game_clock.tick(60) / 1000)

if __name__ == "__main__":
    main()