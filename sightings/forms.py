from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext as _
from .models import Squirrel

class SquirrelForm(ModelForm):
    class Meta:
        model = Squirrel
        fields =['x', 'y', 'unique_squirrel_id', 'shift', 'date', 'age',
                 'primary_fur_color', 'location', 'specific_location', 'running',
                 'chasing', 'climbing', 'eating', 'foraging', 'other_activities',
                 'kuks', 'quaas', 'moans', 'tail_flags', 'tail_twitches',
                 'approaches', 'indifferent', 'runs_from'] 
        labels = {
                'x': _('latitude'),
                'y': _('longitude'),
                'unique_squirrel_id': _('unique squirrel id'),
                'primary_fur_color': _('primary fur color'),
                'specific_location': _('specific location'),
                'other_activies': _('other activities'),
                'runs_from': _('runs from'),
                }
