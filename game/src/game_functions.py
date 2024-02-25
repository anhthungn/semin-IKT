import pygame
from game_objects import *
from settings import *

def run_game():
    pygame.init()

    clock = pygame.time.Clock()

    spaceship = Spaceship(spaceship_size, 3, (1, 0), (sw // 2, sh // 2), 3)

    # Create asteroids
    asteroids = []
    asteroid_counts = [4, 4, 3]  # Distribute the count of asteroids for each type

    for count, img, size in zip(asteroid_counts, [asteroid1_img, asteroid2_img, asteroid3_img], [asteroid1_size, asteroid2_size, asteroid3_size]):
        for _ in range(count):
            asteroids.append(Asteroids(img, size))
    
    # create coins
    num_coins = 3
    coins = [Bonuses(coin_size, coin_img) for _ in range(num_coins)]

    # Create hearts
    heart1 = Bonuses(heart_size, heart_img)

    # Initialize life counter
    life_counter = LifeCounter(heart_img, 3)

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

        for coin in coins:
            coin.draw(screen)

        # Draw hearts
        heart1.draw(screen)

        # Draw life counter label
        life_text = font.render("Life:", True, text_color)
        screen.blit(life_text, (20, 20))

        # Draw life hearts
        life_counter.draw(screen, (20 + life_text.get_width() + 10, 20))

        # Draw score counter
        score_text = font.render("Score: " + str(score), True, text_color)
        screen.blit(score_text, (sw - score_text.get_width() - 20, 20))

        pygame.display.flip() # update the display

        # Cap the frame rate
        clock.tick(FPS)

    pygame.quit()
