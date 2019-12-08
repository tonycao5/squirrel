from django.core.management.base import BaseCommand, CommandError
from sightings.models import Squirrel
import csv

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('args', type = str, nargs = '+')

    def handle(self, *args, **kwargs):
        path = args[0]
        with open(path, 'w') as f:
            csv_writer = csv.writer(f)
            squirrelFields = Squirrel._meta.fields
            row = []
            for i in squirrelFields:
                row.append(str(i).replace("sightings.Squirrel.",""))
            csv_writer.writerow(row)
            for squirrel in Squirrel.objects.all():
                row = []
                for field in squirrelFields:
                    row.append(getattr(squirrel, field.name))
                csv_writer.writerow(row)
