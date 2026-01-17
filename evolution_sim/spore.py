from entity import Entity

class Spore(Entity):
    def __init__(self, entity, *args, **kwargs):
        kwargs['color'] = entity.color
        kwargs['border_color'] = entity.border_color
        super().__init__(*args, **kwargs)
        self.entity = entity

    def tick(self, dt):
        super().tick(dt)

        if self.velocity.magnitude() < 1.0:
            self.alive = False
            self.entity.position = self.position
            self.entity.food = self.food
            return [self.entity]
        