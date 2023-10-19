from model.player import Player
from model.obstacle import Obstacle
from .constants import *

class Game(object):
    def __init__(self):
        self.obstacles = []
        self.player = None
        self.game_over = True
    
    def get_running_speed(self):
        return self.player.v[0]
    
    def restart(self):
        self.game_over = False
        self.player.reset()
        for o in self.obstacles:
            o.reset()

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