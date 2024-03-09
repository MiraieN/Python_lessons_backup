import pygame
import random
import numpy as np
import time

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Define a Ball class
class Ball:
    def __init__(self):
        self.x = random.randint(50, WIDTH - 50)
        self.y = random.randint(50, HEIGHT - 50)
        self.dx = random.choice([-2, 2])
        self.dy = random.choice([-2, 2])
        self.radius = 20

    def move(self):
        self.x += self.dx
        self.y += self.dy

        if self.x < self.radius or self.x > WIDTH - self.radius:
            self.dx *= -1
        if self.y < self.radius or self.y > HEIGHT - self.radius:
            self.dy *= -1

    def draw(self):
        pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), self.radius)

# Create a list to hold the balls
balls = [Ball()]

# Set up the game loop
clock = pygame.time.Clock()
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move and draw the balls
    for ball in balls:
        ball.move()
        ball.draw()

        # If the ball hits a wall, create a new ball
        if ball.x < ball.radius or ball.x > WIDTH - ball.radius or ball.y < ball.radius or ball.y > HEIGHT - ball.radius:
            balls.append(Ball())

    # Check if 90% or more of the pixels are white
    # if np.count_nonzero(screen.get_view('1') == 255) / (WIDTH * HEIGHT) >= 0.9:
    # Create a font object
    font = pygame.font.Font(None, 100)

    # Create a text surface
    text = font.render("WOW, you can see it", True, (0, 0, 0))

    # Get the rectangle of the text surface
    text_rect = text.get_rect()

    # Set the center of the text rectangle to the center of the screen
    text_rect.center = (WIDTH // 2, HEIGHT // 2)

    # Draw the text on the screen
    screen.blit(text, text_rect)

    # Update the display
    pygame.display.flip()

    # Delay for 2 seconds
    # time.sleep(2)

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(FPS)

# Clean up Pygame
pygame.quit()