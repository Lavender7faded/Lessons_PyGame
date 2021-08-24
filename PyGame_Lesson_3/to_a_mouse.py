# Напишите программу, аналогичную программе «К щелчку», в которой
# жёлтый круг постоянно движется к курсору мышки без дополнительного
# щелчка.

################################################################

import pygame

size = width, height = 800, 600
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 120

x, y = 300, 300
x_new, y_new = x, y

Buttercream_COLOR = (239, 225, 206)
MediumPurple_COLOR = (147, 112, 219)

per = False
running = True

while running:
    screen.fill(Buttercream_COLOR)
    pygame.draw.circle(screen, MediumPurple_COLOR, (x, y), 60)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            x_new, y_new = event.pos[0], event.pos[1]
        elif event.type == pygame.QUIT:
            running = False

    if x_new > x:
        x = x + 1
    elif x_new < x:
        x = x - 1

    if y_new > y:
        y = y + 1
    elif y_new < y:
        y = y - 1
        
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
