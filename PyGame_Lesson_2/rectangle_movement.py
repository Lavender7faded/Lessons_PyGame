# Напишите программу, отображающую движение прямоугольника
# произвольного размера, залитого зелёным цветом. Прямоугольник должен
# начать своё движение из нижнего левого угла и двигаться по диагонали в
# правый верхний угол, пока не скроется за границами окна программы.

import pygame

size = width, height = 500, 500
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

green_Color = (130, 183, 75)
brown_Color = (193, 148, 106)

fps = 60

def draw(x, y):
    pygame.draw.rect(screen, green_Color, (x, y, 100, 80))

pos_x = 0
pos_y = 410

run = True
while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            run = False
    
    screen.fill(brown_Color)
    draw(pos_x, pos_y)

    pos_x = pos_x + 1
    pos_y = pos_y - 1

    clock.tick(fps)

    pygame.display.flip()

pygame.quit()