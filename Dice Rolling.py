from dice import D20

class Hand(list):
    def __init__(self, size=0, die_class = D20):
        super().__init__()
        for _ in range(size):
            self.append(die_class())
            
    @classmethod
    def roll(cls, size = 2):
        return cls(size = size)
    
    @property
    def total(self):
        return sum(self)