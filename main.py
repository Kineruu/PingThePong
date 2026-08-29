import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
screen_clock = pygame.time.Clock()

running = True

# Paddle
paddle_x = 100
paddle_y = 200
paddle_width = 20
paddle_height = 100

# Ball
ball_x = 400
ball_y = 300
ball_size = 15
ball_vel_x = 5
ball_vel_y = 5

while running:
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    # Drawing section

    # Paddle 1
    pygame.draw.rect(
        # where
        screen,
        # R G B
        (255, 255, 255),
        # x, y, width, height
        (paddle_x, paddle_y, paddle_width, paddle_height)
    )

    # Ball
    pygame.draw.rect(
        # where
        screen,
        # R G B
        (255, 255, 255),
        # x, y, width, height
        (ball_x, ball_y, ball_size, ball_size)
    )

    ball_x += ball_vel_x
    ball_y += ball_vel_y


    # Controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]: paddle_y -= 6.5
    if keys[pygame.K_s]: paddle_y += 6.5

    if paddle_y < 0: paddle_y = 0
    if paddle_y > 600 - paddle_height: paddle_y = 600 - paddle_height

    # Borders
    if ball_y + ball_size >= 600: ball_vel_y *= -1
    if ball_y + ball_size <= 0: ball_vel_y *= -1

    if ball_x + ball_size >= 800: ball_vel_x *= -1
    if ball_x + ball_size <= 0: ball_vel_x *= -1


    pygame.display.flip()
    screen_clock.tick(60)