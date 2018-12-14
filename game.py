import pygame
import time
import types
import random as rand
from src.charge import Charge

class Simulation:


    def __init__(self, width, height, background_color, charges, env, cont, charge_gen = None, size_def=20):
        self.width = width
        self.height = height
        self.background_color = background_color
        self.screen = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption('Particle Simulation')
        self.running = True
        self.charges = charges
        self.env = env
        self.size_def = size_def
        self.container = cont
        if charge_gen is not None:
            self.charge_gen = types.MethodType(charge_gen, self)

    

    def charge_gen(self):
        self.charges = [Charge(rand.randint(0,self.width) , rand.randint(0,self.height), 20) for _ in range(rand.randint(3,100))]


    def place_charge(self, x, y, size, polar):
        self.charges = self.charges + [Charge(x,y,size, polar)]
        self.env.new_charges(self.charges)
        self.container.charges = self.charges



    def time_step(self):
        #time.sleep(0.02)
        self.screen.fill(self.background_color)
        for charge in self.charges:
            charge.draw(self.screen)
        self.container.draw(self.screen)
        pygame.display.flip()
        self.EventHandler()
        self.container.CheckBoundary()
        self.env.apply_force()


    def EventHandler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.charge_gen()
                    self.env.new_charges(self.charges)
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                self.place_charge(x, y, self.size_def, 1)




        

