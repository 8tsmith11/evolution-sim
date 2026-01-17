import pygame
import math
from pygame import Vector2
from config import FRICTION, WIDTH, HEIGHT

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
        self.area = math.pi * radius * radius
        self.food = food

        self.color = color
        self.border_color = border_color
        self.border_ratio = border_ratio

    def tick(self, dt):
        # If the entity's edge has moved past a screen border,
        # accelerate it back into bounds (100 unit/s/s)
        x, y = self.position.x, self.position.y
        if x + self.radius >= WIDTH:
            self.velocity.x -= dt * 100
        elif x - self.radius <= 0:
            self.velocity.x += dt * 100
        
        if y + self.radius >= HEIGHT:
            self.velocity.y -= dt * 100
        elif y - self.radius <= 0:
            self.velocity.y += dt * 100

        # Slow down due to friction, move
        if self.velocity.magnitude() > 0:
            # Acceleration = Friction * Area
            # Multiply by dt to get change in velocity
            dv = FRICTION * self.area * dt

            # Set velocity to 0 if dv >= v
            # Otherwise v -= dv
            if dv >= self.velocity.magnitude():
                self.velocity.update(0)
            else:
                self.velocity.scale_to_length(self.velocity.magnitude() - dv)

            # Update position based on velocity
            self.position += (self.velocity * dt)

        





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

