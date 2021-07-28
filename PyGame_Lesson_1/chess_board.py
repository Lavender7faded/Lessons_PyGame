import pygame

pygame.init()

# size = width, height = (1000, 1000)

width = height = int(input('Давайте намалюємо шахову дошку =) \nВкажіть розмір вікна від 200 до 1500 пікселів (він буде у форматі 1:1): \n')) 
size = (width, height)
screen = pygame.display.set_mode(size)

rows = cols = int(input('Вкажіть бажану кількість квадратів, я піднесу їх до квадрату та побудую шахове поле: \n'))
square_size = width // cols


game_name = pygame.display.set_caption("The chess board")

# rgb
white_color = (255, 230, 153)
black_color = (128, 64, 0)

def draw_squares(screen):
    screen.fill(white_color)
    for row in range(rows):
        for col in range(row % 2, rows, 2):
            pygame.draw.rect(screen, black_color, (row * square_size, col * square_size, square_size, square_size))

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

    draw_squares(screen)
    pygame.display.update()

pygame.quit()