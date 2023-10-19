import pgzrun
from model.game import Game
from model.player import Player
from model.obstacle import Obstacle


player = Player('player/alien_pink_stand')

# create the game instance
game = Game()

game.add_player(player)

# define width and height of the application. pgzero needs these to be set
WIDTH = game.screen_width
HEIGHT = game.screen_height

# define colors
BACKGROUND_COLOR = (40, 40, 40)

obstacle = Obstacle('obstacle/fence')
game.add_obstacle(obstacle)

def update():
    game.update_player(keyboard.space)
    game.update_obstacles()
    game.detect_collisions()
    if game.game_over and keyboard.R:
        game.restart()

def draw():
    screen.fill(BACKGROUND_COLOR)
    game.draw_player()
    game.draw_obstacles()

# start the application
game.restart()
pgzrun.go()
