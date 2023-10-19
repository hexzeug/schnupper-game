from pgzero.actor import Actor
from .constants import *


# The player class.
class Player(object):
    def __init__(self, image):
        self.actor = Actor(image)
        self.actor.pos = 100, 0 # Set the start position
        self.game = None
        self.jump_count = 0
    
    def reset(self):
        self.v = [5, 0]
        self.actor.pos = self.actor.x, GROUND - self.actor.height / 2
        self.game.score = 0

    def draw(self):
        self.actor.draw()

    def set_game(self, game):
        self.game = game

    def change_image(self, image):
        self.actor.image = image

    def update(self, space_pressed):
        if self.game is None:
            raise RuntimeError('The player has not been added to the game yet.')
        
        on_ground = self.actor.bottom >= GROUND
        falling = self.v[1] > 0

        if space_pressed and (on_ground or falling and self.jump_count < 3):
            self.game.clock.schedule_unique((lambda: self.change_image('player/alien_pink_duck')), 1.0)
            self.game.clock.schedule_unique((lambda: self.change_image('player/alien_pink_duck')), 1.5)
            self.v[1] = -25 if self.jump_count == 1 else -20
            self.jump_count += 1
            self.game.sounds.jump.play()
        
        self.actor.y += self.v[1]
        self.v[1] += GRAVITY

        if falling and on_ground:
            self.jump_count = 0
            self.v[1] = 0
            self.actor.bottom = GROUND
