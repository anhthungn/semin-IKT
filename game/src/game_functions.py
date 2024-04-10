import pygame
from game_objects import *
from settings import *

def run_game():
    pygame.init()

    # clock = pygame.time.Clock()

    # spaceship_hp = 3
    spaceship = Spaceship(spaceship_size, 1.5, (1, 0), (sw // 2, sh // 2), 3)

    # Create asteroids
    asteroids = []
    asteroid_counts = [3, 2, 3]  # Distribute the count of asteroids for each type

    for count, img, size in zip(asteroid_counts, [asteroid1_img, asteroid2_img, asteroid3_img], [asteroid1_size, asteroid2_size, asteroid3_size]):
        for _ in range(count):
            asteroids.append(Asteroids(img, size))

    # create coins
    num_coins = 3
    coins = [Bonuses(coin_size, coin_img) for _ in range(num_coins)]

    # Create hearts
    heart1 = Bonuses(heart1_size, heart1_img)

    # create diamons
    diamond = Bonuses(diamond_size, diamond_img)

    # Font settings for life counter
    font = pygame.font.Font(None, 36)
    text_color = (255, 255, 255)

    # Font settings for score counter
    font = pygame.font.Font(None, 36)
    text_color = (255, 255, 255)

    # Initialize score counter
    score = 0

    # main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # draw everything
        screen.blit(bg, (0, 0))

        spaceship.draw(screen)
        spaceship.motion()

        for asteroid in asteroids:
            asteroid.motion()
            asteroid.draw(screen)
            spaceship.collision_detection(asteroid)

        for coin in coins:
            coin.draw(screen)

        heart1.draw(screen)
        diamond.draw(screen)

        # Draw life counter label
        life_text = font.render("Life:", True, text_color)
        screen.blit(life_text, (20, 23))

        for i in range(spaceship.current_hp):
            screen.blit(heart2_img, (20 + life_text.get_width() + 10 + i * (heart2_img.get_width() + 5), 20))

        # Draw score counter
        score_text = font.render("Score: " + str(score), True, text_color)
        screen.blit(score_text, (sw - score_text.get_width() - 20, 20))

        pygame.display.flip() # update the display

        # # Cap the frame rate
        # clock.tick(FPS)

    pygame.quit()
