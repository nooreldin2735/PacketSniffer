from django.urls import re_path
from .Hub import Hub 

websocket_urlpatterns=[
    re_path(r'ws/connect',Hub.as_asgi())
]
