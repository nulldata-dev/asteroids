import pygame
from circleshape import CircleShape
from constants import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        
        self.rotation = 0 #tracks current player rotation
        self.shoot_cooldown = 0 #tracks the cooldown of the players shoot ability

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + (forward * self.radius)
        b = (self.position - (forward * self.radius)) - right
        c = (self.position - (forward * self.radius)) + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.shoot_cooldown <= 0:
            shot = Shot(self.position.x, self.position.y) #create a new shot
            shot.velocity = pygame.Vector2(0, 1) #create a vector for the new shot
            shot.velocity.rotate_ip(self.rotation) #rotate the shot vector to match the ship rotation
            shot.velocity = shot.velocity * PLAYER_SHOOT_SPEED #increase speed of vector
            self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN #start the cooldown for the shoot ability

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.shoot_cooldown -= dt #tick down the shot cooldown

        if keys[pygame.K_a]: #rotate left when a is pressed
            self.rotate(-dt)
        if keys[pygame.K_d]: #rotate right when d is pressed
            self.rotate(dt)

        if keys[pygame.K_w]: #move forward when w is pressed
            self.move(dt)
        if keys[pygame.K_s]: #move backward when s is pressed
            self.move(-dt)

        if keys[pygame.K_SPACE]: #shoot when spacebar is pressed
            self.shoot()

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, (150, 0,  200), self.position, self.radius, 0)

    def update(self, dt):
        self.position += self.velocity * dt