import json

from channels.generic.websocket import WebsocketConsumer
from channels.db import database_sync_to_async
from chat.models import Room, Message

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        print("Connecting ....................")
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        print("Recive..........")
        self.send(text_data=json.dumps({"message": "Message received successfully!!!!!"}))

    @database_sync_to_async
    def save_message(self, room_name):
        Room.objects.create(
            name=room_name
        )
    
