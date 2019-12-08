from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from sightings.models import Squirrel
from sightings.forms import SquirrelForm
from django.db.models import Count

def all(request):
    squirrels = Squirrel.objects.all()
    context = {            
            's': squirrels, 
            }
    return render(request, 'sightings/all.html', context)

def add(request):
    if request.method == 'POST':
        form = SquirrelForm(request.POST)
        if form.is_valid():
            new = form.save()
            return redirect('/sightings')
    else:
        form = SquirrelForm()
    context = {
            'form': form,
                }
    return render(request, 'sightings/add.html', context)

def map(request):
    squirrels = Squirrel.objects.all()
    context = {
            's': squirrels,
            }
    return render(request, 'sightings/map.html', context)

def edit(request, unique_squirrel_id):
    squirrels = Squirrel.objects.get(unique_squirrel_id = unique_squirrel_id)
    if request.method == 'POST':
        form = SquirrelForm(request.POST, instance = squirrels)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/{unique_squirrel_id}')
    else:
        form = SquirrelForm(instance = squirrels)
    context = {
            'form': form,
                }
    return render(request, 'sightings/edit.html', context)


def stats(request):
    agelist=Squirrel.objects.values("age").annotate(count=Count("age")).order_by()
    shiftlist=Squirrel.objects.values("shift").annotate(count=Count("shift")).order_by()
    primary_fur_colorlist=Squirrel.objects.values("primary_fur_color").annotate(count=Count("primary_fur_color")).order_by()
    datelist=Squirrel.objects.values("date").annotate(count=Count("date")).order_by()
    Runninglist=Squirrel.objects.values("running").annotate(count=Count("running")).order_by()
    chasinglist=Squirrel.objects.values("chasing").annotate(count=Count("chasing")).order_by()
    context={
        "agelist":agelist,
        "shiftlist":shiftlist,
        "primary_fur_colorlist":primary_fur_colorlist,
        "datelist":datelist,
        "Runninglist":Runninglist,
        "chasinglist":chasinglist,
    }

    return render(request,'/sightings/stats.html',context)


