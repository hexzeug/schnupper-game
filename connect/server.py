import socket
from .client import Client
from time import sleep

class Server:
    def __init__(self, port):
        host = socket.gethostbyname(socket.gethostname())
        print(f"opening server on {host}:{port}")
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind(('0.0.0.0', port))
        self.s.listen(5)
        self.s.setblocking(False)
    
    def accept(self):
        if not self.is_open(): return False
        try:
            s, _ = self.s.accept()
            self.client = Client(s)
            return True
        except BlockingIOError:
            return False
    
    def close(self):
        if self.is_open(): self.s.close()
        self.s = None
    
    def is_open(self):
        return self.s != None

s = Server(31415)

c = []

while True:
    sleep(1)
    for cl in c:
        if (cl.receive()):
            cl.send('Echo: ' + cl.msg)
    if (s.accept()):
        c.append(s.client)