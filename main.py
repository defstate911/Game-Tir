import pygame
import random
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGHT))

pygame.display.set_caption('Игра ТИР')
icon = pygame.image.load('img/tir1')
pygame.display.set_icon(icon)

target_image = pygame.image.load('img/tir2')
target_width = 80
target_hight = 80

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HIGHT - target_hight)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

running = True
while running:
    pass

pygame.quit()