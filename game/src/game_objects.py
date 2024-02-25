import pygame
import math
import random
from settings import *

class Spaceship:
    def __init__(self, size, speed, direction, position, hp):
        self._size = size
        self._speed = speed
        self._direction = direction
        self._position = position
        self._max_hp = hp
        self._current_hp = hp
        self._score = 0

        # load spaceship image
        self.img = spaceship_img
        # get the dimensions of the spaceship image
        self.w = self.img.get_width()
        self.h = self.img.get_height()
        # calculate initial position in the middle of the screen
        self.x = (sw - self.w) // 2
        self.y = (sh - self.h) // 2

        self.angle = 0
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w//2, self.y - self.sine * self.h//2)

        # Life counter
        self.font = pygame.font.Font(None, 36)  # Font for displaying text
        self.life_text = self.font.render('Life: ' + str(self._current_hp), True, (255, 255, 255))  # Initial life text

    def motion(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:  # Rotate left
            self.angle += 5  
        if keys[pygame.K_d]:  # Rotate right
            self.angle -= 5 
        if keys[pygame.K_w]:  # Move forward
            self.x += self._speed * math.cos(math.radians(self.angle))
            self.y -= self._speed * math.sin(math.radians(self.angle))

            # Wrap around the screen
            if self.x > sw:  # If spaceship moves off the right side
                self.x = 0  # Move to the left side
            elif self.x < 0:  # If spaceship moves off the left side
                self.x = sw  # Move to the right side
            if self.y > sh:  # If spaceship moves off the bottom
                self.y = 0  # Move to the top
            elif self.y < 0:  # If spaceship moves off the top
                self.y = sh  # Move to the bottom

        # Update rotated surface and rectangle
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)

        # Update head position
        self.head = (self.x + self.cosine * self.w // 2, self.y - self.sine * self.h // 2)

    def draw(self, screen):
        screen.blit(self.rotatedSurf, self.rotatedRect)

    def return_score(self):
        return self._score
    
    def score_increase():
        pass
    
    def life_deduction(self):
        pass

    def collision_detection():
        pass

    def end_game():
        pass

class Asteroids:
    def __init__(self, img, size):
        self.img = img
        self.size = size
        self.width, self.height = self.size
        self.x = random.randint(0, sw - self.width)  # Random initial x position within screen width
        self.y = random.randint(0, sh - self.height)  # Random initial y position within screen height
        self.speed = random.randint(1, 2)  # Random speed
        self.direction = random.randint(0, 360)  # Random initial direction

    def motion(self):
        angle_rad = math.radians(self.direction)
        dx = math.cos(angle_rad) * self.speed
        dy = math.sin(angle_rad) * self.speed
        self.x += dx
        self.y += dy

        # Wrap around the screen
        if self.x > sw:
            self.x = 0 - self.width
        elif self.x < 0 - self.width:
            self.x = sw
        if self.y > sh:
            self.y = 0 - self.height
        elif self.y < 0 - self.height:
            self.y = sh
    
    def draw(self, screen):
        screen.blit(pygame.transform.scale(self.img, self.size), (self.x, self.y))

class Bonuses:
    def __init__(self, size, img):
        self._size = size
        #self._position = position
        self._img = img
        self.width, self.height = self._img.get_size()
        self.x = random.randint(0, sw - self.width)
        self.y = random.randint(0, sh - self.height)

    def draw(self, screen):
        screen.blit(self._img, (self.x, self.y))

class Coin(Bonuses):
    def __init__(self, size, img, value):
        super().__init__(size, img, value)
        self._value = value

class Heart(Bonuses):
    def __init__(self, size, position, value):
        super().__init__(size, position, value)

class LifeCounter:
    def __init__(self, image, num_lives):
        self.image = image
        self.num_lives = num_lives
        self.rect = self.image.get_rect()

    def draw(self, screen, position):
        x, y = position
        for i in range(self.num_lives):
            screen.blit(self.image, (x + i * (self.rect.width + 5), y))


    
