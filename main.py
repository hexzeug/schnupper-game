from model.constants import WIDTH as C_WIDTH, HEIGHT as C_HEIGHT, OPPONENT
import pgzrun
from model.game import Game
from model.player import Player
from model.opponent import Opponent
from model.obstacle import Obstacle
from connect.udp_socket import UDPSocket



WIDTH = C_WIDTH
HEIGHT = C_HEIGHT

game = Game()
game.sounds = sounds

player = Player('player/peppa_pig')
game.add_player(player)

opponent = None
def add_opponent():
    global opponent
    opponent = Opponent('player/george_pig')
    game.add_opponent(opponent)

obstacle = Obstacle('obstacle/fence')
game.add_obstacle(obstacle)

socket = UDPSocket()
game.socket = socket

def restart():
    game.restart()
    game.sounds.respawn.play()
    player.v[0] = 5

def update():
    if not socket.is_open(): exit()
    if socket.receive():
        msg = socket.msg.split()
        if msg[0] == 'p': opponent.pos = list(map(int, msg[1:]))
        elif msg[0] == 'd': opponent.die()
        elif msg[0] == 'r': restart()
        elif msg[0] == 'o': obstacle.pos = map(int, msg[1:])
        elif msg[0] == 'c':
            add_opponent()
            restart()
    game.update_player(keyboard.space)
    game.update_obstacles()
    game.detect_collisions()
    player.v[0] += 0.01
    if player.dead and (opponent is None or opponent.dead) and keyboard.R:
        if not opponent is None: socket.send('r')
        restart()
    if opponent is None and keyboard.C:
        host = input('connect to: ')
        socket.host = host
        add_opponent()
        socket.send(f"c")
        restart()

def draw():
    screen.draw.filled_rect(Rect(0,0,1024,600), (163, 232, 254))
    screen.draw.filled_rect(Rect(0,600,1024,768), (88, 242, 152))
    game.draw_player()
    game.draw_obstacles()
    screen.draw.text('Score: ' + str(game.score), (100,100), color=(0, 0 , 0), fontsize=45)
    screen.draw.text('Highscore: ' + str(game.highscore), (100,160), color=(0, 0 , 0), fontsize=45)
    


# start the application
restart()
pgzrun.go()
