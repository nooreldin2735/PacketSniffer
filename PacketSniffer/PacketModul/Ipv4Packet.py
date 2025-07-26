from PacketModul.Packet import Packet
import struct




class Ipv4Packet(Packet):

  def __init__(self) -> None:
    super().__init__()
    self.version_header=None
    self.header_length=None
    self.ttl=None
    self.proto=None
    self.srcIp=None
    self.targetIp=None
    
  def get_ipv4_addr(self):

    # inits area

    version_headerlength=self.data[0]
    version=version_headerlength >> 4
    header_lenght=(version_headerlength & 15 ) *  4
    ttl,proto,src,target=struct.unpack('! 8x B B 2x 4s 4s',self.data[:20])

    # data assigment section
    self.version_header=version
    self.header_length=header_lenght
    self.ttl=ttl
    self.proto=proto
    self.srcIp=self.ipv4(src)
    self.targetIp=self.ipv4(target)


    return version,header_lenght,ttl,proto,self.ipv4(src),self.ipv4(target),self.data[20:]


  def ipv4(self,addr):
    return '.'.join(map(str,addr))

