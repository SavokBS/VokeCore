

from DataStream.ByteStream import ByteStream
from Networking.Messaging import Messaging
from Utils.Logger import Logger


class ServerHelloMessage(ByteStream):
    def __init__(self, messageBuffer, unknown=0):
        super().__init__(messageBuffer, unknown)

    def encode(self):
        self.writeBytes(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', 24)