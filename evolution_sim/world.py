import pygame
from entity import Entity
from plant import Plant
from random import randint

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height


        # Initialize entities
        # Plants

        plants = [Plant(randint(0, width), randint(0, height), 15) for _ in range(20)]

        self.entities = plants

    def tick(self, dt):
        for e in self.entities:
            e.tick(dt)

    def draw(self, screen):
        for e in self.entities:
            e.draw(screen)