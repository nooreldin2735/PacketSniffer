from django.http import response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from PacketModul.Sniffer import Sniffer

@api_view(['GET'])
def Sniff(req):
  sniffer=Sniffer()
  
  return Response({'Packet':sniffer.sniff()})
