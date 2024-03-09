import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BIG_RADIUS = 200
INNER_RADIUS = 30

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Inner Circle Movement")

# Inner Circle class
class InnerCircle(pygame.sprite.Sprite):
    def __init__(self, big_circle):
        super().__init__()
        self.radius = INNER_RADIUS
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, WHITE, (self.radius, self.radius), self.radius)
        self.rect = self.image.get_rect()
        self.big_circle = big_circle
        self.reset_position()
        self.dx = 2  # Adjust the speed as needed
        self.dy = 2
        # self.rect_left = big_circle.radius - ((big_circle.radius * 2/math.sqrt(2))/2)+big_circle.radius + self.radius
        # self.rect_up = self.rect_left
        # self.rect_right = big_circle.radius + ((big_circle.radius * 2/math.sqrt(2))/2)+big_circle.radius - self.radius
        # self.rect_down = self.rect_right
        # print(self.rect_left, self.rect_right, self.rect_down, self.rect_up)

    def reset_position(self):
        angle = math.radians(pygame.time.get_ticks() % 360)
        self.rect.center = (
            self.big_circle.rect.center[0] + int(math.cos(angle) * (BIG_RADIUS - INNER_RADIUS)),
            self.big_circle.rect.center[1] + int(math.sin(angle) * (BIG_RADIUS - INNER_RADIUS))
        )

    def update(self):
        # Move the inner circle
        self.rect.x += self.dx
        self.rect.y += self.dy

        # Check for collisions with the big circle
        distance = math.sqrt((self.rect.centerx - self.big_circle.rect.centerx) ** 2 +
                             (self.rect.centery - self.big_circle.rect.centery) ** 2)

        if distance + self.radius >= BIG_RADIUS:
            self.rotate()
            # self.reset_position()

            # Calculate reflection vector
            normal = pygame.Vector2(self.rect.centerx - self.big_circle.rect.centerx,
                                    self.rect.centery - self.big_circle.rect.centery).normalize()

            # Reflect the velocity vector
            velocity = pygame.Vector2(self.dx, self.dy)
            self.dx, self.dy = velocity.reflect(normal)

    def rotate(self):
        # Rotate the inner circle
        self.image = pygame.transform.rotate(self.image, 90)


# Big Circle class
class BigCircle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.radius = BIG_RADIUS
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, WHITE, (self.radius, self.radius), self.radius, width=2)  # Set width for the outline
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

# class Square:
#     def __init__(self):




# Create sprite groups
all_sprites = pygame.sprite.Group()
big_circle = BigCircle()
inner_circle = InnerCircle(big_circle)

all_sprites.add(big_circle, inner_circle)

# Main game loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update
    all_sprites.update()

    # Draw
    screen.fill(BLACK)
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)