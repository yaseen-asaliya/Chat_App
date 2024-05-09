"""
ASGI config for webscoket project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
from chat.routing import websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webscoket.settings')

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        # "websocket": AuthMiddlewareStack(
        #     AuthMiddlewareStack(URLRouter(websocket_urlpatterns))
        # ),
        "websocket": AuthMiddlewareStack(
            # Route WebSocket connections to the appropriate consumer
            URLRouter(
                websocket_urlpatterns  # Include your WebSocket URL patterns here
            )
    ),
    }
    
)