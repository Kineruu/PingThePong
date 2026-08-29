from random import randint
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
screen_clock = pygame.time.Clock()

running = True

# Paddle 1
#x, y, width, height
paddle = pygame.Rect(100, 200, 20, 100)

# Paddle 2
#x, y, width, height
paddle2 = pygame.Rect(700, 200, 20, 100)

# Ball
# x, y, ball size, ball size
ball = pygame.Rect(400, 300, 15, 15)

left_or_right = randint(0, 1)
if left_or_right == 0:
    ball_vel_x = 5
if left_or_right == 1:
    ball_vel_x = -5

up_or_down = randint(0, 1)
if up_or_down == 0:
    ball_vel_y = 5
if up_or_down == 1:
    ball_vel_y = -5 

while running:
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))

    # Drawing section

    # Paddle 1      # Where  # R    G    B    # thing
    pygame.draw.rect(screen, (255, 255, 255), paddle)

    # Paddle 2
    pygame.draw.rect(screen, (255, 255, 255), paddle2)

    # Ball
    pygame.draw.rect(screen, (255, 255, 255), ball)

    ball.x += ball_vel_x
    ball.y += ball_vel_y

    # Controls
    paddle_speed = 6

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]: paddle.y -= paddle_speed
    if keys[pygame.K_s]: paddle.y += paddle_speed

    if keys[pygame.K_i]: paddle2.y -= paddle_speed
    if keys[pygame.K_k]: paddle2.y += paddle_speed

    if paddle.y < 0: paddle.y = 0
    if paddle.y > 600 - paddle.height: paddle_y = 600 - paddle.height

    # Borders
    if ball.y + ball.height >= 600: ball_vel_y *= -1
    if ball.y + ball.height <= 0: ball_vel_y *= -1

    if ball.x + ball.width >= 800: ball_vel_x *= -1
    if ball.x + ball.width <= 0: ball_vel_x *= -1

    if paddle.top < 0: paddle.top = 0
    if paddle.bottom > 600: paddle.bottom = 600

    if ball.colliderect(paddle): ball_vel_x *= -1
    if ball.colliderect(paddle2): ball_vel_x *= -1

    pygame.display.flip()
    screen_clock.tick(60)

    # I am losing my mind