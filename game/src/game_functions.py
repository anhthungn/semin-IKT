import pygame
from game_objects import *
from settings import *

def initialize_game():
    pygame.init()

    clock = pygame.time.Clock()

    spaceship_hp = 10
    spaceship = Spaceship(spaceship_size, 4, (1, 0), (sw // 2, sh // 2), spaceship_hp)

    # Create asteroids
    asteroids = []
    asteroid_counts = [2, 3, 3]  # Distribute the count of asteroids for each type

    for count, img, size in zip(asteroid_counts, [asteroid1_img, asteroid2_img, asteroid3_img], [asteroid1_size, asteroid2_size, asteroid3_size]):
        for _ in range(count):
            asteroids.append(Asteroids(img, size))

    # create coins
    num_coins = 3
    coins = [Bonuses(coin_size, coin_img) for _ in range(num_coins)]

    # Create hearts
    #heart1 = Bonuses(heart1_size, heart1_img)

    #diamond = Bonuses(diamond_size, diamond_img)

    return clock, spaceship, asteroids, coins

def draw_objects(screen, spaceship, asteroids, coins):
    spaceship.draw(screen)
    spaceship.motion()

    for asteroid in asteroids:
        asteroid.motion()
        asteroid.draw(screen)
        spaceship.collision_detection(asteroid)

    for coin in coins:
        coin.draw(screen)
        if spaceship.collision_detection(coin):  # If collision with coin occurs
            coins.remove(coin)  # Remove the coin from the list of coins

    #heart1.draw(screen)
    #diamond.draw(screen)

def update_scores(screen, spaceship):
    # Font settings for life counter
    font = pygame.font.Font(None, 36)
    text_color = (255, 255, 255)

    # Font settings for score counter
    font = pygame.font.Font(None, 36)
    text_color = (255, 255, 255)

    # Draw life counter label
    life_text = font.render("Life:", True, text_color)
    screen.blit(life_text, (20, 23))

    for i in range(spaceship._current_hp):
        screen.blit(heart2_img, (20 + life_text.get_width() + 10 + i * (heart2_img.get_width() + 5), 20))

    # Draw score counter
    score_text = font.render("Score: " + str(spaceship._score), True, text_color)
    screen.blit(score_text, (sw - score_text.get_width() - 20, 20))

def run_game():
    clock, spaceship, asteroids, coins = initialize_game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        screen.blit(bg, (0, 0))

        draw_objects(screen, spaceship, asteroids, coins)

        update_scores(screen, spaceship)

        pygame.display.flip()  # update the display

        clock.tick(FPS)
