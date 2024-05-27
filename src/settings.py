import pygame

# Initialize pygame
pygame.init()

# screen
sw = 800
sh = 600
FPS = 60

# Create the screen
screen = pygame.display.set_mode((sw, sh))
pygame.display.set_caption("Space War")

# background image
bg = pygame.image.load(r'úkoly\game\resouces\images\background1.jpg')
game_title = pygame.image.load(r'úkoly\game\resouces\images\game_title.png')
game_over_title = pygame.image.load(r'úkoly\game\resouces\images\game_over_button.png')

# game objects
spaceship_img = pygame.image.load(r'úkoly\game\resouces\images\spaceship1.png')
asteroid1_img = pygame.image.load(r'úkoly\game\resouces\images\asteroid1.png')
asteroid2_img = pygame.image.load(r'úkoly\game\resouces\images\asteroid2.png')
asteroid3_img = pygame.image.load(r'úkoly\game\resouces\images\asteroid3.png')
coin_img = pygame.image.load(r'úkoly\game\resouces\images\coin.png')
heart1_img = pygame.image.load(r'úkoly\game\resouces\images\heart1.png')
heart2_img = pygame.image.load(r'úkoly\game\resouces\images\heart2.png')
diamond_img = pygame.image.load(r'úkoly\game\resouces\images\diamond.png')

# game buttons
yes_button = pygame.image.load(r"úkoly\game\resouces\images\yes_button.png")
no_button = pygame.image.load(r"úkoly\game\resouces\images\no_button.png")

# game object sizes
spaceship_size = (75, 45)
laser_size = (10, 3)

asteroid1_size = (50, 50)
asteroid2_size = (50, 50)
asteroid3_size = (50, 50)

coin_size = (35,35)
heart1_size = (43, 37)
hear2_size = (30, 30)
diamond_size = (50, 38)

yes_button_size = (83, 42)
no_button_size = (83, 42)

# sound effects
coin_sound = pygame.mixer.Sound(r'úkoly\game\resouces\sound effects\coin_sound.wav')
health_recharge = pygame.mixer.Sound(r'úkoly\game\resouces\sound effects\health_recharge.wav')
game_over_sound = pygame.mixer.Sound(r'úkoly\game\resouces\sound effects\game_over_sound.mp3')
click_sound = pygame.mixer.Sound(r'úkoly\game\resouces\sound effects\click_sound.wav')
damage_sound = pygame.mixer.Sound(r'úkoly\game\resouces\sound effects\damage_sound.mp3')

# load images
bg = pygame.transform.scale(bg, (sw, sh))  # Resize if necessary
spaceship_img = pygame.transform.scale(spaceship_img, spaceship_size)
coin_img = pygame.transform.scale(coin_img, coin_size)
heart1_img = pygame.transform.scale(heart1_img, heart1_size)
heart2_img = pygame.transform.scale(heart2_img, hear2_size)
diamond_img = pygame.transform.scale(diamond_img, diamond_size)
yes_button = pygame.transform.scale(yes_button, yes_button_size)
no_button = pygame.transform.scale(no_button, no_button_size)