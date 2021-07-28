# На холсте расположено два круга жёлтого и голубого цветов.
# Голубой круг остаётся неподвижен, а жёлтый всё время стремится
# приблизиться к нему. Как только расстояние между кругами становится
# небольшим, голубой круг «убегает» от жёлтого и появляется в произвольном
# месте холста.

import pygame
import random
import math


size = width, height = 500, 500
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

Color_Tofu = (234, 230, 218)
Color_Island_Paradise = (149, 222, 227)
Color_Warm_Sand = (192, 171, 142)

fps = 60
# отрисовка первого круга жёлтого цвета
def draw_circle_1(x, y, radius):
    pygame.draw.circle(screen, Color_Tofu, (x, y), radius)
# отрисовка второго круга голубого цвета   
def draw_circle_2(x, y, radius):
    pygame.draw.circle(screen, Color_Island_Paradise, (x, y), radius)  

# расположение круга в произвольном месте холста с учётом его радиуса
r = 40
random.seed()
x1, y1 = random.randint(r, width - r), random.randint(r, width - r)
random.seed()
x2, y2 = random.randint(r, width - r), random.randint(r, width - r)

# главный игровой цикл
running = True
while running:
    # внутри игрового цикл ещё один цикл приема и обработки различных событий
    events = pygame.event.get()
    for event in events:
        # обработка закрытия окна
        if event.type == pygame.QUIT:
            running = False

    screen.fill(Color_Warm_Sand)
    # изменение координат с целью приближения кругов друг к другу
    # для первого круга
    if x1 > x2:
        x1 = x1 - 1
    elif x1 < x2:
        x1 = x1 + 1
    if y1 > y2:
        y1 = y1 - 1
    elif y1 < y2:
        y1 = y1 + 1

    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    if distance <= (r + 5) + r:
        x2 = (random.randint(r, width - r)) % width
        y2 = (random.randint(r, height - r)) % height 
        
    draw_circle_1(x1, y1, r)
    draw_circle_2(x2, y2, r)
        
    # управление обновлением экрана
    clock.tick(fps)
    # обновление экрана
    pygame.display.flip()   

pygame.quit()