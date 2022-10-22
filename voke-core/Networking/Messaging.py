
import traceback
from Utils.Logger import Logger


class Messaging:
    @staticmethod
    def writeHeader(type, length, version):
        buffer = b''
        buffer += int.to_bytes(type, 2, "big")
        buffer += int.to_bytes(length, 3, "big")
        buffer += int.to_bytes(version, 2, "big")
        return buffer

    @staticmethod
    def readHeader(buffer):
        return int.from_bytes(buffer[:2], "big"), int.from_bytes(buffer[2:5], "big"), int.from_bytes(buffer[5:], "big")

    @staticmethod
    def sendMessage(type, fields):
        from Logic.LogicLaserMessageFactory import LogicLaserMessageFactory
        m = LogicLaserMessageFactory().createMessageByType(type,b'')
        try:
            m.encode()
        except:
            print(traceback.format_exc())
            Logger().log("red", f"Error | Cannot encode this type of packet: {type}")
            return
        m.messageBuffer += Messaging.writeHeader(type, len(m.messagePayload), 0)
        m.messageBuffer += m.messagePayload
        try:
            fields["Client"].send(m.messageBuffer)
        except:
            Logger().log("red", f"Client | Cannot send message type of {type}. There is no client to send.")
