import pygame
import math
import random

class Charge:
    def __init__(self, x, y, size, charge=1, color=(0,0,255)):
        self.x = x*1.0 
        self.y = y*1.0
        self.speed_x = 0.0 
        self.speed_y = 0.0
        self.size = size
        self.color = color
        self.thickness = 3
        self.charge = charge

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size, self.thickness)

    def update(self, forcex, forcey):
        if self.charge is not 1:
            self.speed_x += forcex
            self.speed_y += forcey
            self.x += self.speed_x
            self.y += self.speed_y


