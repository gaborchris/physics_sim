from src import interactions
from src.charge import Charge
import pygame
import time
import random as rand


if __name__ == "__main__":
    (width, height) = (1000,1000)
    background_color = (255,255,255)
    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption('Tutorial 1')

    a = Charge(20 + 100,30 + 100, 10)
    b = Charge(30 + 100,30 + 100, 10)
    c = Charge(25 + 100,25 + 100, 10)
    d = Charge(30 + 100,25 + 100, 10)
    e = Charge(27 + 100,21 + 100, 10)

    charges = [Charge(rand.randint(0,100) + 500, rand.randint(0,100) + 500, 20) for x in range(0, 5)]
    env = interactions.Interaction(charges, 10)


    running = True
    while running:
        time.sleep(0.01)
        screen.fill(background_color)

        for charge in charges:
            charge.draw(screen)

        pygame.display.flip()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    charges = [Charge(rand.randint(0,100) + 500, rand.randint(0,100) + 500, 20) for x in range(0, 5)]
                    env = interactions.Interaction(charges, 10)

        env.apply_force()
        #a.update(0.1,0.2)

