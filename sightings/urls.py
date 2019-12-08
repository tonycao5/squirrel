from django.urls import path
from . import views

urlpatterns = [
        path('sightings/add/', views.add),
        path('map/', views.map),
        path('sightings/', views.all),
        path('sightings/<str:unique_squirrel_id>/', views.edit),
        path('sightings/stats', views.stats),

]
