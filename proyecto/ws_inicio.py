import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class consumer_inicio(WebsocketConsumer):
    def connect(self):
        print('Conectado Upload')
        self.room_group_name = 'upload'
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        print('Desconectado')
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        print('Recibe')
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'mensaje_todo_grupo',
                'message': str(message)
            }
        )
    # Receive message from room group
    def mensaje_todo_grupo(self, event):
        message = event['message']
        self.send(text_data=json.dumps({
            'message': message
        }))
