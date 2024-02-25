import pygame

# Initialize pygame
pygame.init()

# screen
sw = 800
sh = 600
FPS = 60

# Create the screen
screen = pygame.display.set_mode((sw, sh))
pygame.display.set_caption("Space Game")

# background image
bg = pygame.image.load('úkoly\\game\\resouces\\images\\background.jpg')

# game objects
spaceship_img = pygame.image.load('úkoly\\game\\resouces\\images\\spaceship.png')
asteroid1_img = pygame.image.load('úkoly\game\\resouces\\images\\asteroid1.png')
asteroid2_img = pygame.image.load('úkoly\\game\\resouces\\images\\asteroid2.png')
asteroid3_img = pygame.image.load('úkoly\\game\\resouces\\images\\asteroid3.png')
coin_img = pygame.image.load('úkoly\\game\\resouces\\images\\coin.png')
heart_img = pygame.image.load('úkoly\\game\\resouces\\images\\heart.png')

# game object sizes
spaceship_size = (50, 50)

asteroid1_size = (300, 300)
asteroid2_size = (200, 200)
asteroid3_size = (150, 150)

coin_size = (35,35)
heart_size = (35, 35)

# load images
bg = pygame.transform.scale(bg, (sw, sh))  # Resize if necessary
spaceship_img = pygame.transform.scale(spaceship_img, spaceship_size)
coin_img = pygame.transform.scale(coin_img, coin_size)
heart_img = pygame.transform.scale(heart_img, heart_size)
