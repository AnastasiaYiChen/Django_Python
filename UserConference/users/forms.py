from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

MEAL_CHOICES= [
    ('chinese food', 'Chinese Food'),
    ('french meal', 'French Meal'),
    ('fish and potatoes', 'Fish and Potatoes'),
    ('vegetarian diet ', 'Vegetarian Diet '),
    ]

class UserRegisterForm(UserCreationForm):


    first_name = forms.CharField(label='First name', max_length=100)
    last_name = forms.CharField(label='Last name', max_length=100)
    phone_number = forms.IntegerField()
    address = forms.CharField(label='address', max_length=100)
    meal_preference = forms.CharField(label='What is your favorite meal?', widget=forms.Select(choices=MEAL_CHOICES))
    registration_date = forms.DateField()


    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'phone_number', 'address', 'meal_preference',
                  'password1', 'password2', 'registration_date']
