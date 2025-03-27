#remove the "hello from pygame community" message
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
#import pygame
import pygame

def main():
    print("Starting Asteroids!")

if __name__ == "__main__":
    main()