from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Users

class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields.pop('password2')

    name = forms.CharField(max_length=30, help_text='Required. Please enter your full name.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = Users
        fields = ('name', 'email', 'password1')