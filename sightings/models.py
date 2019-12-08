from django.db import models
from django.urls import reverse

class Squirrel(models.Model):
    x = models.DecimalField(
            max_digits = 20,
            decimal_places = 14,
            null = True,
            )
    y = models.DecimalField(
            max_digits = 20,
            decimal_places = 14,
            null = True,
            )
    unique_squirrel_id = models.CharField(
            max_length = 24,
            primary_key=True,
            )
    hectare = models.CharField(
            max_length = 16,
            default = None,
            blank = True,
            null = True,
            )
    shift = models.CharField(
            max_length = 16,
            default = None,
            blank = True,
            null = True,
            )
    date = models.CharField(
            max_length = 20,
            default = 0,
            blank = True,
            null = True,
            )
    hectare_squirrel_number = models.IntegerField(
            default = 0,
            blank = True,
            null = True,
            )
    age = models.CharField(
            max_length = 16,
            default = None,
            blank = True,
            null = True,
            )
    primary_fur_color = models.CharField(
            max_length = 16,
            default = None,
            blank = True,
            null = True,
            )
    highlight_fur_color = models.CharField(
            max_length = 16,
            default = None,
            blank = True,
            null = True,
            )
    combination_of_primary_and_highlight_color = models.CharField(
            max_length = 256,
            default = None,
            blank = True,
            null = True,
            )
    color_notes = models.CharField(
            max_length = 256,
            default = None,
            blank = True,
            null = True,
            )
    location = models.CharField(
            max_length = 256,
            default = None,
            blank = True,
            null = True,
            )
    above_ground_sighter_measurement = models.CharField(
            max_length = 256,
            default = None,
            blank = True,
            null = True,
            )
    specific_location = models.CharField(
            max_length = 256,
            default = None,
            blank = True,
            null = True,
            )
    running = models.BooleanField(
            default = None,
            blank = True,
            null = True,
            )
    chasing = models.BooleanField(
            default = None,
            blank = True,
            null = True,
            )
    climbing = models.BooleanField(
            default = None,
            blank = True,
            null = True,
            )
    eating = models.BooleanField(
            default = None,
            blank = True,
            null = True,
            )
    foraging = models.BooleanField(
            default = None,
            blank = True,
            null = True,
            )
    other_activities = models.CharField(
            max_length = 256,
            default = None,
            null = True,
            blank = True,
            )
    kuks = models.BooleanField(
            default = None,
            blank = True,
            null = True,
            )
    quaas = models.BooleanField(
            default = None,
            blank = True,
            null = True,
            )
    moans = models.BooleanField(
            default = None,
            blank = True,
            null = True,
            )
    tail_flags = models.BooleanField(
            default = None,
            blank = True,
            null = True,
            )
    tail_twitches = models.BooleanField(
            default = None,
            blank = True,
            null = True,
            )
    approaches = models.BooleanField(
            default = None,
            blank = True,
            null = True,
            )
    indifferent = models.BooleanField(
            default = None,
            blank = True,
            null = True,
            )
    runs_from = models.BooleanField(
            default = None,
            blank = True,
            null = True,
            )
