# В центре квадратного холста появляется небольшой квадрат, имеющий
# жёлтую заливку, и плавно увеличивается по размеру холста. При увеличении
# квадрата все стороны холста должны быть равноудалены от всех сторон
# квадрата.

import pygame

size = width, height = 500, 500
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

green_Color = (130, 183, 75)
brown_Color = (193, 148, 106)

fps = 60
def draw(x, y, a, b):
    pygame.draw.rect(screen, green_Color, ((x, y), (a, b)))

pos_x = 250
pos_y = 250
p_a = 0
p_b = 0

run = True
while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            run = False
    
    screen.fill(brown_Color)
    draw(pos_x, pos_y, p_a, p_b)
    pos_x = pos_x - 1
    pos_y = pos_y - 1
    p_a = p_a + 3
    p_b = p_b + 3

    clock.tick(fps)

    pygame.display.flip()

pygame.quit()
