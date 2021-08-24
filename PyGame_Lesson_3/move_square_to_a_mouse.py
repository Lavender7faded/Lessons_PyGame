# Напишите программу, аналогичную программе «Перемещение круга
# мышкой», в которой при захвате мышкой квадрата его можно переместить в
# другое место холста.

import pygame

size = width, height = 800, 600
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 120

PaleGoldenRod_COLOR = (238, 232, 170)
DarkOrange_COLOR = (255, 140, 0)

x, y = 120, 120

per = False
running = True

while running:
    screen.fill(PaleGoldenRod_COLOR)
    pygame.draw.rect(screen, DarkOrange_COLOR, (x, y, 100, 100))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (event.pos[0] < x or 
                event.pos[0] < y or
                event.pos[1] > x or
                event.pos[1] > y):
                per = True
        elif event.type == pygame.MOUSEBUTTONUP:
            per = False
        elif event.type == pygame.MOUSEMOTION and per == True:
            x, y = event.pos[0], event.pos[1]
            pygame.draw.rect(screen, DarkOrange_COLOR, (x, y, 100, 100))
        elif event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()