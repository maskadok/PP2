import pygame
import sys
pygame.init()
screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("двигающийся мячик ваууу")
WHITE = (255, 255, 255)
RED = (255, 0, 0)
ball_pos = [screen_size[0] // 2, screen_size[1] // 2]
ball_radius = 25
movement_speed = 20
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and ball_pos[1] - movement_speed >= 0:
                ball_pos[1] -= movement_speed
            elif event.key == pygame.K_DOWN and ball_pos[1] + movement_speed <= screen_size[1]:
                ball_pos[1] += movement_speed
            elif event.key == pygame.K_LEFT and ball_pos[0] - movement_speed >= 0:
                ball_pos[0] -= movement_speed
            elif event.key == pygame.K_RIGHT and ball_pos[0] + movement_speed <= screen_size[0]:
                ball_pos[0] += movement_speed
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, ball_pos, ball_radius)
    pygame.display.flip()
pygame.quit()
sys.exit()