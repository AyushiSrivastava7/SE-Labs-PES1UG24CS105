import pygame


class Laser:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x - 3, y - 12, 6, 16)
        self.speed = 8
        self.color = (100, 220, 255)

    def update(self):
        self.rect.y -= self.speed

    def off_screen(self):
        return self.rect.bottom < 0

    def collides(self, meteor):
        dx = self.rect.centerx - meteor.x
        dy = self.rect.centery - meteor.y
        return (dx ** 2 + dy ** 2) ** 0.5 < meteor.radius + 3

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)