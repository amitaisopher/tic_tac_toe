from django.db import models
from ttt_app.utils import ttt_enums
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Games(models.Model):
    game_start_time = models.DateTimeField()
    game_moves_counter = models.IntegerField(default=0)
    board_state = models.CharField(max_length=200)
    game_state = models.IntegerField(default=ttt_enums.GameState.NotStarted )
    x_player = models.TextField()
    circle_player = models.TextField()
    player_of_next_move = models.TextField()
    winner = models.TextField(default="no winner yet")


class MyUserManager(BaseUserManager):
    """
    A custom user manager to deal with emails as unique identifiers for auth
    instead of usernames. The default that's used is "UserManager"
    """
    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)


class Users(AbstractBaseUser, PermissionsMixin):
    name = models.TextField()
    user_moves_counter = models.IntegerField(default=0)
    total_number_of_gmaes = models.IntegerField(default=0)
    number_played_as_x = models.IntegerField(default=0)
    number_played_as_circle = models.IntegerField(default=0)
    games = models.ManyToManyField(Games, through='UsersToGames')
    email = models.EmailField(unique=True, null=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    USERNAME_FIELD = 'email'
    objects = MyUserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        return f"name: {self.name}, email: {self.email}"

class UsersToGames(models.Model):
    user_email = models.ForeignKey(Users, on_delete=models.CASCADE)
    game_id = models.ForeignKey(Games, on_delete=models.CASCADE)
    date_joined = models.DateTimeField()
    user_selected_shape = models.IntegerField()
