from model.constants import WIDTH as C_WIDTH, HEIGHT as C_HEIGHT, OPPONENT
import pgzrun
from model.game import Game
from model.player import Player
from model.obstacle import Obstacle
from connect.server import Server
from connect.client import Client



WIDTH = C_WIDTH
HEIGHT = C_HEIGHT

game = Game()
game.sounds = sounds

player = Player('player/peppa_pig.png')
game.add_player(player)

opponent = None
def add_opponent(client):
    global opponent
    opponent = Player('player/george_pig')
    opponent.client = client
    game.add_opponent(opponent)

obstacle = Obstacle('obstacle/fence')
game.add_obstacle(obstacle)

server = None
if (OPPONENT != ''):
    add_opponent(Client((OPPONENT, 31415)))
else:
    server = Server(31415)

def update():
    if opponent is None and server.accept():
        add_opponent(server.client)
    if not opponent is None:
        if not opponent.client.is_open(): exit()
        if opponent.client.receive():
            if (opponent.client.msg) == 'j': opponent.jump()
    game.update_player(keyboard.space)
    game.update_obstacles()
    game.detect_collisions()
    player.v[0] += 0.01
    if game.game_over and keyboard.R:
        game.restart()
        game.sounds.respawn.play()
        player.v[0] = 5

def draw():
    screen.draw.filled_rect(Rect(0,0,1024,600), (163, 232, 254))
    screen.draw.filled_rect(Rect(0,600,1024,768), (88, 242, 152))
    game.draw_player()
    game.draw_obstacles()
    screen.draw.text('Score: ' + str(game.score), (100,100), color=(0, 0 , 0), fontsize=45)
    screen.draw.text('Highscore: ' + str(game.highscore), (100,160), color=(0, 0 , 0), fontsize=45)
    


# start the application
game.restart()
pgzrun.go()
