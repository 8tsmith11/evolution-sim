import pygame
from entity import Entity
from plant import Plant
from blob import Blob
from random import randint

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height


        # Initialize entities
        # Plants

        plants = [Plant(randint(0, width), randint(0, height), 15) for _ in range(1)]
        blobs = [Blob(randint(0, width), randint(0, height), 30, food=2000000) for _ in range(10)]

        self.entities = plants
        self.entities.extend(blobs)

    def tick(self, dt):
        # Remove dead entities
        self.entities = [e for e in self.entities if e.alive]

        for i, a in enumerate(self.entities):
            for b in self.entities[i + 1:]:
                a.interact(b, dt)
                b.interact(a, dt)

        to_spawn = []
        for e in self.entities:
            new_entities = e.tick(dt)
            if new_entities:
                to_spawn.extend(new_entities)

        self.entities.extend(to_spawn)

    def draw(self, screen):
        for e in self.entities:
            e.draw(screen)