from DataStream.ByteStream import ByteStream
from Networking.Messaging import Messaging
from Utils.Logger import Logger


class ClientHelloMessage(ByteStream):
    def __init__(self, messageBuffer, unknown=0):
        super().__init__(messageBuffer, unknown)



    def decode(self):
        self.readInt()
        self.keyVersion = self.readInt()
        self.readInt()
        self.clientSeed = self.readInt()
    def process(self, client):
        fields = {"Client": client}
        Messaging().sendMessage(20100, fields)

