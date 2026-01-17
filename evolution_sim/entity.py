import pygame
import pygame.font
from pygame import Vector2

class Entity:
    draw_food = False
    debug_font = None

    def __init__(
        self,
        x,
        y,
        radius,
        food=0,
        color=(0, 0, 0),
        border_color=(0, 0, 0),
        border_ratio=0, # border_ratio * radius = border thickness
    ):
        self.position = Vector2(x, y)
        self.velocity = Vector2(0, 0)
        self.radius = radius
        self.food = food

        self.color = color
        self.border_color = border_color
        self.border_ratio = border_ratio

    def tick(self, dt):
        pass

    def draw(self, screen):
        x, y = int(self.position.x), int(self.position.y)
        r = int(self.radius)

        # Draw the inner circle
        pygame.draw.circle(screen, self.color, (x, y), self.radius)

        # Draw the circle's outline (at least 1 pixel)
        border_width = max(1, int(r * self.border_ratio))
        pygame.draw.circle(screen, self.border_color, (x, y), r, border_width)

        # Draw food if the debug view is enabled
        if Entity.draw_food:
            text_surface = Entity.debug_font.render(f"{self.food:.1f}", True, (0, 0, 0))
            text_rect = text_surface.get_rect()
            text_rect.center = (x, y)
            screen.blit(text_surface, text_rect)

