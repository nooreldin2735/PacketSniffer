import socket
from PacketModul import Ipv4Packet
from PacketModul import IcmpPacket 
import struct

class Sniffer:

  def __init__(self) -> None:
  
    self.conn=socket.socket(socket.AF_PACKET,socket.SOCK_RAW,socket.htons(3))
    self.ipv4_packet=Ipv4Packet.Ipv4Packet()
    self.icmp_packet=IcmpPacket.IcmpPacket()

    
  def GetEthernetFrame(self,data):
    dest_mac,src_mac,proto=struct.unpack('! 6s 6s H',data[:14])

    # socket.htons(proto) does convert the network short in to type and then data[14:] return the rest of the packet 
    #skipping the Header and return the payload

    return self.get_mac_addr(dest_mac),self.get_mac_addr(src_mac),socket.htons(proto),data[14:]

  def get_mac_addr(self,mac_addr):
    bytes_chunk=map('{:02x}'.format,mac_addr)
    return ':'.join(bytes_chunk)
  def sniff(self):
      raw_data, _ = self.conn.recvfrom(65536)
      result = {}

      dest_mac, src_mac, eth_protocol, data = self.GetEthernetFrame(raw_data)
      result["ethernet"] = {
          "destination_mac": dest_mac,
          "source_mac": src_mac,
          "protocol": eth_protocol,
          "payload": data.hex()
      }

      # 8 means IPv4
      if eth_protocol == 8:
          self.ipv4_packet.init_data(data)
          version, header_length, ttl, proto, src_ip, target_ip, ipv4_payload = self.ipv4_packet.get_ipv4_addr()

          result["ipv4"] = {
              "version": version,
              "header_length": header_length,
              "ttl": ttl,
              "protocol": proto,
              "source_ip": src_ip,
              "target_ip": target_ip,
              "payload": ipv4_payload.hex()
          }

          # ICMP (proto 1 inside IPv4)
          if proto == 1:
              self.icmp_packet.init_data(ipv4_payload)
              icmp_type, code, checksum, icmp_data = self.icmp_packet.icmp_packet()

              result["icmp"] = {
                  "type": icmp_type,
                  "code": code,
                  "checksum": checksum,
                  "data": icmp_data.hex()
              }

      return result



