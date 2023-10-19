from pgzero.actor import Actor
from .constants import *
import random


class Obstacle(object):
    def __init__(self, image, speed=0):
        self.actor = Actor(image)
        self.actor.pos = 0, 0
        self.v = [speed, 0]
        self.game = None
    
    def reset(self):
        self.actor.y = GROUND - self.actor.height / 2
        self.actor.x = random.randrange(WIDTH, WIDTH + 600)

    def set_game(self, game):
        self.game = game

    def draw(self):
        self.actor.draw()
    
    def update(self, x = None, y = None):
        if x is None and y is None:
            if self.actor.x < -self.actor.width:  # Reset the position if the obstacle has gone of screen.
                # The x position is set to a random value, to prevent the obstacles from sticking together.
                self.actor.x = random.randrange(
                    WIDTH + self.actor.width,
                    WIDTH + self.actor.width + 400
                )  
            else:  # If the obstacle is still on the screen move it to the left to create the feeling of running.
                self.actor.x -= self.game.get_running_speed() - self.v[0]
        
        else:
            self.actor.x = x
            self.actor.y = y
