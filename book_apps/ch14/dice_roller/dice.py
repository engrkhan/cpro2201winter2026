import random
from dataclasses import dataclass

@dataclass
class Die:
    value:int = 1
                
    def roll(self):
        self.value = random.randrange(1, 7)

               
class Dice:
    sum:int = 0
    # use explicit initializer because @dataclass doesn't allow
    # attributes with a default value that's mutable (like list)
    def __init__(self):
        self.list = []
        self.sum = 0

    def addDie(self, die):
        self.list.append(die)
        self.sum = self.sum + die.value

    def getSum(self):
        return self.sum   
                
    def rollAll(self):
        for die in self.list:
            die.roll()
            self.sum = self.sum + die.value
        
