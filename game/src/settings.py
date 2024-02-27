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
bg = pygame.image.load(r'úkoly\game\resouces\images\background.jpg')

# game objects
spaceship_img = pygame.image.load(r'úkoly\game\resouces\images\spaceship.png')
laser_img = pygame.image.load(r'úkoly\game\resouces\images\laser.png')
asteroid1_img = pygame.image.load(r'úkoly\game\resouces\images\asteroid1.png')
asteroid2_img = pygame.image.load(r'úkoly\game\resouces\images\asteroid2.png')
asteroid3_img = pygame.image.load(r'úkoly\game\resouces\images\asteroid3.png')
coin_img = pygame.image.load(r'úkoly\game\resouces\images\coin.png')
heart1_img = pygame.image.load(r'úkoly\game\resouces\images\heart1.png')
heart2_img = pygame.image.load(r'úkoly\game\resouces\images\heart2.png')
diamond_img = pygame.image.load(r'úkoly\game\resouces\images\diamond.png')
alien_img = pygame.image.load(r'úkoly\game\resouces\images\alien.png')

# game object sizes
spaceship_size = (50, 50)
laser_size = (10, 3)

asteroid1_size = (300, 300)
asteroid2_size = (200, 200)
asteroid3_size = (150, 150)

coin_size = (35,35)
heart1_size = (35, 35)
hear2_size = (30, 30)
diamond_size = (38, 38)

alien_size = (20, 20)

# load images
bg = pygame.transform.scale(bg, (sw, sh))  # Resize if necessary
spaceship_img = pygame.transform.scale(spaceship_img, spaceship_size)
coin_img = pygame.transform.scale(coin_img, coin_size)
heart1_img = pygame.transform.scale(heart1_img, heart1_size)
heart2_img = pygame.transform.scale(heart2_img, hear2_size)
diamond_img = pygame.transform.scale(diamond_img, diamond_size)
alien_img = pygame.transform.scale(alien_img, alien_size)
