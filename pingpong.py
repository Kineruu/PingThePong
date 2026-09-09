# imports
import random
import pygame

# we make the pygame thing work
pygame.init()
# screen resolution
screen = pygame.display.set_mode((800, 600))
screen_clock = pygame.time.Clock() #clock is used for fps apparently

# most basic counting system
p1points = 0
p2points = 0

# if it works or not
running = True
waiting = False
wait_start = 0

# gamemode
gamemode = 0
# 1 - player vs player
# 2 - player vs bot
# 3 - bot vs bot

# Paddle 1
#x, y, width, height
paddle = pygame.Rect(100, 200, 20, 100)

# Paddle 2
#x, y, width, height
paddle2 = pygame.Rect(700, 200, 20, 100)

# Ball
# x, y, ball size, ball size
ball = pygame.Rect(400, 300, 15, 15)

def return_ball_vel():
    x = random.choice([-4, 4])
    y = random.choice([-2, -1, 1, 2])

    return x, y

ball_vel_x, ball_vel_y = return_ball_vel()

ball_acceleration = 0.05
ball_max_speed = 5

ball_x = float(ball.x)
ball_y = float(ball.y)


# font for text
font = pygame.font.Font(None, 30)
menu_font = pygame.font.Font(None, 50)

def reset_ball():
    global ball_x, ball_y

    ball_x = 400
    ball_y = 300

    ball.x = int(ball_x)
    ball.y = int(ball_y)

    ball_vel_x, ball_vel_y = return_ball_vel()
    return ball_vel_x, ball_vel_y

def ball_velocity(ball, paddle, direction):
    hit_pos = ball.centery - paddle.centery

    ball_vel_y = hit_pos / 10
    ball_speed = 5

    ball_vel_x = direction * ball_speed
    return ball_vel_x, ball_vel_y

while running:
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            running = False

        if gamemode == 0 and evt.type == pygame.KEYDOWN:
            if evt.key == pygame.K_1: gamemode = 1
            elif evt.key == pygame.K_2: gamemode = 2
            elif evt.key == pygame.K_3: gamemode = 3

    screen.fill((0, 0, 0))

    if gamemode == 0:
        title = menu_font.render("PONG", True, (255, 255, 255))
        screen.blit(title, (350, 100))

        pvp = font.render("1 - Player vs Player", True, (255, 255, 255))
        screen.blit(pvp, (300, 200))

        pvai = font.render("2 - Player vs AI", True, (255, 255, 255))
        screen.blit(pvai, (300, 250))

        aivai = font.render("3 - AI vs AI", True, (255, 255, 255))
        screen.blit(aivai, (300, 300))
    else:

        # Drawing section
        # Paddle 1      # Where  # R    G    B    # thing
        pygame.draw.rect(screen, (255, 255, 255), paddle)
        # Paddle 2
        pygame.draw.rect(screen, (255, 255, 255), paddle2)
        # Ball
        pygame.draw.rect(screen, (255, 255, 255), ball)

        p1 = font.render(f"P1: {p1points}", True, (255, 255, 255))
        screen.blit(p1, (5, 10))

        p2 = font.render(f"P2: {p2points}", True, (255, 255, 255))
        screen.blit(p2, (700, 10))

        # Controls
        paddle_speed = 6
        bot_speed = 4
        bot2_speed = 5 

        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]: quit()

        if gamemode == 1 or gamemode == 2:
            if keys[pygame.K_w]: paddle.y -= paddle_speed
            if keys[pygame.K_s]: paddle.y += paddle_speed

        paddle.clamp_ip(pygame.Rect(0, 0, 275, 600))

        if gamemode == 1:
            if keys[pygame.K_UP]: paddle2.y -= paddle_speed
            if keys[pygame.K_DOWN]: paddle2.y += paddle_speed

        elif gamemode == 2:
            if ball.centery < paddle2.centery: paddle2.y -= bot_speed
            if ball.centery > paddle2.centery: paddle2.y += bot_speed

        elif gamemode == 3:
            if ball.centery < paddle.centery: paddle.y -= bot_speed
            if ball.centery > paddle.centery: paddle.y += bot_speed

            if ball.centery < paddle2.centery: paddle2.y -= bot2_speed
            if ball.centery > paddle2.centery: paddle2.y += bot2_speed  

        paddle2.clamp_ip(pygame.Rect(525, 0, 275, 600))

        # Crazy border checking
        if ball.right <= 0:
            p2points += 1
            ball_vel_x, ball_vel_y = reset_ball()

            waiting = True
            wait_start = pygame.time.get_ticks()

        if ball.left >= 800:
            p1points += 1
            ball_vel_x, ball_vel_y = reset_ball()

            waiting = True
            wait_start = pygame.time.get_ticks()

        if waiting:
            if pygame.time.get_ticks() - wait_start >= 1000:
                waiting = False

        if not waiting:
            # Prevents the ball from going through paddles
            steps = max(1, int(max(abs(ball_vel_x), abs(ball_vel_y))))

            for _ in range(steps):
                # Move the ball a small amount
                ball_x += ball_vel_x / steps
                ball_y += ball_vel_y / steps

                ball.x = int(ball_x)
                ball.y = int(ball_y)

                if ball_y <= 0:
                    ball_y = 0
                    ball_vel_y = abs(ball_vel_y)

                elif ball_y + ball.height >= 600:
                    ball_y = 600 - ball.height
                    ball_vel_y = -abs(ball_vel_y)

                if ball_vel_x < 0 and ball.colliderect(paddle):

                    ball_x = paddle.right
                    ball_vel_x = abs(ball_vel_x)

                    # -1 = very top
                    #  0 = center
                    # +1 = very bottom

                    hit_pos = ((ball.centery - paddle.centery)/ (paddle.height / 2))

                    ball_vel_y = hit_pos * 4

                    # Prevent nearly-horizontal shots
                    if abs(ball_vel_y) < 2:
                        if ball_vel_y >= 0: ball_vel_y = 2
                        else: ball_vel_y = -2

                    ball_vel_x += ball_acceleration
                    if ball_vel_x > ball_max_speed:
                        ball_vel_x = ball_max_speed


                if ball_vel_x > 0 and ball.colliderect(paddle2):
                    ball_x = paddle2.left - ball.width
                    ball_vel_x = -abs(ball_vel_x)

                    hit_pos = ((ball.centery - paddle2.centery) / (paddle2.height / 2))

                    ball_vel_y = hit_pos * 4

                    if abs(ball_vel_y) < 2:
                        if ball_vel_y >= 0: ball_vel_y = 2
                        else: ball_vel_y = -2

                    ball_vel_x -= ball_acceleration

                    if abs(ball_vel_x) > ball_max_speed: ball_vel_x = -ball_max_speed

                ball.x = int(ball_x)
                ball.y = int(ball_y)

    pygame.display.flip()
    screen_clock.tick(60)