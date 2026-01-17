from entity import Entity
from config import FOOD_KINETIC_ENERGY, OVERLAP_EAT_RATE
from pygame.math import Vector2
from random import randint

# Default colors
PURPLE = (220, 30, 220)
DARK_PURPLE = (100, 20, 100)

class Blob(Entity):
    def __init__(self, *args, **kwargs):
        kwargs['color'] = PURPLE
        kwargs['border_color'] = DARK_PURPLE
        kwargs['border_ratio'] = 0.20
        super().__init__(*args, **kwargs)

        self.direction = Vector2(0, 0)
        self.direction.from_polar((1, randint(0, 360)))

        self.period = 10
        self.timer = 0

    def tick(self, dt):
        self.accelerate(10, self.direction, dt)
        super().tick(dt)

        self.timer += dt
        if self.timer >= self.period:
            self.timer = 0
            self.direction.from_polar((1, randint(0, 360)))


    # Expend food to change velocity
    def accelerate(self, food, direction: Vector2, dt):
        # Cannot expend more food than it has
        food *= dt
        food = min(self.food, food)
        self.food -= food
        dv = FOOD_KINETIC_ENERGY * food / self.area
        self.velocity += direction.normalize() * dv

    def interact(self, other: Entity, dt):
        self.overlap_eat(other, dt)

    def overlap_eat(self, other: Entity, dt):
        # If entities aren't overlapping, return
        if self.position.distance_to(other.position) >= self.radius + other.radius:
            return
            
        food = OVERLAP_EAT_RATE * self.area * dt

        # Cannot eat more food than the other entity has
        food = min(other.food, food)

        # Eat
        self.food += food
        other.food -= food
