from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Users, Games
from .forms import SignUpForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
from django.contrib.auth.decorators import login_required
from ttt_app.utils.ttt_enums import GameState, GameResult
from django.utils import timezone
# Create your views here.


def index(request):
    return render(request, 'ttt_app\index.html')

def home(request):
    if request.user.is_authenticated:
        return render(request, 'ttt_app\home.html', {'name': request.user.name})
    else:
        return redirect('login')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=email, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'ttt_app\\signup.html', {'form': form})

def game(request, game_id):
    return HttpResponse(f"You are playing game {game_id}")

def room(request, room_name):
    return render(request, 'ttt_app\\room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })

def chat_index(request):
    return render(request, 'ttt_app\\chat_index.html', {})

def view_all_users(request):
    all_users = Users.objects.all()
    return render(request, 'ttt_app\\all_users.html', {'all_users_list': all_users})

@login_required()
def user_statistics(request):
    user_info = Users.objects.get(email=request.user.email)
    games_related_to_user = user_info.games.all()

    return render(request, 'ttt_app\\user_statistics.html', {'user_info': user_info,
                                                             'number_of_games': len(games_related_to_user),
                                                             'ongoing_games': len([game for game in games_related_to_user if (game.game_state != GameState.NotStarted and game.game_state != GameState.Finished)]),
                                                             'number_of_winnings': len(user_info.games.filter(game_state=GameState.Finished.value, winner=user_info.email)),
                                                             'number_of_losses': len(games_related_to_user.filter(game_state=GameState.Finished.value).exclude(winner=user_info.email)),
                                                             'number_of_draws': len(games_related_to_user.filter(game_state=GameState.Finished.value, winner='none')),
                                                             'times_played_as_x': len(games_related_to_user.filter(x_player=user_info.email)),
                                                             'times_played_as_circle': len(games_related_to_user.filter(circle_player=user_info.email)),

                                                             })

def game(request):
    return render(request, 'ttt_app\\game.html', {})

def start_game(request):
    games_pending_for_second_user = Games.objects.get(game_state=GameState.NotStarted)
    if len(games_pending_for_second_user) > 0:
        return render(request, '', {'game': games_pending_for_second_user[0]})
    else:
        new_game = Games(game_start_time=timezone.now(),
                         board_state='{[],[],[]}',
                         )