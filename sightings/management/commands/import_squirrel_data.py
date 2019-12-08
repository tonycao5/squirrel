from django.core.management.base import BaseCommand
from sightings.models import Squirrel
import csv
from  decimal import Decimal
class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('args', nargs='*', type = str)
    def handle(self, *args, **kwargs):
        path = args[0]
        insertlist=[]
        with open(path,"r", encoding="utf-8") as f:
            csv_reader = csv.reader(f)
            for row in csv_reader:
                for i in range(0,len(row)):
                    if row[i]=="false":
                        row[i]=False
                    if row[i]=="true":
                        row[i]=True
                    date=row[5]
                    newdate=date[-4:]+"-"+date[0:2]+"-"+date[2:4]
                try:
                    squirrel = Squirrel(x=Decimal(row[0]), y=Decimal(row[1]),
                    unique_squirrel_id=row[2], 
                    hectare=row[3],
                    shift=row[4], 
                    date=newdate, 
                    hectare_squirrel_number=row[6], 
                    age=row[7],
                    primary_fur_color=row[8], 
                    highlight_fur_color=row[9],
                    combination_of_primary_and_highlight_color=row[10], 
                    color_notes=row[11],
                    location=row[12],
                    above_ground_sighter_measurement=row[13], 
                    specific_location=row[14],
                    running=row[15], 
                    chasing=row[16], 
                    climbing=row[17], 
                    eating=row[18],
                    foraging=row[19],
                    other_activities=row[20], 
                    kuks=row[21], 
                    quaas=row[22],
                    moans=row[23],
                    tail_flags=row[24], 
                    tail_twitches=row[25], 
                    approaches=row[26],
                    indifferent=row[27],
                    runs_from=row[28], 
                    other_interactions=row[29], 
                    lat_long=row[30])
                    insertlist.append(squirrel)
                except:
                    continue
            Squirrel.objects.bulk_create(insertlist)


