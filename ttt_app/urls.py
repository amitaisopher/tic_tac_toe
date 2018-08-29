from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^chatIndex/$', views.chat_index, name='chat_index'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', auth_views.login, {'template_name': 'ttt_app/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^userStatistics/$', views.user_statistics, name='user_statistics'),
    url(r'^startGame/$', views.start_game, name='start_game'),
    url(r'^game/$', views.game, {}),
    url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
    path('game/<int:game_id>/', views.game, name='game'),
    path('viewAllUsers', views.view_all_users, name='viewAllUsers')
]