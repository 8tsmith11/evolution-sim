import pygame

class Entity:
    def __init__(
        self,
        x,
        y,
        radius,
        food,
        color,
        border_color,
        border_ratio, # border_ratio * radius = border thickness
    ):
        self.x, self.y = x, y
        self.radius = radius
        self.food = food

        self.color = color
        self.border_color = border_color
        self.border_ratio = border_ratio

    def tick(self, dt):
        pass

    def draw(self, screen):
        x, y = int(self.x), int(self.y)
        r = int(self.radius)

        # Draw the inner circle.
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

        # Draw the circle's outline (at least 1 pixel).
        border_width = max(1, int(r * self.border_ratio))
        pygame.draw.circle(screen, self.border_color, (x, y), r, border_width)