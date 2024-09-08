import pygame
import random
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGHT))

pygame.display.set_caption('Игра ТИР')
icon = pygame.image.load('img/tir1.jpg')
pygame.display.set_icon(icon)

target_image = pygame.image.load('img/tir2.png')
target_width = 80
target_hight = 80

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HIGHT - target_hight)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_hight:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HIGHT - target_hight)
    screen.blit(target_image, (target_x, target_y))
    pygame.display.update()

pygame.quit()