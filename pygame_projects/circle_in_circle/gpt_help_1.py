import pygame
import sys
import math
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1000, 1000
BIG_RADIUS = 500
INNER_RADIUS = 10
FPS = 100
GRAVITY_VAR = 5
GRAVITY_INCREASE = 0.2
SPEED = 3

# Colors
WHITE = (255, 255, 255)

# Create a screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Inner Circle")

# Classes
class BigCircle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self):
        pygame.draw.circle(screen, WHITE, (self.x, self.y), self.radius, 1)

class InnerCircle:
    def __init__(self, x, y, radius, direction):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = SPEED
        self.direction = direction  # in degrees
        self.gravity_var = GRAVITY_VAR

    def move(self):
        radian_angle = math.radians(self.direction)
        self.x += self.speed * math.cos(radian_angle)
        # self.y += self.speed * math.sin(radian_angle)
        # print(self.y)
        self.gravity()
        # print(self.y)

    def gravity(self):
        self.y += self.gravity_var
        if self.gravity_var < GRAVITY_VAR * 2:
            self.gravity_var += GRAVITY_INCREASE

    def check_collision(self, big_circle):
        distance = math.sqrt((self.x - big_circle.x)**2 + (self.y - big_circle.y)**2)
        return distance + self.radius + 1 >= big_circle.radius

    def bounce(self, big_circle):
        angle_to_center = math.atan2(self.y - big_circle.y, self.x - big_circle.x)
        angle_of_approach = math.radians(self.direction)
        angle_of_reflection = 2 * angle_to_center - angle_of_approach + math.pi
        self.direction = math.degrees(angle_of_reflection)

        # Add a random angle adjustment for variety
        random_adjustment = random.uniform(-30, 30)  # Adjust the range as needed
        self.direction += random_adjustment
        self.move()
        if self.y > HEIGHT * 0.75:
            self.gravity_var = -GRAVITY_VAR*3

    def draw(self):
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), self.radius)


# Create instances
big_circle = BigCircle(WIDTH // 2, HEIGHT // 2, BIG_RADIUS)
# inner_circle = InnerCircle(WIDTH // 2, HEIGHT // 2 - BIG_RADIUS + INNER_RADIUS+100, INNER_RADIUS, 45)
circles = [InnerCircle(WIDTH // 2, HEIGHT // 2 - BIG_RADIUS + INNER_RADIUS+100, INNER_RADIUS, 45)]

# Game loop
clock = pygame.time.Clock()

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#
#     inner_circle.move()
#
#     if inner_circle.check_collision(big_circle):
#         inner_circle.bounce(big_circle)
#
#     screen.fill((0, 0, 0))
#     big_circle.draw()
#     inner_circle.draw()
#
#     pygame.display.flip()
#     clock.tick(FPS)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    for inner_circle in circles:
        inner_circle.move()

        if inner_circle.check_collision(big_circle):
            inner_circle.bounce(big_circle)
            # circles.append(InnerCircle(WIDTH // 2, HEIGHT // 2 - BIG_RADIUS + INNER_RADIUS+100, INNER_RADIUS, 45))

        screen.fill((0, 0, 0))
        big_circle.draw()
    for inner_circle in circles:
        inner_circle.draw()

    pygame.display.flip()
    clock.tick(FPS)
    # FPS += len(circles)//5