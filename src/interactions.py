import math
class Interaction:
    def __init__(self, charges, force_const):
        self.charges = charges
        self.force_const = force_const


    def apply_force(self):
        x = 0
        for charge in self.charges:
            forcex = 0
            forcey = 0
            for other in self.charges:
                if other is not charge:
                    dist = self.get_distance(charge, other) + 0.00001
                    force = 1/(dist**2) 
                    angle = self.get_angle(charge, other)
                    forcex += math.cos(angle)*force
                    forcey += math.sin(angle)*force
            charge.update(self.force_const*forcex, self.force_const*forcey)
                    


    def get_distance(self,charge1, charge2):
        return math.sqrt((charge1.x-charge2.x)**2 + (charge1.y-charge2.y)**2)

    def get_angle(self,charge1, charge2):
        return math.atan2(charge1.y - charge2.y, charge1.x - charge2.x)





