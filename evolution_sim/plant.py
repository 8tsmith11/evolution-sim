from entity import Entity
from spore import Spore
from config import PLANT_FOOD_RATE
import random
import math
import pygame

# Default, constant plant colors
GREEN = (50, 180, 50)
DARK_GREEN = (20, 100, 20)

SPORE_RADIUS = 5
SPORE_AREA = math.pi * SPORE_RADIUS**2

class Plant(Entity):
    def __init__(self, *args, **kwargs):
        kwargs['color'] = GREEN
        kwargs['border_color'] = DARK_GREEN
        kwargs['border_ratio'] = 0.15
        super().__init__(*args, **kwargs)

        self.spore_threshold = 200
        self.min_spore_food = 150
        self.max_spore_food = 199


    def tick(self, dt):
        super().tick(dt)

        # Photosynthesis
        self.food += PLANT_FOOD_RATE * dt

        # Shoot a spore if food is sufficient
        if self.food >= self.spore_threshold:
            angle = random.uniform(0, 360)

            # Amount of food to propel the spore with
            # Velocity = Food / Spore Area
            propulsion_food = random.uniform(self.min_spore_food, self.max_spore_food)
            self.food -= propulsion_food
            propulsion_food -= 1 # The spore has 1 food to keep it alive
            magnitude = 100 * propulsion_food / SPORE_AREA
            spore_velocity = pygame.math.Vector2()
            spore_velocity.from_polar((magnitude, angle))
            spore_position = self.position + spore_velocity.normalize() * self.radius
            spore_plant = Plant(0, 0, 15)
            spore = Spore(spore_plant, spore_position.x, spore_position.y, SPORE_RADIUS, food=1)
            spore.velocity = spore_velocity

            return [spore]



