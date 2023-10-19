from model.player import Player
from model.opponent import Opponent
from model.obstacle import Obstacle
from .constants import *

class Game(object):
    def __init__(self):
        self.obstacles = []
        self.player = None
        self.opponent = None
        self.game_over = True
        self.score = 0
        self.highscore = 0
        self.socket = None
    
    def get_running_speed(self):
        return self.player.v[0]
    
    def restart(self):
        self.game_over = False
        self.player.reset()
        if not self.opponent is None: self.opponent.reset()
        self.sounds.respawn.play()
        for o in self.obstacles:
            o.reset()

    # --- Player ------------------------------------------------
    def add_player(self, player: Player):
        self.player = player
        player.set_game(self)
    
    def add_opponent(self, opponent: Opponent):
        self.opponent = opponent
        opponent.set_game(self)
        opponent.reset()

    def draw_player(self):
        if not self.opponent is None:
            self.opponent.draw()
        if not self.player is None:
            self.player.draw()

    def update_player(self, input_action):
        if not self.player is None and (not self.player.dead or not self.player.dead):
            self.player.update(input_action)
            self.score += 1
            if self.highscore < self.score:
                self.highscore += 1
        if not self.opponent is None:
            self.opponent.update()


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
        if self.game_over: return
        for obstacle in self.obstacles:
            player_x1 = self.player.actor.left + 10
            player_x2 = self.player.actor.right - 10
            obstacle_x1 = obstacle.actor.x - obstacle.actor.width / 2
            obstacle_x2 = obstacle.actor.x + obstacle.actor.width / 2

            horizontal_overlap = player_x2 >= obstacle_x1 and player_x1 <= obstacle_x2
            
            player_y = self.player.actor.bottom - 10
            obstacle_y = obstacle.actor.y - obstacle.actor.height / 2

            vertical_overlap = player_y >= obstacle_y
        if vertical_overlap and horizontal_overlap:
            self.game_over = True
            self.player.die()
            self.sounds.death.play()
            if not self.opponent is None: self.socket.send('d')