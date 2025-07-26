import struct
class Packet:

  def __init__(self) -> None:

    self.data=None
    self.src_mac=None
    self.des_mac=None
    self.eth_protcol=None
  def init_data(self,data):
    self.data=data
