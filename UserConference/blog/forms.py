from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from blog.models import Post, Selection



CONFERENCE_CHOICES = []
for y in Post.objects.all():
    CONFERENCE_CHOICES.append((y, y))

print(CONFERENCE_CHOICES)

print(type(Post.objects.all()))


class CreateListForm(ModelForm):
    tag = forms.CharField(label='Tag', max_length=100)
    conference_preference = forms.CharField(label='Do you want to select a conference and event?',
                                            widget=forms.Select(choices=CONFERENCE_CHOICES))

    class Meta:
        model = Selection
        fields = ['tag', 'conference_preference']
