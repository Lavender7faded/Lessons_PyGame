# # Напишите программу, в которой по щелчку левой кнопкой мышки в месте
# # щелчка появляется красный круг, постоянно растущий и увеличивающийся в
# # диаметре.

import pygame

size = width, height = 800, 600
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 120
MintCream_COLOR = (245, 255, 250)
LightSkyBlue_COLOR = (135, 206, 250)

x = y = 40

def draw(radius):
    pygame.draw.circle(screen, LightSkyBlue_COLOR, (x, y), radius)
r = 0

running = True
pygame.display.update()
click = False

while running:
    screen.fill(MintCream_COLOR)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            r=0
            click = True
            x, y = event.pos

    if click == True:
        draw(r)
        r = r + 1

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()