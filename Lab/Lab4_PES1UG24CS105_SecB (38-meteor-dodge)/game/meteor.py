import pygame
import random
import math


class Meteor:
    def __init__(self, width, x=None, y=None, radius=None, vx=None, vy=None):
        self.x = random.randint(0, width) if x is None else x
        self.y = -30 if y is None else y

        if radius is None:
            self.radius = random.randint(12, 28)
        else:
            self.radius = radius

        if vx is None or vy is None:
            angle = random.uniform(70, 110)
            speed = random.uniform(2, 5)
            self.vx = math.cos(math.radians(angle)) * speed
            self.vy = math.sin(math.radians(angle)) * speed
        else:
            self.vx = vx
            self.vy = vy

        self.color = (
            random.randint(160, 220),
            random.randint(80, 120),
            random.randint(40, 80)
        )
        self.rot = 0
        self.rot_speed = random.uniform(-3, 3)

    def split(self):
        if self.radius < 20:
            return []

        child_radius = max(8, self.radius // 2)
        child_speed = max(3, math.sqrt(self.vx ** 2 + self.vy ** 2))

        angle = math.atan2(self.vy, self.vx)

        child1 = Meteor(
            700,
            self.x,
            self.y,
            child_radius,
            math.cos(angle - math.radians(35)) * child_speed,
            math.sin(angle - math.radians(35)) * child_speed
        )

        child2 = Meteor(
            700,
            self.x,
            self.y,
            child_radius,
            math.cos(angle + math.radians(35)) * child_speed,
            math.sin(angle + math.radians(35)) * child_speed
        )

        child1.color = self.color
        child2.color = self.color

        return [child1, child2]

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.rot = (self.rot + self.rot_speed) % 360

    def off_screen(self, height):
        return self.y > height + 60

    def collides(self, rect):
        cx, cy = rect.centerx, rect.centery
        dx, dy = self.x - cx, self.y - cy
        return (dx ** 2 + dy ** 2) ** 0.5 < self.radius + 16

    def draw(self, screen):
        pts = []

        for i in range(7):
            angle = math.radians(self.rot + i * (360 / 7))
            r = self.radius * (0.8 + 0.2 * (i % 2))
            pts.append((
                int(self.x + r * math.cos(angle)),
                int(self.y + r * math.sin(angle))
            ))

        pygame.draw.polygon(screen, self.color, pts)

        inner = [
            (
                int(self.x + (self.radius * 0.5) *
                    math.cos(math.radians(self.rot + i * (360 / 7)))),
                int(self.y + (self.radius * 0.5) *
                    math.sin(math.radians(self.rot + i * (360 / 7))))
            )
            for i in range(7)
        ]

        pygame.draw.polygon(
            screen,
            tuple(max(0, c - 40) for c in self.color),
            inner
        )
