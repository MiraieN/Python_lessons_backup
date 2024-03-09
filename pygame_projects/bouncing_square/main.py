import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SQUARE_SIZE = 50

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Squares")

# Clock to control the frame rate
clock = pygame.time.Clock()

class Square:
    def __init__(self, x, y, color, speed):
        self.rect = pygame.Rect(x, y, SQUARE_SIZE, SQUARE_SIZE)
        self.color = color
        self.speed = speed

    def move(self):
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]

    def bounce(self):
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.speed[0] *= -1
        if self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.speed[1] *= -1

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)

# Create squares
square1 = Square(100, 100, WHITE, [5, 5])
square2 = Square(500, 300, WHITE, [-5, -5])

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLACK)

    # Move and bounce squares
    square1.move()
    square1.bounce()
    square2.move()
    square2.bounce()

    # Draw squares
    square1.draw()
    square2.draw()

    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)