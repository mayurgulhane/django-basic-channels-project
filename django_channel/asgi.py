"""
ASGI config for django_channel project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
# from apk.consumers import MyConsumer
from notification_apk.consumers import MyConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_channel.settings')

# application = get_asgi_application()
django_application = get_asgi_application()

ws_patterns = [
    path('ws/test/', MyConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    'http': django_application,
    'websocket': URLRouter(ws_patterns)
})
