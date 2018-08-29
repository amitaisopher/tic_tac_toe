from django.conf.urls import url
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from . import consumers

websocket_urlpatterns = [
    url(r'^ws/ttt/(?P<room_name>[^/]+)/$', consumers.ChatConsumer),
]

application = ProtocolTypeRouter({

    "websocket": AuthMiddlewareStack(
        URLRouter([
            url(r'^ws/ttt/userStatistics/$', consumers.StatisticsConsumer),
            url(r'^ws/ttt/(?P<room_name>[^/]+)/$', consumers.ChatConsumer),
        ])
    ),

})