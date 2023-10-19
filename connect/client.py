import socket

class Client:
    def __init__(self, socket_or_adress):
        self.msg = None
        if (type(socket_or_adress) == socket.socket):
            self.s = socket_or_adress
        else:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.connect(socket_or_adress)
        self.s.setblocking(False)
    
    def send(self, msg):
        if not self.is_open(): return
        self.s.setblocking(True)
        self.s.send((msg + '\n').encode())
        self.s.setblocking(False)
        print('sent: ' + msg)
    
    def receive(self):
        if not self.is_open():
            return False
        try:
            self.msg = self.s.recv(4096).decode()[:-1]
            print('recieved: ' + self.msg)
            return True
        except BlockingIOError:
            return False
        except ConnectionResetError:
            self.s = None
            return False
    
    def close(self):
        if self.is_open(): self.s.close()
        self.s = None
    
    def is_open(self):
        return self.s != None
