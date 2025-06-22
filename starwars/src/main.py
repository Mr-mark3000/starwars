
import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Star Wars Game")

# Load images
player_img = pygame.image.load("../assets/player.png")
enemy_img = pygame.image.load("../assets/enemy.png")
background_img = pygame.image.load("../assets/background.png")
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

font = pygame.font.SysFont(None, 36)

def reset_game():
    player_x = WIDTH // 2
    player_y = HEIGHT - 60
    player_speed = 5
    player_lives = 3

    bullets = []
    bullet_speed = 7

    enemy_x = random.randint(0, WIDTH - 50)
    enemy_y = 50
    enemy_speed = 2
    enemy_bullets = []
    enemy_bullet_speed = 5
    enemy_last_shot_time = pygame.time.get_ticks()

    score = 0
    level = 1

    return {
        "player_x": player_x,
        "player_y": player_y,
        "player_speed": player_speed,
        "player_lives": player_lives,
        "bullets": bullets,
        "bullet_speed": bullet_speed,
        "enemy_x": enemy_x,
        "enemy_y": enemy_y,
        "enemy_speed": enemy_speed,
        "enemy_bullets": enemy_bullets,
        "enemy_bullet_speed": enemy_bullet_speed,
        "enemy_last_shot_time": enemy_last_shot_time,
        "score": score,
        "level": level
    }

def draw_game(state):
    screen.blit(background_img, (0, 0))
    for bullet in state["bullets"]:
        pygame.draw.rect(screen, (255, 255, 0), (bullet[0], bullet[1], 4, 10))
    for e_bullet in state["enemy_bullets"]:
        pygame.draw.rect(screen, (255, 0, 0), (e_bullet[0], e_bullet[1], 4, 10))

    screen.blit(player_img, (state["player_x"], state["player_y"]))
    screen.blit(enemy_img, (state["enemy_x"], state["enemy_y"]))

    score_text = font.render(f"Score: {state['score']}  Level: {state['level']}  Lives: {state['player_lives']}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

def game_over_screen():
    screen.fill((0, 0, 0))
    game_over_text = font.render("Game Over! Press ENTER to play again or ESC to exit.", True, (255, 0, 0))
    screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2))
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_RETURN:
                    waiting = False

clock = pygame.time.Clock()
while True:
    state = reset_game()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    state["bullets"].append([state["player_x"] + player_img.get_width() // 2, state["player_y"]])

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and state["player_x"] > 0:
            state["player_x"] -= state["player_speed"]
        if keys[pygame.K_RIGHT] and state["player_x"] < WIDTH - player_img.get_width():
            state["player_x"] += state["player_speed"]

        for bullet in state["bullets"][:]:
            bullet[1] -= state["bullet_speed"]
            if bullet[1] < 0:
                state["bullets"].remove(bullet)

        state["enemy_y"] += state["enemy_speed"]
        if state["enemy_y"] > HEIGHT:
            state["enemy_y"] = 0
            state["enemy_x"] = random.randint(0, WIDTH - enemy_img.get_width())

        current_time = pygame.time.get_ticks()
        if current_time - state["enemy_last_shot_time"] >= 1000:
            state["enemy_bullets"].append([
                state["enemy_x"] + enemy_img.get_width() // 2,
                state["enemy_y"] + enemy_img.get_height()
            ])
            state["enemy_last_shot_time"] = current_time

        for e_bullet in state["enemy_bullets"][:]:
            e_bullet[1] += state["enemy_bullet_speed"]
            if e_bullet[1] > HEIGHT:
                state["enemy_bullets"].remove(e_bullet)

        for bullet in state["bullets"][:]:
            if state["enemy_x"] < bullet[0] < state["enemy_x"] + enemy_img.get_width() and state["enemy_y"] < bullet[1] < state["enemy_y"] + enemy_img.get_height():
                state["bullets"].remove(bullet)
                state["enemy_y"] = 0
                state["enemy_x"] = random.randint(0, WIDTH - enemy_img.get_width())
                state["score"] += 1
                if state["score"] % 5 == 0:
                    state["level"] += 1
                    state["enemy_speed"] += 1
                    state["enemy_bullet_speed"] += 0.5

        for e_bullet in state["enemy_bullets"][:]:
            if state["player_x"] < e_bullet[0] < state["player_x"] + player_img.get_width() and state["player_y"] < e_bullet[1] < state["player_y"] + player_img.get_height():
                state["enemy_bullets"].remove(e_bullet)
                state["player_lives"] -= 1
                if state["player_lives"] == 0:
                    running = False

        draw_game(state)
        pygame.display.flip()
        clock.tick(60)

    game_over_screen()
