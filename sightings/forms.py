from django import forms
from django.forms import ModelForm
from .models import Squirrel

class SquirrelForm(ModelForm):
    class Meta:
        model = Squirrel
        fields = ['x', 'y', 'unique_squirrel_id', 'shift', 'date', 'age',
                 'primary_fur_color', 'location', 'specific_location', 'running',
                 'chasing', 'climbing', 'eating', 'foraging', 'other_activities',
                 'kuks', 'quaas', 'moans', 'tail_flags', 'tail_twitches',
                 'approaches', 'indifferent', 'runs_from'] 
