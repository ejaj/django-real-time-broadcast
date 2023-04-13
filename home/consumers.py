import json
from random import randint
# from time import sleep
from asyncio import sleep
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer


class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        for i in range(1000):
            self.send(json.dumps({'message': randint(1, 100)}))
            # sleep(1)


class WSGraphConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        for i in range(1000):
            await self.send(json.dumps({'value': randint(1, 100)}))
            await sleep(1)


class WSJokeConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add('jokes', self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard('jokes', self.channel_name)

    async def send_jokes(self, event):
        text_message = event['text']
        await self.send(text_message)
