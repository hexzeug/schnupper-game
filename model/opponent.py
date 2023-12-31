from pgzero.actor import Actor
from .constants import *


# The player class.
class Opponent(object):
    def __init__(self, image):
        self.img = image
        self.actor = Actor(image)
        self.game = None
        self.dead = True
        self.pos = [0, 0]
    
    def reset(self):
        self.dead = False
        self.actor.image = self.img

    def die(self):
        self.dead = True
        self.actor.image = self.img + '_hurt'
        if self.game.player.dead: self.game.music.pause()

    def draw(self):
        self.actor.draw()

    def set_game(self, game):
        self.game = game

    def update(self):
        self.actor.x = self.pos[0]
        self.actor.y = self.pos[1]