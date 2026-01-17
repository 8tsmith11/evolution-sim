from entity import Entity
from config import PLANT_FOOD_RATE

# Default, constant plant colors
GREEN = (50, 180, 50)
DARK_GREEN = (20, 100, 20)

class Plant(Entity):
    def __init__(self, *args, **kwargs):
        kwargs['food'] = 0
        kwargs['color'] = GREEN
        kwargs['border_color'] = DARK_GREEN
        kwargs['border_ratio'] = 0.15
        super().__init__(*args, **kwargs)

        self.spore_threshold = 10


    def tick(self, dt):
        super().tick(dt)
        self.food += PLANT_FOOD_RATE * dt