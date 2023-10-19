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
        self.game_over = False
    
    def get_running_speed(self):
        return self.player.v[0]

    # --- Player ------------------------------------------------
    def add_player(self, player: Player):
        self.player = player
        player.set_game(self)

    def draw_player(self):
        if not self.player is None:
            self.player.draw()

    def update_player(self, input_action):
        if not self.player is None and not self.game_over:
            self.player.update(input_action)   

    # --- Obstacles ------------------------------------------------
    def add_obstacle(self, obstacle: Obstacle):
        self.obstacles.append(obstacle)
        obstacle.set_game(self)

    def draw_obstacles(self):
        for obstacle in self.obstacles:
            obstacle.draw()

    def update_obstacles(self):
        if not self.game_over:
            for obstacle in self.obstacles:
                obstacle.update()

    def detect_collisions(self):
        for obstacle in self.obstacles:
            player_x1 = self.player.actor.x - self.player.actor.width / 2
            player_x2 = self.player.actor.x + self.player.actor.width / 2
            obstacle_x1 = obstacle.actor.x - obstacle.actor.width / 2
            obstacle_x2 = obstacle.actor.x + obstacle.actor.width / 2

            horizontal_overlap = player_x2 >= obstacle_x1 and player_x1 <= obstacle_x2
            
            player_y = self.player.actor.y + self.player.actor.height / 2
            obstacle_y = obstacle.actor.y - obstacle.actor.height / 2

            vertical_overlap = player_y >= obstacle_y
        if vertical_overlap and horizontal_overlap:
            self.game_over = True