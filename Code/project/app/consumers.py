from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
from time import sleep

class MySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print('Websocket Connected...', event)

        self.send({
            'type' : 'websocket.accept'
        })

    def websocket_receive(self, event):
        print('Message received...', event)
        print('The received message is: ', event['text'])

        for i in range(10):
            self.send({
                'type' : 'websocket.send',
                'text' : f'Message {i} to client.'
            })
            sleep(1)

        # self.send({
        #     'type' : 'websocket.send',
        #     'text' : 'Message to client'
        # })

    def websocket_disconnect(self, event):
        print('Websocket disconnected...', event)
        raise StopConsumer()

class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print('Websocker Connected...', event)

        await self.send({
            'type' : 'websocket.accept'
        })

    async def websocket_receive(self, event):
        print('Message received...', event)
        print('The received message is: ', event['text'])

        for i in range(10):
            await self.send({
                'type' : 'websocket.send',
                'text' : f' Async Message {i} to client'
            })
            sleep(1)

        # await self.send({
        #     'type' : 'websocket.send',
        #     'text' : 'Message to client'
        # })

    async def websocket_disconnect(self, event):
        print('Websocket disconnected...', event)
        raise StopConsumer()