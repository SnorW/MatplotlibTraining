import plotly
from random import randint


class Die:
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        self.rolls = randint(1, self.num_sides)
        return self.rolls
