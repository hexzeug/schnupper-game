import socket

class UDPSocket:
    def __init__(self, host = None):
        self.public = socket.gethostbyname(socket.gethostname())
        self.host = host
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.bind(('0.0.0.0', 31415))
        self.s.setblocking(False)
        print(f"listening on {self.public}:31415")
    
    def send(self, msg):
        if not self.is_open() or self.host is None: return
        self.s.setblocking(True)
        self.s.sendto((msg + '\n').encode(), (self.host, 31415))
        self.s.setblocking(False)
        print(f"sent: '{msg}'")
    
    def receive(self):
        if not self.is_open():
            return False
        try:
            pl = self.s.recvfrom(4096).decode()
            if len(pl) == 0: raise Exception()
            self.msg = pl[:-1]
            print(f"received '{self.msg}'")
            return True
        except BlockingIOError:
            return False
        except:
            self.s = None
            return False
    
    def close(self):
        if self.is_open(): self.s.close()
        self.s = None
    
    def is_open(self):
        return self.s != None
    