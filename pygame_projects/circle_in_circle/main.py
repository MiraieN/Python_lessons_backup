import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60
MIN_BALLS_DEGREE = 0
MAX_BALLS_DEGREE = 180

screen = pygame.display.set_mode((WIDTH, HEIGHT))

class Ball:
    def __init__(self):
        self.x = random.randint(50, WIDTH - 50)
        self.y = random.randint(50, HEIGHT - 50)
        self.radius = 30
        self.degree = random.randint(1, 179)
        self.center = (self.x + self.radius, self.y + self.radius)

    def move(self):
        self.collision()
        dx, dy = self.way()
        self.y += dy
        self.x += dx

    def collision(self):
        if not square_collision_passed(self):
            # check collision over the square

            new_degree = 1
            self.degree = new_degree
            pass

    def way(self):
        dy = 0.01111111 * self.degree
        if dy > 1:
            dy -= 2
        if dy < 0:
            dx = -1 - dy
        else:
            dx = 1 - dy
        return dx ,dy

    def draw(self):
        pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), self.radius)


class BigBall:
    def __init__(self):
        self.x, self.y = 0, 0
        self.radius = 200
        self.draw()

    def draw(self):
        pygame.draw.circle(screen, (100, 100, 0), (self.x, self.y), self.radius)


def square_collision_passed(obj):
    big_ball.x
    pass


ball = Ball()
big_ball = BigBall()












