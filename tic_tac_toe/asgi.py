import os
from channels import asgi

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tic_tac_toe.settings")
channel_layer = channels.asgi.get_channel_layer()