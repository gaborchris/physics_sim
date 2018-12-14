import math


class Interaction:


    def __init__(self, force_const):
        self.charges = []
        self.force_const = force_const


    def add_charges(self, charges):
        self.charges = self.charges + charges
    

    def new_charges(self, charges):
        self.charges = charges


    def apply_force(self):
        x = 0
        for charge in self.charges:
            if charge.charge is not 1:
                forcex = 0
                forcey = 0
                for other in self.charges:
                    if other is not charge:
                        dist = max(self.get_distance(charge, other),1)
                        force = 1/(dist**2) 
                        angle = self.get_angle(charge, other)
                        if other.charge is not charge.charge: 
                            forcex -= math.cos(angle)*force*1/(1+100*2.71**(-dist/5))
                            forcey -= math.sin(angle)*force*1/(1+100*2.71**(-dist/5))
                        else:
                            forcex += math.cos(angle)*force
                            forcey += math.sin(angle)*force
                charge.update(self.force_const*forcex, self.force_const*forcey)


    def get_distance(self,charge1, charge2):
        return math.sqrt((charge1.x-charge2.x)**2 + (charge1.y-charge2.y)**2)


    def get_angle(self,charge1, charge2):
        return math.atan2(charge1.y - charge2.y, charge1.x - charge2.x)





