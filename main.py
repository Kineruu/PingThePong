from random import randint
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
screen_clock = pygame.time.Clock()

running = True

# Paddle
#x, y, width, height
paddle = pygame.Rect(100, 200, 20, 100)

# Ball
# x, y, ball size, ball size
ball = pygame.Rect(400, 300, 15, 15)

ball_vel_x = randint(-5, 5)
ball_vel_y = randint(-5, 5)

while running:
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    # Drawing section

    # Paddle 1      # Where  # R    G    B    # thing
    pygame.draw.rect(screen, (255, 255, 255), paddle)

    # Ball
    pygame.draw.rect(screen, (255, 255, 255), ball)

    ball.x += ball_vel_x
    ball.y += ball_vel_y

    # Controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]: paddle.y -= 6
    if keys[pygame.K_s]: paddle.y += 6

    if paddle.y < 0: paddle.y = 0
    if paddle.y > 600 - paddle.height: paddle_y = 600 - paddle.height

    # Borders
    if ball.y + ball.height >= 600: ball_vel_y *= -1
    if ball.y + ball.height <= 0: ball_vel_y *= -1

    if ball.x + ball.width >= 800: ball_vel_x *= -1
    if ball.x + ball.width <= 0: ball_vel_x *= -1

    if paddle.top < 0: paddle.top = 0
    if paddle.bottom > 600: paddle.bottom = 600

    pygame.display.flip()
    screen_clock.tick(60)

    # I am losing my mind