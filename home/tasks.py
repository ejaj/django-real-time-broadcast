import requests
from celery import shared_task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

channel_layer = get_channel_layer()


@shared_task
def get_joke():
    url = 'https://api.chucknorris.io/jokes/random'
    response = requests.get(url).json()
    joke = response['value']

    async_to_sync(channel_layer.group_send)('jokes', {
        'type': 'send_jokes',
        'text': joke
    })
