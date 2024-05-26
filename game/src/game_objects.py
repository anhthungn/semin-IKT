import pygame
import math
import random
from settings import *

class Spaceship:
    def __init__(self, size, speed, direction, position, hp):
        self._size = size
        self._speed = speed
        self._direction = direction
        self._position = position if position else ((sw - size[0]) // 2, (sh - size[1]) // 2)
        self._max_hp = 3
        self._current_hp = hp
        self._score = 0

        # load spaceship image
        self.img = pygame.transform.scale(spaceship_img, size)
        # get the dimensions of the spaceship image
        self.w, self.h = self._size
        self.x, self.y = self._position

        self.angle = 0
        self.update_rotation()

        self.colliding_asteroids = set()

    def update_rotation(self):
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect(center=(self.x, self.y))
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w // 2, self.y - self.sine * self.h // 2)

    def motion(self):   
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]: # rotate left
            self.angle += 5
        if keys[pygame.K_d]: # rotate right
            self.angle -= 5
        if keys[pygame.K_w]: # move forward
            self.x += self._speed * math.cos(math.radians(self.angle))
            self.y -= self._speed * math.sin(math.radians(self.angle))

            # Wrap around the screen
            self.x %= sw
            self.y %= sh

        self.update_rotation()

    def draw(self, screen):
        screen.blit(self.rotatedSurf, self.rotatedRect)
    
    def score_increase(self, value):
        self._score += value
    
    def life_deduction(self):
        self._current_hp -= 1

    def collision_detection(self, obj):
        if isinstance(obj, Asteroids):
            asteroid_rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)  # Create a rectangle for the asteroid's position and size
            if self.rotatedRect.colliderect(asteroid_rect):  # Check if the spaceship's rotated rectangle collides with the asteroid's rectangle
                if obj not in self.colliding_asteroids:  # If this asteroid is not already in the colliding set
                    self.life_deduction()  # Deduct one life from the spaceship
                    self.colliding_asteroids.add(obj)  # Add this asteroid to the set of colliding asteroids
            else:
                if obj in self.colliding_asteroids:  # If the asteroid was previously colliding but no longer is
                    self.colliding_asteroids.remove(obj)  # Remove it from the set of colliding asteroids
        elif isinstance(obj, Bonuses):
            obj_rect = obj._img.get_rect(topleft=(obj.x, obj.y))
            if self.rotatedRect.colliderect(obj_rect):
                if isinstance(obj, Heart):
                    health_recharge.play()
                    obj.restore_hp(self)  # Restore HP if it's a Heart bonus
                elif isinstance(obj, Diamond):
                    self.score_increase(100)
                    coin_sound.play()
                    obj.reset_position()
                elif isinstance(obj, Coin):
                    self.score_increase(50)
                    coin_sound.play()
                    obj.reset_position()
                return True
        return False
        
    def end_game(self):
        if self._current_hp <= 0:
            pygame.quit()
            exit()

class Asteroids:
    def __init__(self, img, size):
        self.img = img
        self.size = size
        self.width, self.height = self.size
        self.x = random.randint(0, sw - self.width)  # Random initial x position within screen width
        self.y = random.randint(0, sh - self.height)  # Random initial y position within screen height
        self.speed = random.randint(1, 3)  # Random speed
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
        self._img = img
        self.width, self.height = self._img.get_size()
        self.x = random.randint(0, sw - self.width)
        self.y = random.randint(0, sh - self.height)

    def draw(self, screen):
        screen.blit(self._img, (self.x, self.y))

    def reset_position(self):
        self.x = random.randint(0, sw - self.width)
        self.y = random.randint(0, sh - self.height)

class Coin(Bonuses):
    def __init__(self, size, img):
        super().__init__(size, img)

class Heart(Bonuses):
    def __init__(self, size, img):
        super().__init__(size, img)

    def restore_hp(self, spaceship):
        if spaceship._current_hp < spaceship._max_hp:
            spaceship._current_hp += 1
            self.reset_position()  # Move the heart to a new random position
    
class Diamond(Bonuses):
    def __init__(self, size, img):
        super().__init__(size, img)
