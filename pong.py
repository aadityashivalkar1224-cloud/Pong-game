import pygame, sys, random

pygame.init()
pygame.mixer.init()

#This was made by following the tutorial
WIDTH, HEIGHT = 1280, 720
FONT = pygame.font.SysFont("Consolas", int(WIDTH / 20))
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Footpong!")
CLOCK = pygame.time.Clock()

# Load sound: I used ai to help me make this
paddle_hit_sound = pygame.mixer.Sound("floop2_x.wav")

# Load and resize soccer ball image: I used ai to help me make this
original_ball_image = pygame.image.load("Football.png.png").convert_alpha()
ball_image = pygame.transform.scale(original_ball_image, (20, 20))

# Paddles: This was made by following the tutorial
player = pygame.Rect(0, 0, 10, 100)
player.center = (WIDTH - 100, HEIGHT / 2)

opponent = pygame.Rect(0, 0, 10, 100)
opponent.center = (100, HEIGHT / 2)

player_score, opponent_score = 0, 0

# Ball: This was made by following the tutorial
ball = pygame.Rect(0, 0, 20, 20)
ball.center = (WIDTH / 2, HEIGHT / 2)
x_speed, y_speed = 1, 1

# Obstacles: I used ai to help me make this
obstacle_size = (25, 160)
top_left_obstacle = pygame.Rect(0, 0, *obstacle_size)
top_right_obstacle = pygame.Rect(WIDTH - obstacle_size[0], 0, *obstacle_size)
bottom_left_obstacle = pygame.Rect(0, HEIGHT - obstacle_size[1], *obstacle_size)
bottom_right_obstacle = pygame.Rect(WIDTH - obstacle_size[0], HEIGHT - obstacle_size[1], *obstacle_size)
obstacles = [top_left_obstacle, top_right_obstacle, bottom_left_obstacle, bottom_right_obstacle]

#This was made by following the tutorial
while True:
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_UP] and player.top > 0:
        player.top -= 2
    if keys_pressed[pygame.K_DOWN] and player.bottom < HEIGHT:
        player.bottom += 2

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Ball-wall collision: This was made by following the tutorial
    if ball.y >= HEIGHT:
        y_speed = -1
    if ball.y <= 0:
        y_speed = 1

    # Ball-goal collision: This was made by following the tutorial
    if ball.x <= 0:
        player_score += 1
        ball.center = (WIDTH / 2, HEIGHT / 2)
        x_speed, y_speed = random.choice([1, -1]), random.choice([1, -1])
    if ball.x >= WIDTH:
        opponent_score += 1
        ball.center = (WIDTH / 2, HEIGHT / 2)
        x_speed, y_speed = random.choice([1, -1]), random.choice([1, -1])

    # Paddle collision with sound: I used ai to help me make this
    if ball.colliderect(player):
        x_speed = -1
        paddle_hit_sound.play()
    if ball.colliderect(opponent):
        x_speed = 1
        paddle_hit_sound.play()

    # Obstacle collision: I used ai to help me make this
    for obs in obstacles:
        if ball.colliderect(obs):
            if abs(ball.right - obs.left) < 10 or abs(ball.left - obs.right) < 10:
                x_speed *= -1
            if abs(ball.bottom - obs.top) < 10 or abs(ball.top - obs.bottom) < 10:
                y_speed *= -1

    # Opponent AI: This was made by following the tutorial
    if opponent.y < ball.y:
        opponent.top += 1
    if opponent.bottom > ball.y:
        opponent.bottom -= 1

    # Ball movement: This was made by following the tutorial
    ball.x += x_speed * 2.5
    ball.y += y_speed * 2.5

    # Drawing: I used ai to help me make this
    SCREEN.fill("light green")
    pygame.draw.line(SCREEN, "white", (0, 0), (WIDTH, 0), 30)
    pygame.draw.line(SCREEN, "white", (0, HEIGHT), (WIDTH, HEIGHT), 30)
    pygame.draw.rect(SCREEN, "blue", player)
    pygame.draw.rect(SCREEN, "red", opponent)
    SCREEN.blit(ball_image, ball.topleft)  # Draw resized soccer ball image
    pygame.draw.line(SCREEN, "white", (WIDTH / 2, 0), (WIDTH / 2, HEIGHT), 5)
    pygame.draw.circle(SCREEN, "white", (WIDTH // 2, HEIGHT // 2), 70, 5)

    # Penalty boxes: I used ai to help me make this
    penalty_box_width, penalty_box_height = 90, 400
    pygame.draw.rect(SCREEN, "white", pygame.Rect(WIDTH - penalty_box_width, HEIGHT // 2 - penalty_box_height // 2, penalty_box_width, penalty_box_height), 5)
    pygame.draw.rect(SCREEN, "white", pygame.Rect(0, HEIGHT // 2 - penalty_box_height // 2, penalty_box_width, penalty_box_height), 5)

    # Goal areas: I used ai to help me make this
    goal_area_width, goal_area_height = 50, 200
    pygame.draw.rect(SCREEN, "white", pygame.Rect(WIDTH - goal_area_width, HEIGHT // 2 - goal_area_height // 2, goal_area_width, goal_area_height), 5)
    pygame.draw.rect(SCREEN, "white", pygame.Rect(0, HEIGHT // 2 - goal_area_height // 2, goal_area_width, goal_area_height), 5)

    # Corner arcs: I used ai to help me make this
    corner_radius = 20
    pygame.draw.arc(SCREEN, "white", pygame.Rect(0, 0, corner_radius * 2, corner_radius * 2), 0, 1.57, 5)
    pygame.draw.arc(SCREEN, "white", pygame.Rect(WIDTH - corner_radius * 2, 0, corner_radius * 2, corner_radius * 2), 1.57, 3.14, 5)
    pygame.draw.arc(SCREEN, "white", pygame.Rect(0, HEIGHT - corner_radius * 2, corner_radius * 2, corner_radius * 2), 4.71, 0, 5)
    pygame.draw.arc(SCREEN, "white", pygame.Rect(WIDTH - corner_radius * 2, HEIGHT - corner_radius * 2, corner_radius * 2, corner_radius * 2), 3.14, 4.71, 5)

    # Obstacles: I used ai to help me make this
    for obs in obstacles:
        pygame.draw.rect(SCREEN, "white", obs)

    # Score: This was made by following the tutorial
    player_score_text = FONT.render(str(player_score), True, "white")
    opponent_score_text = FONT.render(str(opponent_score), True, "white")
    SCREEN.blit(player_score_text, (WIDTH / 2 + 50, 50))
    SCREEN.blit(opponent_score_text, (WIDTH / 2 - 50, 50))

    pygame.display.update()
    CLOCK.tick(300)
