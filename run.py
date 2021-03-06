from src import interactions
from src.charge import Charge
from src import container
import pygame
import time
import random as rand
import game


def NewCharge(self, num, size=20):
    pass

def GetRandCharges(num, size=20):
    charges = [Charge(rand.randint(0,100) + 450, rand.randint(0,100) + 450, size, -1) for _ in range(num)]
    return charges

def GetEdgeCharges(x1, y1, x2, y2):
    charges = []
    charges += [Charge(x1, y1, 20)]
    charges += [Charge(x1, y2, 20)]
    charges += [Charge(x2, y1, 20)]
    charges += [Charge(x2, y2, 20)]
    return charges


def SetRandCharges(self):
    self.charges = [Charge(rand.randint(0,100) + 400, rand.randint(0,100) + 400, 20, -1) for _ in range(rand.randint(3,7))]

def GetLattice(start, num, spacing):
    charges = []
    for i in range(0,num*spacing, spacing):
        for j in range(0, num*spacing, spacing):
            charges += [Charge(start + i, start + j, 20, 1, (0,255,0))]
    return charges





if __name__ == "__main__":
    (width, height) = (1000,1000)
    background_color = (255,255,255)
    x1 = 200
    y1 = 200
    x2 = 800
    y2 = 800
    ballsize = 10
    charges = GetRandCharges(3, ballsize)
    charges = charges + GetLattice(400, 5, 40)
    env = interactions.Interaction(2)
    env.new_charges(charges)
    boundary = container.Container(x1, y1, x2, y2, charges)
    
    sim = game.Simulation(width,height, background_color, charges, env, boundary, e_size=ballsize)


    while sim.running:
        sim.time_step()




