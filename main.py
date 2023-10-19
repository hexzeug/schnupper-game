import pgzrun
from model.game import Game
from model.player import Player
from model.obstacle import Obstacle
from model.constants import WIDTH as C_WIDTH, HEIGHT as C_HEIGHT

WIDTH = C_WIDTH
HEIGHT = C_HEIGHT

game = Game()
game.sounds = sounds

player = Player('player/alien_pink_stand')
game.add_player(player)

obstacle = Obstacle('obstacle/fence')
game.add_obstacle(obstacle)


def update():
    game.update_player(keyboard.space)
    game.update_obstacles()
    game.detect_collisions()
    player.v[0] += 0.01
    if game.game_over and keyboard.R:
        game.restart()
        game.sounds.respawn.play()
        player.v[0] = 5

def draw():
    screen.fill((40, 40, 40))
    game.draw_player()
    game.draw_obstacles()
    screen.draw.text('Score: ' + str(game.score), (100,100), color=(255,255,255), fontsize=45)


# start the application
game.restart()
pgzrun.go()
