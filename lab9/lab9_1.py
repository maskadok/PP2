import pygame
import pytz
import datetime

pygame.init()
screen = pygame.display.set_mode((800, 800))
clock_face = pygame.image.load('эти_часики.png')
minute_hand = pygame.image.load('такие.png')
second_hand = pygame.image.load('смешные.png')
center_x = 400
center_y = 400
def get_new_pos(image, angle, pos):
    rotated_image = pygame.transform.rotate(image, angle)
    original_rect = image.get_rect()
    rotated_rect = rotated_image.get_rect()
    rotated_rect.center = pos
    return rotated_image, rotated_rect
def update_hands():
    utc_now = datetime.datetime.utcnow()
    timezone = pytz.timezone('Etc/GMT-6')
    local_time = utc_now.replace(tzinfo=pytz.utc).astimezone(timezone)
    minutes = local_time.minute
    seconds = local_time.second
    minute_angle = -(minutes / 60) * 360 
    second_angle = -(seconds / 60) * 360
    rotated_minute_hand, rotated_minute_rect = get_new_pos(minute_hand, minute_angle, (center_x, center_y))
    rotated_second_hand, rotated_second_rect = get_new_pos(second_hand, second_angle, (center_x, center_y))
    screen.blit(clock_face, (0, 0))
    screen.blit(rotated_minute_hand, rotated_minute_rect.topleft)
    screen.blit(rotated_second_hand, rotated_second_rect.topleft)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    update_hands()
    pygame.display.flip()
    pygame.time.delay(1000)
pygame.quit()