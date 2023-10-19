from pgzero.actor import Actor

# The player class.
class Player(object):
    def __init__(self, image):
        self.actor = Actor(image)
        self.actor.pos = 100, 0 # Set the start position
        self.jump_height = -15  # The jump height is negative, as the top of the screen is 0 and the bottom is the height
        self.game = None
    
    def reset(self):
        self.v = [5, 0]
        self.actor.pos = self.actor.x, self.game.ground_start - self.actor.height / 2

    def draw(self):
        self.actor.draw()

    def set_game(self, game):
        self.game = game

    def update(self, space_pressed):
        if self.game is None:
            raise RuntimeError('The player has not been added to the game yet.')
        
        if space_pressed:
            self.v[1] = self.jump_height
        
        self.actor.y += self.v[1]
        self.v[1] += self.game.gravity
        
        lowestPoint = self.game.ground_start - self.actor.height / 2

        if self.actor.y > lowestPoint:
            self.v[1] = 0
            self.actor.y = lowestPoint
