import socket
import traceback
from Logic.LogicLaserMessageFactory import LogicLaserMessageFactory

from Networking.Messaging import Messaging


class Connection:


    def __init__(self, client: socket.socket()):
        self.client = client 

    def recv(self, n):
        data = bytearray()
        while len(data) < n:
            packet = self.client.recv(n - len(data))
            if not packet:
                return b''
            data.extend(packet)
        return data

    
    def receive(self):
        try:
            m_header = self.client.recv(7)
            if len(m_header) > 0:
                m_type, m_length, m_ver = Messaging().readHeader(m_header)
                m_payload = self.recv(m_length)
                m = LogicLaserMessageFactory().createMessageByType(m_type, m_payload)
                try:
                    m.decode()
                    m.process(self.client)
                except:
                    print(traceback.format_exc())

        except Exception as e:
            print(traceback.format_exc())


    