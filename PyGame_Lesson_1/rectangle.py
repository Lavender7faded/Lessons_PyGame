import pygame

size = width, height = (int(input('Enter the width of screen: \n')), int(input('Enter the height of screen: \n')))
screen = pygame.display.set_mode(size)

game_name = pygame.display.set_caption("The rectangle")

green_color = (230, 255, 153)
violet_color = (230, 153, 255)

pygame.init()

def draw():
    screen.fill(green_color)
    
    pygame.draw.rect(screen, violet_color, (5, 5, 390, 290))

draw()

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()