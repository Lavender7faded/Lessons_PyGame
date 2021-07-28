import pygame

size = width, height = (700, 500)
screen = pygame.display.set_mode(size)

game_name = pygame.display.set_caption("The line")

peach_color = (255, 204, 153)
skyblue_color = (153, 153, 255)

pygame.init()

def draw():
    screen.fill(peach_color)
    
    pygame.draw.line(screen, skyblue_color, (0, 0), (700, 500), 8)
    pygame.draw.line(screen, skyblue_color, (700, 0), (0, 500), 8)

draw()

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()