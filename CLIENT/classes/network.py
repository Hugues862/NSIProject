import socket
import pickle
TransferBytes = 1024*2


class Network:
    def __init__(self, ip):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = ip
        self.port = 5555
        self.addr = (self.server, self.port)

    def connect(self):
        try:
            self.client.connect(self.addr)
            return True
        except:
            return False

    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
        except socket.error as e:
            print(e)

    def recv(self, id=False):
        try:
            temp = self.client.recv(TransferBytes)
            #temp = temp.decode("utf-8") if id==False else temp.from_bytes(2,"little")
            send = ''

            send = pickle.loads(temp)
            return send
        except socket.error as e:
            print(e)
            return False
