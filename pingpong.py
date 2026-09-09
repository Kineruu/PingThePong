# imports
import random
import pygame

# we make the pygame thing work
pygame.init()
# screen resolution

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen_clock = pygame.time.Clock() #clock is used for fps apparently

# Game settings
PADDLE_SPEED = 6
BOT_SPEED = 4
BOT2_SPEED = 5 

BALL_ACCELERATION = 0.05
BALL_MAX_SPEED = 5
BALL_BOUNCE_RANDOMNESS = 0.5

p1points = 0
p2points = 0

running = True
waiting = False
wait_start = 0

# 0 - Menu
# 1 - Player vs Player 
# 2 - Player vs Bot 
# 3 - Bot vs Bot
gamemode = 0


# Paddle 1
#x, y, width, height
paddle = pygame.Rect(100, 200, 20, 100)
paddle2 = pygame.Rect(700, 200, 20, 100)

# Ball
ball = pygame.Rect(400, 300, 15, 15)

ball_x = float(ball.x)
ball_y = float(ball.y)

def return_ball_vel():
    x = random.choice([-4, 4])
    y = random.choice([-2, -1, 1, 2])

    return x, y

ball_vel_x, ball_vel_y = return_ball_vel()

# Fonts
font = pygame.font.Font(None, 30)
menu_font = pygame.font.Font(None, 50)

def reset_ball():
    global ball_x, ball_y

    ball_x = WIDTH / 2
    ball_y = HEIGHT / 2

    ball.x = int(ball_x)
    ball.y = int(ball_y)

    return return_ball_vel()

def draw_menu():
    title = menu_font.render("PONG", True, (255, 255, 255))
    screen.blit(title, (350, 100))

    pvp = font.render("1 - Player vs Player", True, (255, 255, 255))
    screen.blit(pvp, (300, 200))

    pvai = font.render("2 - Player vs Bot", True, (255, 255, 255))
    screen.blit(pvai, (300, 250))

    aivai = font.render("3 - Bot vs Bot", True, (255, 255, 255))
    screen.blit(aivai, (300, 300))

def draw_game():
    pygame.draw.rect(screen, (255, 255, 255), paddle)
    pygame.draw.rect(screen, (255, 255, 255), paddle2)
    pygame.draw.rect(screen, (255, 255, 255), ball)

    p1 = font.render(f"P1: {p1points}", True, (255, 255, 255))
    screen.blit(p1, (5, 10))

    p2 = font.render(f"P2: {p2points}", True, (255, 255, 255))
    screen.blit(p2, (700, 10))

def handle_scoring():
    global p1points, p2points
    global ball_vel_x, ball_vel_y
    global waiting, wait_start

    if ball.right <= 0:
        p2points += 1
        ball_vel_x, ball_vel_y = reset_ball()
        waiting = True
        wait_start = pygame.time.get_ticks()

    elif ball.left >= WIDTH:
        p1points += 1
        ball_vel_x, ball_vel_y = reset_ball()
        waiting = True
        wait_start = pygame.time.get_ticks()

    if waiting:
        if pygame.time.get_ticks() - wait_start >= 1000:
            waiting = False

def move_ball():
    global ball_x, ball_y
    global ball_vel_x, ball_vel_y

    steps = max(1, int(max(abs(ball_vel_x), abs(ball_vel_y))))

    for _ in range(steps):
        ball_x += ball_vel_x / steps
        ball_y += ball_vel_y / steps

        ball.x = int(ball_x)
        ball.y = int(ball_y)

        # Top and bottom collision
        if ball_y <= 0:
            ball_y = 0
            ball_vel_y = abs(ball_vel_y)

        elif ball_y + ball.height >= HEIGHT:
            ball_y = HEIGHT - ball.height
            ball_vel_y = -abs(ball_vel_y)

        # Paddle 1 collision
        if ball_vel_x < 0 and ball.colliderect(paddle):
            ball_x = paddle.right
            ball_vel_x = abs(ball_vel_x)

            hit_pos = (ball.centery - paddle.centery) / (paddle.height / 2)

            ball_vel_y = (hit_pos * 4 + random.uniform(-BALL_BOUNCE_RANDOMNESS, BALL_BOUNCE_RANDOMNESS))

            if abs(ball_vel_y) < 2:
                if ball_vel_y >= 0: ball_vel_y = 2
                else: ball_vel_y = -2

            ball_vel_x += BALL_ACCELERATION
            if ball_vel_x > BALL_MAX_SPEED: ball_vel_x = BALL_MAX_SPEED

        # Paddle 2 collision
        if ball_vel_x > 0 and ball.colliderect(paddle2):
            ball_x = paddle2.left - ball.width
            ball_vel_x = -abs(ball_vel_x)

            hit_pos = (ball.centery - paddle2.centery) / (paddle2.height / 2)

            ball_vel_y = (hit_pos * 4 + random.uniform(-BALL_BOUNCE_RANDOMNESS, BALL_BOUNCE_RANDOMNESS))

            if abs(ball_vel_y) < 2:
                if ball_vel_y >= 0: ball_vel_y = 2
                else: ball_vel_y = -2

            ball_vel_x -= BALL_ACCELERATION
            if abs(ball_vel_x) > BALL_MAX_SPEED: ball_vel_x = -BALL_MAX_SPEED

        ball.x = int(ball_x)
        ball.y = int(ball_y)

def move_paddles(keys):
    if gamemode == 1 or gamemode == 2:
        if keys[pygame.K_w]: paddle.y -= PADDLE_SPEED
        if keys[pygame.K_s]: paddle.y += PADDLE_SPEED

    if gamemode == 1:
        if keys[pygame.K_UP]: paddle2.y -= PADDLE_SPEED
        if keys[pygame.K_DOWN]: paddle2.y += PADDLE_SPEED

    elif gamemode == 2:
        if ball.centery < paddle2.centery: paddle2.y -= BOT_SPEED
        if ball.centery > paddle2.centery: paddle2.y += BOT_SPEED

    elif gamemode == 3:
        if ball.centery < paddle.centery: paddle.y -= BOT_SPEED
        if ball.centery > paddle.centery: paddle.y += BOT_SPEED

        if ball.centery < paddle2.centery: paddle2.y -= BOT2_SPEED
        if ball.centery > paddle2.centery: paddle2.y += BOT2_SPEED

    paddle.clamp_ip(pygame.Rect(0, 0, 275, HEIGHT))
    paddle2.clamp_ip(pygame.Rect(525, 0, 275, HEIGHT))

def handle_events():
    global running, gamemode

    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            running = False

        if gamemode == 0 and evt.type == pygame.KEYDOWN:
            if evt.key == pygame.K_1:
                gamemode = 1
            elif evt.key == pygame.K_2:
                gamemode = 2
            elif evt.key == pygame.K_3:
                gamemode = 3

    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        running = False

    return keys

while running:
    handle_events()
    screen.fill((0, 0, 0))
    if gamemode == 0: draw_menu()
    else:
        draw_game()

        keys = pygame.key.get_pressed()
        move_paddles(keys)
        handle_scoring()

        if not waiting:
            move_ball()

    pygame.display.flip()
    screen_clock.tick(60)

pygame.quit()