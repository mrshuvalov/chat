import socket

class server():
    def __init__(self, ip, port):
        self.port = port
        self.ips = []
        self.ip = ip
        self.connection = False
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((ip, port))


    def create_connection(self):
        self.connection = True
        self.sock.listen(100)
        while self.connection: 
            client_sock, client_addr = self.sock.accept()

    def messaging(self):
        self.connection = True
        while self.connection:
            msg, addr = self.sock.recvfrom(1024)
            self.ips.append(addr)
            print(bytes.decode(msg))
            for adr in self.ips:
                self.sock.sendall(msg, (adr, self.port))





