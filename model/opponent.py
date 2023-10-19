from pgzero.actor import Actor
from .constants import *


# The player class.
class Player(object):
    def __init__(self, image):
        self.img = image
        self.actor = Actor(image)
        self.actor.pos = 100, 0 # Set the start position
        self.game = None
        self.jump_count = 0
        self.sched_jump = False
        self.dead = True
    
    def reset(self):
        self.dead = False
        self.actor.image = self.img
        self.v = [5, 0]
        self.actor.pos = self.actor.x, GROUND - self.actor.height / 2
        self.game.score = 0
    
    def die(self):
        self.dead = True
        self.actor.image = self.img + '_hurt'

    def draw(self):
        self.actor.draw()

    def set_game(self, game):
        self.game = game

    def jump(self):
        self.sched_jump = True

    def update(self, space_pressed):
        if self.game is None:
            raise RuntimeError('The player has not been added to the game yet.')
        
        on_ground = self.actor.bottom >= GROUND
        falling = self.v[1] > 0

        if (space_pressed or self.sched_jump) and (on_ground or falling and self.jump_count < 3):
            self.v[1] = -25 if self.jump_count == 1 else -20
            self.jump_count += 1
            self.sched_jump = False
            self.game.sounds.jump.play()
            if not self.game.opponent is None and not self is self.game.opponent:
                self.game.opponent.client.send('j')
        
        self.actor.y += self.v[1]
        self.v[1] += GRAVITY

        if falling and on_ground:
            self.jump_count = 0
            self.v[1] = 0
            self.actor.bottom = GROUND