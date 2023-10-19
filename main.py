import pgzrun
from model.game import Game
from model.player import Player
from model.obstacle import Obstacle

# create the player


# create the game instance
game = Game()
# add the player


# define width and height of the application. pgzero needs these to be set
WIDTH = game.screen_width
HEIGHT = game.screen_height

# define colors
BACKGROUND_COLOR = (40, 40, 40)

def update():
    game.update_player(keyboard.space)

def draw():
    # drawing the background
    screen.fill(BACKGROUND_COLOR)

    # draw the player


# start the application
pgzrun.go()
