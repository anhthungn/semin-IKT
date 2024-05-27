import pygame
from game_objects import *
from settings import *

def initialize_game():
    pygame.init()
    clock = pygame.time.Clock()

    spaceship = Spaceship(spaceship_size, 4, (1, 0), (sw // 2, sh // 2), 3)

    # create asteroids
    asteroids = []
    asteroid_counts = [3, 3, 3]  # distribute the count of asteroids for each type

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
        spaceship.collision_detection(coin)  # check for collision and handle scoring and repositioning
    
    diamond.draw(screen)
    spaceship.collision_detection(diamond)
    
    if spaceship._current_hp < 3: # draw heart if spaceship HP is below 3
        heart1.draw(screen)
        spaceship.collision_detection(heart1)

def update_scores(screen, spaceship):
    # font settings
    font = pygame.font.Font("úkoly/game/resouces/font.ttf", 20)
    text_color = (255, 255, 255)

    # draw life counter label
    life_text = font.render("LIFE:", False, text_color)
    screen.blit(life_text, (20, 23))

    for i in range(spaceship._current_hp):
        screen.blit(heart2_img, (20 + life_text.get_width() + 10 + i * (heart2_img.get_width() + 5), 15))

    # draw score counter
    score_text = font.render("SCORE: " + str(spaceship._score), False, text_color)
    screen.blit(score_text, (sw - score_text.get_width() - 20, 20))

def draw_title(screen):
    # draw background
    screen.blit(bg, (0, 0))

    # draw game title
    game_title_rect = game_title.get_rect(center=(sw // 2, sh // 3 + 20))
    screen.blit(game_title, game_title_rect)

    # draw "press to Start" text
    font = pygame.font.Font("úkoly/game/resouces/bold_font.ttf", 20)
    text_color = (255, 255, 255)
    press_to_start_text = font.render("PRESS ANYWHERE TO START", True, text_color)
    press_to_start_rect = press_to_start_text.get_rect(center=(sw // 2, sh // 2 + 100))
    screen.blit(press_to_start_text, press_to_start_rect)

    pygame.display.flip()

def draw_game_over_screen(screen):
    # draw game over button
    game_over_button_rect = game_over_title.get_rect(center=(sw // 2, sh // 3 + 20))
    screen.blit(game_over_title, game_over_button_rect)

    # draw "play again?" text
    font = pygame.font.Font("úkoly/game/resouces/bold_font.ttf", 20)
    text_color = (255, 255, 255)
    play_again_text = font.render("PLAY AGAIN?", True, text_color)
    play_again_rect = play_again_text.get_rect(center=(sw // 2, sh // 2 + 8))
    screen.blit(play_again_text, play_again_rect)

    # draw "Yes" button
    yes_button_rect = yes_button.get_rect(center=(sw // 2 - 60, sh // 2 + 58))
    screen.blit(yes_button, yes_button_rect)

    # draw "No" button
    no_button_rect = no_button.get_rect(center=(sw // 2 + 60, sh // 2 + 58))
    screen.blit(no_button, no_button_rect)

    pygame.display.flip()

    return yes_button_rect, no_button_rect

def run_game():
    while True:
        screen, clock, spaceship, asteroids, coins, diamond, heart1 = initialize_game()

        # display the game title and "Press to Start" text
        draw_title(screen)

        # wait for the player to click and start the game
        start_game = False
        while not start_game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    click_sound.play()
                    start_game = True

        # main game loop
        game_over = False
        damage_sound_played = False
        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            screen.blit(bg, (0, 0))

            draw_objects(screen, spaceship, asteroids, coins, diamond, heart1)
            update_scores(screen, spaceship)

            if spaceship._current_hp <= 0 and not damage_sound_played:
                damage_sound.play()
                damage_sound_played = True
                pygame.time.set_timer(pygame.USEREVENT, int(damage_sound.get_length() * 800))
            elif spaceship._current_hp <= 0 and damage_sound_played:
                game_over = True

            pygame.display.flip()  # update the display
            clock.tick(FPS)

        # Wait for the damage sound to finish
        waiting_for_sound = True
        while waiting_for_sound:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.USEREVENT:
                    waiting_for_sound = False

        # display game over screen with buttons
        yes_button_rect, no_button_rect = draw_game_over_screen(screen)
        game_over_sound.play()

        # wait for the player to click "yes" or "no"
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

