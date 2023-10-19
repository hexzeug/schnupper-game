from pgzero.actor import Actor
from .constants import *


# The player class.
class Opponent(object):
    def __init__(self, image):
        self.img = image
        self.actor = Actor(image)
        self.game = None
        self.dead = True
    
    def reset(self):
        self.dead = False
        self.actor.image = self.img

    def die(self):
        self.dead = True
        self.actor.image = self.img + '_hurt'

    def draw(self):
        self.actor.draw()

    def set_game(self, game):
        self.game = game

    def update(self, x, y):
        self.actor.pos(x, y)