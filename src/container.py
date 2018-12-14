import pygame
class Container:

    def __init__(self, x1, y1, x2, y2, charges):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = (255, 0, 0)
        self.charges = charges

    def CheckBoundary(self):
        eta = 0.8
        for charge in self.charges:
            if charge.x <= self.x1:
                charge.speed_x *= -eta
                charge.x = 2*self.x1 - charge.x
            if charge.x >= self.x2:
                charge.speed_x *= -eta
                charge.x = 2*self.x2 - charge.x

            if charge.y <= self.y1:
                charge.speed_y *= -eta
                charge.y = 2*self.y1 - charge.y
            if charge.y >= self.y2:
                charge.speed_y *= -eta
                charge.y = 2*self.y2 - charge.y


    def draw(self, screen):
        pygame.draw.line(screen, self.color, (self.x1, self.y1), (self.x1, self.y2)) 
        pygame.draw.line(screen, self.color, (self.x1, self.y1), (self.x2, self.y1)) 
        pygame.draw.line(screen, self.color, (self.x2, self.y2), (self.x1, self.y2)) 
        pygame.draw.line(screen, self.color, (self.x2, self.y2), (self.x2, self.y1)) 

