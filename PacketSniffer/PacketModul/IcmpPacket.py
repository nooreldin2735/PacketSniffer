from PacketModul.Packet import Packet


import struct

class IcmpPacket(Packet):
  def __init__(self) -> None:
    super().__init__()
      
  def icmp_packet(self):
    icmp_type,code,checksum=struct.unpack('! B B H',self.data[:4])
    return icmp_type,code,checksum,self.data[4:]

