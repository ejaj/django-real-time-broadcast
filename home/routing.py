from django.urls import path

from .consumers import WSConsumer, WSGraphConsumer, WSJokeConsumer

ws_urlpatterns = [
    path('ws/notifiation/', WSConsumer.as_asgi()),
    path('ws/graph/', WSGraphConsumer.as_asgi()),
    path('ws/joke/', WSJokeConsumer.as_asgi()),
]
