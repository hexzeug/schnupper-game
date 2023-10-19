from pgzero.actor import Actor
from .constants import *


# The player class.
class Opponent(object):
    def __init__(self, image):
        self.img = image
        self.actor = Actor(image)
        self.game = None
        self.dead = True
        self.prevPrevPos = [0, 0]
        self.prevPos = [0, 0]
        self.pos = [0, 0]
    
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

    def update(self):
        if self.pos is None:
            if self.dead: return
            self.pos = [
                self.prevPos[0],
                2 * self.prevPos[1] - self.prevPrevPos[1]
            ]
        self.actor.x = self.pos[0]
        self.actor.y = self.pos[1]
        if self.actor.bottom > GROUND:
            self.actor.bottom = GROUND
            self.pos[1] = self.actor.y
        self.prevPrevPos = self.prevPos
        self.prevPos = self.pos
        self.pos = None