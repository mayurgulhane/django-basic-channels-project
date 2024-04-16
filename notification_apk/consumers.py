from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json

class MyConsumer(WebsocketConsumer):
    def connect(self):
       # backend to frontend  
       self.room_name = "my_consumer"
       self.room_group_name = "my_consumer_group"
       async_to_sync(self.channel_layer.group_add)(
           self.room_group_name, 
           self.channel_name,
       )
       self.accept()

       self.send(text_data=json.dumps({'status': 'connected from Django Channel'}))

    def receive(self,text_data):
        # frontend to backend
        print(text_data)
        self.send(text_data=json.dumps({'status': 'We got you'}))

    def disconnect(self, *args, **kwargs):
        print("Disconnecting from Django Channel....")

    def send_notification(self, event):
        data = json.loads(event.get('value'))
        self.send(text_data=json.dumps({'payload': data}))
        print(event)