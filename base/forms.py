from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import MainRoom, User


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['avatar', 'name', 'username', 'bio', 'email', 'password1', 'password2']

class MainRoomForm(ModelForm):
    class Meta:
        model = MainRoom
        fields = '__all__'
        exclude = ['host', 'participants']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'name', 'username', 'email', 'bio']