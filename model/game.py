from model.player import Player
from model.obstacle import Obstacle

# The Game class.
# This class holds all information regarding the game and also contains all props like the player or the obstacles.
class Game(object):
    def __init__(self):
        self.gravity = 1.5  # The gravity affects how fast the player falls to the ground
        self.screen_height = 768
        self.screen_width = 1024
        self.ground_start = 768  # The height at which the ground starts. Everything before this is sky.
        self.obstacles = [] # The list of obstacles
        self.player = None # The player
    
    def get_running_velocity(self):
        return self.player.v[0]

    # --- Player ------------------------------------------------
    def add_player(self, player: Player):
        self.player = player
        player.set_game(self)

    def draw_player(self):
        if not self.player is None:
            self.player.draw()

    def update_player(self, input_action):
        if not self.player is None:
            self.player.update(input_action)   

    # --- Obstacles ------------------------------------------------
    def add_obstacle(self, obstacle: Obstacle):
        self.obstacles.append(obstacle)
        obstacle.set_game(self)

    def draw_obstacles(self):
        for obstacle in self.obstacles:
            obstacle.draw()

    def update_obstacles(self):
        for obstacle in self.obstacles:
            obstacle.update()