# :hamster: Squirrel-Tracking Application ![](https://img.shields.io/badge/License-Mozilla%20v2.0-blue) ![](https://img.shields.io/badge/Environment-Django-yellowgreen)  ![](https://img.shields.io/badge/Build-passing-red)

## Group Name and Section

Tools for Analytics (SEC2)

Project Group 45

Zhicheng Cao (zc2500);
Han Wang (hw2752)

UNIs: [zc2500, hw2752]

Deployed URLs: https://zc2500toolsforanalytics.appspot.com/

The web suffix for each function (feature) are:

admin/

sightings/add/

map/

sightings/

sightings/<unique_squirrel_id>/

sightings/stats

## Background

This is the FINAL PROJECT of Tools for Analytics. 

This is a real story...

Long long ago, eccentric billionaire Joffrey Hosencratz purchased the web development company you work for. We had met him once in an elevator and he was impressed with our skill in developing web applications with the Django framework. He also relayed that his most recent trip to Sedona, AZ has left him in a bit of trouble. See, he fancies the show Rick and Morty and a particular scene coupled with a traumatic childhood squirrel experience and a bad crystal bath experience in Sedona as left him wanting. 

He would like to start keeping track of all the known squirrels and plans to start with Central Park. He’s asked us to build an application that can import the 2018 Central Park Squirrel Census data and allow his team to add, update, and view squirrel data. 

## Install

This project uses Django and Python. Go check them out if you don't have them locally installed or VM installed if you want to make more modify on this project.

'$ sudo apt-get install python-pip'

## Usage

This is mainly two folders in this repository. The folder "sightings" is the App documents, which is to achieve the functions we need. 

We have deployed on Google Cloud and you can acknown and use this project by entering the URLs we provide (Suggested).  You can also use this project by using the common method.

## Features

The features we successfully achieve are the following:

Import: A command that can be used to import the data from the 2018 census file (in CSV format). The file path should be specified at the command line after the name of the management command. 

Export: A command that can be used to export the data in CSV format. The file path should be specified at the command line after the name of the management command. 

Views:
- A view that shows a map that displays the location of the squirrel sightings on an OpenStreets map.
- A view that lists all squirrel sightings with links to edit each
- A view to update a particular sighting
- A view to create a new sighting
  Fields supported:
    Latitude
    Longitude
    Unique Squirrel ID
    Shift
    Date
    Age
    Primary Fur Color
    Location
    Specific Location
    Running
    Chasing
    Climbing
    Eating
    Foraging
    Other Activities
    Kuks
    Quaas
    Moans
    Tail flags
    Tail twitches
    Approaches
    Indifferent
    Runs from
- A view with general stats about the sightings

Deployed URLs: https://zc2500toolsforanalytics.appspot.com/

The web suffix for each function (feature) are:

admin/

sightings/add/

map/

sightings/

sightings/<unique_squirrel_id>/

sightings/stats

## Maintainers:
@tonycao5
@hw2752

## License:
Mozilla Public License, v. 2.0.
