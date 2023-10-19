from pgzero.actor import Actor
from .constants import *
import random


class Obstacle(object):
    def __init__(self, image, speed=0):
        self.actor = Actor(image)
        self.actor.pos = 0, 0
        self.v = [speed, 0]
        self.game = None
        self.pos = None
        self.send = False
    
    def reset(self):
        self.actor.y = GROUND - self.actor.height / 2
        self.actor.x = random.randrange(WIDTH, WIDTH + 600)

    def set_game(self, game):
        self.game = game

    def draw(self):
        self.actor.draw()
        self.pos = None
    
    def update(self, dt):
        if self.pos is None:
            if self.actor.x < -self.actor.width:
                self.actor.x = random.randrange(
                    WIDTH + self.actor.width,
                    WIDTH + self.actor.width + 400
                )  
            else:
                self.actor.x -= self.game.get_running_speed() - self.v[0] * FRAMERATE * dt
            if self.send:
                self.game.socket.send(f"o {int(self.actor.x)} {int(self.actor.y)}")
        
        else:
            self.actor.x = self.pos[0]
            self.actor.y = self.pos[1]
