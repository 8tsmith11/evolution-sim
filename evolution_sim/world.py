import pygame
from entity import Entity

class World:
    def __init__(self):
        self.entities = [Entity(100, 100, 30, 30, (23, 32, 185), 0, 0.5)]

    def tick(self, dt):
        for e in self.entities:
            e.tick(dt)

    def draw(self, screen):
        for e in self.entities:
            e.draw(screen)