from django.forms import ModelForm
from .models import Item
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Item1Form(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'