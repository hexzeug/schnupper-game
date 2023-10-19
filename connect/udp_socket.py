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
        if msg[0] not in ['p', 'o']:
            print(f"sent: '{msg}'")
    
    def receive(self):
        if not self.is_open():
            return False
        try:
            pl, addr = self.s.recvfrom(4096)
            if len(pl) == 0: return False
            self.msg = pl.decode()[:-1]
            self.host = addr[0]
            if self.msg[0] not in ['p', 'o']: print(f"received '{self.msg}' from '{addr}'")
            return True
        except BlockingIOError:
            return False
        except:
            return False
    
    def close(self):
        if self.is_open(): self.s.close()
        self.s = None
    
    def is_open(self):
        return self.s != None
    