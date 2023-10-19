import socket
from time import sleep

class Client:
    def __init__(self, socket_or_adress):
        self.msg = None
        if (type(socket_or_adress) == socket.socket):
            self.s = socket_or_adress
        else:
            self.s = socket.socket()
            self.s.connect(socket_or_adress)
        self.s.setblocking(False)
    
    def send(self, msg):
        self.s.setblocking(True)
        self.s.send((msg + '\n').encode())
        self.s.setblocking(False)
    
    def receive(self):
        try:
            self.msg = self.s.recv(4096).decode()[:-1]
            return True
        except BlockingIOError:
            return False

c = Client(('localhost', 31415))
c.send('hello')

while True:
    sleep(1)
    if (c.receive()):
        print(c.msg)