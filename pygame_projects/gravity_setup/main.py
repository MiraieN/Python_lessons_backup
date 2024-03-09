import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Setup gravity")

WHITE = (255, 255, 255)

gravity_amount = 1

square_size = 50
square_color = (255, 0, 0)  # Red
square_speed = 8
square_y = 100
square_x = 100
speed_reducer = 10

move_down = True

square = pygame.Surface((square_size, square_size))
pygame.draw.rect(square, square_color, (0, 0, square_size, square_size))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if move_down:
        square_y += square_speed
        square_speed += gravity_amount
        if square_y + square_size >= height:
            move_down = False
            square_speed -= square_speed // speed_reducer
            speed_reducer -= 1.2
            if square_speed < 0.2:
                break
            # print(square_speed)

    if not move_down:
        square_y -= square_speed
        square_speed -= gravity_amount
        if square_speed == 0:
            move_down = True

    window.fill(WHITE)  # White

    window.blit(square, (square_x, square_y))

    pygame.display.flip()

    pygame.time.Clock().tick(80)

