
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Order, Costumer


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CostumerForm(ModelForm):
    class Meta:
        model = Costumer
        fields = '__all__'
        exclude = ['user']
