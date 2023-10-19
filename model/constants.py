import sys

WIDTH = 1024
HEIGHT = 768
GROUND = 600
GRAVITY = 1.5
OPPONENT = '' if len(sys.argv) < 2 else sys.argv[1]
FRAMERATE = 60