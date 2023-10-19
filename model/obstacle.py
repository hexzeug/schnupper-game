from pgzero.actor import Actor
import random

# The obstacle class.
class Obstacle(object):
    def __init__(self, image):
        self.actor = Actor(image)
        self.actor.y = 0
        self.actor.x = 0
        self.game = None

    def set_game(self, game):
        self.actor.y = game.ground_start - self.actor.height / 2
        self.actor.x = random.randrange(game.screen_width, game.screen_width + 400)
        self.game = game

    def draw(self):
        self.actor.draw()
    
    def update(self):
        if self.actor.x < 0 - self.actor.width:  # Reset the position if the obstacle has gone of screen.
            # The x position is set to a random value, to prevent the obstacles from sticking together.
            self.actor.x = random.randrange(
                self.game.screen_width + self.actor.width,
                self.game.screen_width + self.actor.width + 400
            )  
        else:  # If the obstacle is still on the screen move it to the left to create the feeling of running.
            self.actor.x -= self.game.running_speed
