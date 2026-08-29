import pygame
import time
import keyboard

pygame.init()

screen = pygame.display.set_mode((800, 600))

running = True

paddle_x = 100
paddle_y = 200
paddle_width = 20
paddle_height = 100

while running:
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    pygame.draw.rect(
        # where
        screen,
        # R G B
        (255, 255, 255),
        # x, y, width, height
        (paddle_x, paddle_y, paddle_width, paddle_height))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]: paddle_y -= .35
    if keys[pygame.K_s]: paddle_y += .35

    if paddle_y < 0: paddle_y = 0
    if paddle_y > 600 - paddle_height: paddle_y = 600 - paddle_height

    pygame.display.flip()