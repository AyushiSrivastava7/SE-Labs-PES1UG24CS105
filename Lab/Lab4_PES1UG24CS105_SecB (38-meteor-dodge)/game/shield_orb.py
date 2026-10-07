import pygame
import random


class ShieldOrb:
    def __init__(self, width):
        self.x = random.randint(20, width - 20)
        self.y = -20
        self.radius = 12
        self.speed = 2
        self.color = (80, 220, 255)

    def update(self):
        self.y += self.speed

    def off_screen(self, height):
        return self.y > height + 30

    def collides(self, rect):
        dx = self.x - rect.centerx
        dy = self.y - rect.centery
        return (dx ** 2 + dy ** 2) ** 0.5 < self.radius + 16

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            self.color,
            (int(self.x), int(self.y)),
            self.radius
        )