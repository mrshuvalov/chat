import socket

class client():

    def __init__(self, name, ip, port):
        self.name = name
        self.ip = ip
        self.port = port
        self.connection = False
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    def mailing(self):
        while self.connection:
            msg = input(self.name + " : ")
            msg = str.encode(msg)
            self.sock.sendto(msg, (self.ip, self.port))
            remsg, addr = self.sock.recvfrom(1024)
            if addr != self.ip:
                raise ConnectionError
            remsg = bytes.decode(remsg)
            print(remsg)
            if "exit" in msg:
                break

    def create_connection(self):
        self.connection = True
        self.sock.connect((self.ip, self.port))
        hello = str(self.name) + " is online now"
        self.sock.sendto(str.encode(hello), (self.ip, self.port))

    def close_connection(self):
        self.connection = False
        self.sock.close()
