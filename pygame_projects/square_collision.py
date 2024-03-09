import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 400, 300
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Moving Square")

# Set up square properties
square_size = 50
square_color = (255, 0, 0)  # Red
square_speed = 5

# Set up initial square position and direction
square_x, square_y = 0, height // 2 - square_size // 2
move_right = True

# Create the square surface and draw the rectangle
square = pygame.Surface((square_size, square_size))
pygame.draw.rect(square, square_color, (0, 0, square_size, square_size))

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the square
    if move_right:
        square_x += square_speed
        if square_x + square_size > width:
            square_x = width - square_size
            move_right = False
    else:
        square_x -= square_speed
        if square_x < 0:
            square_x = 0
            move_right = True

    # Draw the background
    window.fill((255, 255, 255))  # White

    # Draw the square
    window.blit(square, (square_x, square_y))

    # Update the display
    pygame.display.flip()

    # Set the frames per second
    pygame.time.Clock().tick(30)