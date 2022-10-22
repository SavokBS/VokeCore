
import socket, select
from Networking.Connection import Connection

from Utils.Logger import Logger


class Server:
    def __init__(self, port):
        self.port = port
        self.sock = socket.socket()
        self.sock.setblocking(0)
        self.clients = {self.sock: None}


    def listen(self):
        log = Logger()
        self.sock.bind(("0.0.0.0", self.port))
        self.sock.listen()
        log.log("green", f"Server | Server started on port {self.port}")

        while(True):
            read, write, except_ = select.select(self.clients, [], self.clients)
            for i in read:
                if i == self.sock:
                    client, address = self.sock.accept()
                    client.setblocking(1)
                    log.log("purple", f"Client | New connection - {address}")
                    self.clients[client] = Connection(client)
                else:
                    try:
                        self.clients[client].receive()
                    except:
                        self.disconnect(client)



                    

        
        