from django.db import models
from django.urls import reverse
# Create your models here.

class Squirrel(models.Model):

    x = models.DecimalField(

            max_digits=2000,

            decimal_places=20,

            default=None,

            blank=True,

            help_text=_('Latitude'),

            null=True,

            )



    y = models.DecimalField(

            max_digits=2000,

            decimal_places=20,

            default=None,

            blank=True,

            help_text=_('Longitude'),

            null=True,

            )



    unique_squirrel_id = models.CharField(

            max_length=20,

            default=None,

            primary_key=True,

            blank=True,

            )



    hectare = models.CharField(

            max_length=10,

            default=None,

            blank=True,

            null=True,

            )



    shift = models.CharField(

            max_length=10,

            default=None,

            blank=True,

            null=True,

            )



    date = models.CharField(

            max_length=20,

            default=0,

            blank=True,

            null=True,

            )



    hectare_squirrel_number = models.IntegerField(

            default=0,

            blank=True,

            null=True,

            )



    age = models.CharField(

            max_length=8,

            default=None,

            blank=True,

            null=True,

            )



    primary_fur_color = models.CharField(

            max_length=8,

            default=None,

            blank=True,

            null=True,

            )



    highlight_fur_color = models.CharField(

            max_length=8,

            default=None,

            blank=True,

            null=True,

            )



    combination_of_primary_and_highlight_color = models.CharField(

            max_length=100,

            default=None,

            blank=True,

            null=True,

            )



    color_notes = models.CharField(

            max_length=100,

            default=None,

            blank=True,

            null=True,

            )



    location = models.CharField(

            max_length=100,

            default=None,

            blank=True,

            null=True,

            )



    above_ground_sighter_measurement = models.CharField(

            max_length=10,

            default=None,

            blank=True,

            null=True,

            )



    specific_location = models.CharField(

            max_length=100,

            default=None,

            blank=True,

            null=True,

            help_text=_('specific location of squirrel'),

            )



    running = models.BooleanField(

            default=None,

            blank=True,

            null=True,

            help_text=_('whether the squirrel is running'),

            )



    chasing = models.BooleanField(

            default=None,

            blank=True,

            null=True,

            help_text=_('whether the squirrel is chasing'),

            )



    climbing = models.BooleanField(

            default=None,

            blank=True,

            null=True,

            help_text=_('whether the squirrel is climbing'),

            )



    eating = models.BooleanField(

            default=None,

            blank=True,

            null=True,

            help_text=_('whether the squirrel is eating'),

            )



    foraging = models.BooleanField(

            default=None,

            blank=True,

            null=True,

            help_text=_('whether the squirrel is foraging'),

            )



    other_activities = models.CharField(

            max_length=100,

            default=None,

            null=True,

            blank=True,

            )



    kuks = models.BooleanField(

            default=None,

            blank=True,

            null=True,

            help_text=_('whether the squirrel kuks'),

            )



    quaas = models.BooleanField(

            default=None,

            blank=True,

            null=True,

            help_text=_('whether the squirrel quaas'),

            )



    moans = models.BooleanField(

            default=None,

            blank=True,

            null=True,

            help_text=_('whether the squirrel moans'),

            )



    tail_flags = models.BooleanField(

            default=None,

            blank=True,

            null=True,

            help_text = _('whether the squirrel has tail flags'),

            )



    tail_twitches = models.BooleanField(

            default=None,

            blank=True,

            null=True,

            help_text = _('whether the squirrel has tail twitches'),

            )



    approaches = models.BooleanField(

            default=None,

            blank=True,

            null=True,

            help_text = _('whether the squirrel approaches'),

            )



    indifferent = models.BooleanField(

            default=None,

            blank=True,

            null=True,

            help_text = _('whether the squirrel is indifferent'),

            )



    runs_from = models.BooleanField(

            default=None,

            blank=True,

            null=True,

            help_text = _('whether the squirrel runs from'),

            )



    other_interactions = models.CharField(

            max_length=100,

            default=None,

            blank=True,

            null=True,

            )



    lat_long = models.CharField(

            max_length=100,

            default=None,

            blank=True,

            null=True,

            )



    zip_codes = models.CharField(

            max_length=100,

            default=None,

            blank=True,

            null=True,

            )



    community_districts = models.IntegerField(

            default=0,

            blank=True,

            null=True,

            )



    borough_boundaries = models.IntegerField(

            default=0,

            blank=True,

            null=True,

            )



    city_coucil_districts = models.IntegerField(

            default=0,

            blank=True,

            null=True,

            )



    police_precincts = models.IntegerField(

            default=0,

            blank=True,

            null=True,

            )

