import socket
import pickle
from multiprocessing import Process

DEBUG = True


class Network:
    def __init__(self, ip, TB):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = ip
        self.port = 55556
        self.TransferBytes = TB
        self.addr = (self.server, self.port)

    def connect(self):
        #try:
            print(f"Connecting to {self.server}")
            self.client.connect(self.addr)
            print(f"Connection successful")
            return True
        #except:
            #return False

    def send(self, data):
        #print(f"Sent data | {data}")
        try:
            self.client.send(pickle.dumps(data))
        except socket.error as e:
            print(e)

    def recv(self, id=False):
        try:
            temp = self.client.recv(self.TransferBytes)

            #temp = temp.decode("utf-8") if id==False else temp.from_bytes(2,"little")
            send = ''

            send = pickle.loads(temp)

            return send
        except socket.error as e:
            print(e)
            return False
