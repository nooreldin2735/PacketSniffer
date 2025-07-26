# snifferapi/Hub.py
from channels.generic.websocket import WebsocketConsumer
from PacketModul.Sniffer import Sniffer
import json
import threading
import time

class Hub(WebsocketConsumer):

    def connect(self):
        self.accept()
        self.send(text_data=json.dumps({
            'type': 'connection_established',
            'message': 'User Connected'
        }))

        self.running = True
        self.sniffer = Sniffer()
        self.sniff_thread = threading.Thread(target=self.send_packets)
        self.sniff_thread.start()

    def disconnect(self, close_code):
        self.running = False

    def send_packets(self):
        while self.running:
            try:
                packet_data = self.sniffer.sniff()
                self.send(text_data=json.dumps({
                    'type': 'packet',
                    'data': packet_data
                }))
                time.sleep(2)  # To avoid overwhelming the browser/UI
            except Exception as e:
                self.send(text_data=json.dumps({
                    'type': 'error',
                    'message': str(e)
                }))
                break

