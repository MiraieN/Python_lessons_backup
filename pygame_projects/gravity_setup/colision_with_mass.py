import pygame
import sys

class Square:
    def __init__(self, x, y, size, color):
        self.square_size = size
        self.x = x
        self.y = y
        self.color = color
        self.speed = 0
        self.speed_loss = 0
        self.move = False
        self.move_left = True

        self.square = pygame.Surface((self.square_size, self.square_size))
        pygame.draw.rect(self.square, self.color, (0, 0, self.square_size, self.square_size))

    def step(self):
        if self.speed < 1:
            self.move = False
        if self.move and self.speed > 0:
            self.wall_collide()

            if self.move_left:
                self.x -= self.speed
            else:
                self.x += self.speed
            self.speed -= self.speed_loss
        window.blit(self.square, (self.x, self.y))
        pygame.display.flip()

    def set_start(self):
        self.speed = 20
        self.speed_loss = 0.1
        self.move = True

    def wall_collide(self):
        if self.x <= 0:
            self.move_left = False
        elif self.x + self.square_size >= width:
            self.move_left = True
        self.speed -= self.speed // 15

    def obj_collide(self, obj):
        if self.x_in_obj(obj) and self.y_in_obj(obj):
            if self.move_left:
                self.move_left = False
            else:
                self.move_left = True
            obj.speed = self.speed - self.speed_loss
            self.speed = 0 + self.speed_loss
            # self.move = False
            obj.move = True

    def x_in_obj(self, obj):
        # if self.x + self.square_size + self.speed // 2 >= obj.x and self.x - self.speed // 2 <= obj.x + obj.square_size:
        if self.x + self.square_size >= obj.x and self.x <= obj.x + obj.square_size:
            return True

    def y_in_obj(self, obj):
        if self.y < obj.y + obj.square_size and self.y + self.square_size > obj.y:
            return True

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Setup gravity")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


square1 = Square(100, 100, 50, GREEN)
square2 = Square(200, 100, 50, RED)
square3 = Square(400, 100, 50, GREEN)

square1.set_start()

squares = [square1, square2, square3]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    window.fill(WHITE)

    for sq in squares:
        sq.step()
        for col in squares:
            if col != sq:
                sq.obj_collide(col)

    pygame.time.Clock().tick(60)

    # window.fill(WHITE)
    # square1.step()
    # pygame.time.Clock().tick(80)
