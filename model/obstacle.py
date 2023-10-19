from pgzero.actor import Actor
import random

# The obstacle class.
class Obstacle(object):
    def __init__(self, image, speed=0):
        self.actor = Actor(image)
        self.actor.pos = 0, 0
        self.v = [speed, 0]
        self.game = None
    
    def reset(self):
        self.actor.y = self.game.ground_start - self.actor.height / 2
        self.actor.x = random.randrange(self.game.screen_width, self.game.screen_width + 400)

    def set_game(self, game):
        self.game = game

    def draw(self):
        self.actor.draw()
    
    def update(self):
        if self.actor.x < -self.actor.width:  # Reset the position if the obstacle has gone of screen.
            # The x position is set to a random value, to prevent the obstacles from sticking together.
            self.actor.x = random.randrange(
                self.game.screen_width + self.actor.width,
                self.game.screen_width + self.actor.width + 400
            )  
        else:  # If the obstacle is still on the screen move it to the left to create the feeling of running.
            self.actor.x -= self.game.get_running_speed() - self.v[0]
