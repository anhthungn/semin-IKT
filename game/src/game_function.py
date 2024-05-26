import pygame
from game_objects import *
from settings import *

def initialize_game():
    pygame.init()
    clock = pygame.time.Clock()

    spaceship = Spaceship(spaceship_size, 4, (1, 0), (sw // 2, sh // 2), 3)

    # Create asteroids
    asteroids = []
    asteroid_counts = [3, 3, 3]  # Distribute the count of asteroids for each type

    for count, img, size in zip(asteroid_counts, [asteroid1_img, asteroid2_img, asteroid3_img], [asteroid1_size, asteroid2_size, asteroid3_size]):
        for _ in range(count):
            asteroids.append(Asteroids(img, size))

    # create coins
    num_coins = 3
    coins = [Coin(coin_size, coin_img) for _ in range(num_coins)]

    heart1 = Heart(heart1_size, heart1_img)

    diamond = Diamond(diamond_size, diamond_img)

    return screen, clock, spaceship, asteroids, coins, diamond, heart1

def draw_objects(screen, spaceship, asteroids, coins, diamond, heart1):
    spaceship.draw(screen)
    spaceship.motion()

    for asteroid in asteroids:
        asteroid.motion()
        asteroid.draw(screen)
        spaceship.collision_detection(asteroid)

    for coin in coins:
        coin.draw(screen)
        spaceship.collision_detection(coin)  # Check for collision and handle scoring and repositioning
    
    diamond.draw(screen)
    spaceship.collision_detection(diamond)
    
    if spaceship._current_hp < 3: # Draw heart if spaceship HP is below 3
        heart1.draw(screen)
        spaceship.collision_detection(heart1)

def update_scores(screen, spaceship):
    # Font settings
    font = pygame.font.Font("úkoly/game/resouces/font.ttf", 20)
    text_color = (255, 255, 255)

    # Draw life counter label
    life_text = font.render("LIFE:", False, text_color)
    screen.blit(life_text, (20, 23))

    for i in range(spaceship._current_hp):
        screen.blit(heart2_img, (20 + life_text.get_width() + 10 + i * (heart2_img.get_width() + 5), 20))

    # Draw score counter
    score_text = font.render("SCORE: " + str(spaceship._score), False, text_color)
    screen.blit(score_text, (sw - score_text.get_width() - 20, 20))

def draw_title(screen):
    # Draw background
    screen.blit(bg, (0, 0))

    # Draw game title
    game_title_rect = game_title.get_rect(center=(sw // 2, sh // 3 + 20))
    screen.blit(game_title, game_title_rect)

    # Draw "Press to Start" text
    font = pygame.font.Font("úkoly/game/resouces/bold_font.ttf", 20)
    text_color = (255, 255, 255)
    press_to_start_text = font.render("PRESS ANYWHERE TO START", True, text_color)
    press_to_start_rect = press_to_start_text.get_rect(center=(sw // 2, sh // 2 + 100))
    screen.blit(press_to_start_text, press_to_start_rect)

    pygame.display.flip()

def draw_game_over_screen(screen):
    # Draw game over button
    game_over_button_rect = game_over_button.get_rect(center=(sw // 2, sh // 3 + 20))
    screen.blit(game_over_button, game_over_button_rect)

    # Draw "Play again?" text
    font = pygame.font.Font("úkoly/game/resouces/bold_font.ttf", 20)
    text_color = (255, 255, 255)
    play_again_text = font.render("PLAY AGAIN?", True, text_color)
    play_again_rect = play_again_text.get_rect(center=(sw // 2, sh // 2 + 8))
    screen.blit(play_again_text, play_again_rect)

    # Draw "Yes" button
    yes_button_rect = yes_button.get_rect(center=(sw // 2 - 60, sh // 2 + 58))
    screen.blit(yes_button, yes_button_rect)

    # Draw "No" button
    no_button_rect = no_button.get_rect(center=(sw // 2 + 60, sh // 2 + 58))
    screen.blit(no_button, no_button_rect)

    pygame.display.flip()

    return yes_button_rect, no_button_rect

def run_game():
    while True:
        screen, clock, spaceship, asteroids, coins, diamond, heart1 = initialize_game()

        # Display the game title and "Press to Start" text
        draw_title(screen)

        # Wait for the player to click and start the game
        start_game = False
        while not start_game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    click_sound.play()
                    start_game = True

        # Main game loop
        game_over = False
        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            screen.blit(bg, (0, 0))

            draw_objects(screen, spaceship, asteroids, coins, diamond, heart1)
            update_scores(screen, spaceship)

            if spaceship._current_hp <= 0:
                game_over_sound.play()
                game_over = True

            pygame.display.flip()  # update the display
            clock.tick(FPS)

        # Display game over screen with buttons
        yes_button_rect, no_button_rect = draw_game_over_screen(screen)

        # Wait for the player to click "yes" or "no"
        play_again = None
        while play_again is None:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if yes_button_rect.collidepoint(event.pos):
                        click_sound.play()
                        play_again = True
                    elif no_button_rect.collidepoint(event.pos):
                        play_again = False

        if not play_again:
            pygame.quit()
            return

if __name__ == "__main__":
    run_game()

# def game_buttons(screen, clock, start_button_rect, game_over_button_rect, new_game_button_rect):
#     game_started = False
#     while not game_started:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 return False
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if start_button_rect and start_button_rect.collidepoint(event.pos):
#                     click_sound.play()
#                     game_started = True
#                 elif game_over_button_rect and game_over_button_rect.collidepoint(event.pos):
#                     click_sound.play()
#                     pygame.quit()
#                     return False
#                 elif new_game_button_rect and new_game_button_rect.collidepoint(event.pos):
#                     click_sound.play()
#                     return True

#         screen.blit(bg, (0, 0))
#         if start_button_rect:
#             screen.blit(start_button_img, start_button_rect)
#         if game_over_button_rect:
#             screen.blit(game_over_button, game_over_button_rect)
#         if new_game_button_rect:
#             screen.blit(new_game_button, new_game_button_rect)
        
#         pygame.display.flip()
#         clock.tick(FPS)

#     return True

# def run_game():
#     while True:
#         screen, clock, spaceship, asteroids, coins, diamond, heart1 = initialize_game()

#         # Start button settings
#         start_button_rect = start_button_img.get_rect(center=(sw // 2, sh // 2))

#         # Display the start button and wait for click
#         if not game_buttons(screen, clock, start_button_rect, None, None):
#             return

#         # Main game loop
#         game_over = False
#         while not game_over:
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     pygame.quit()
#                     return

#             screen.blit(bg, (0, 0))

#             draw_objects(screen, spaceship, asteroids, coins, diamond, heart1)
#             update_scores(screen, spaceship)

#             if spaceship._current_hp <= 0:
#                 game_over_sound.play()
#                 game_over = True

#             pygame.display.flip()  # update the display
#             clock.tick(FPS)

#         # Game over screen
#         game_over_button_rect = game_over_button.get_rect(center=(sw // 2, sh // 2 - 70))
#         new_game_button_rect = new_game_button.get_rect(center=(sw // 2, sh // 2 + 70))

#         if not game_buttons(screen, clock, None, game_over_button_rect, new_game_button_rect):
#             return

# if __name__ == "__main__":
#     run_game()