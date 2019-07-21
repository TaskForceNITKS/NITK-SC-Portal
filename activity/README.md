# Activity App

The activity app contains files required for student-activities page

# What it does

It displays the object from the Crew model on the webpage.
Each object is displayed on the webpage based on the section field in the model.

## How to get data from json file into the model

The activities.json file is located at activities_list/activities.json

1. When initially running migrate, a data migration will load the data from the json file into the model.
2. After that whenever you change the database, to update the model run the following.
```console
/NITK-SC-Portal$ python manage.py shell < ./activity/activities_list/sync_list.py
```
Note: If you change the location of the activities.json file please update the file location in
* ./activity/activities_list/sync_list.py 
* ./migration/0002_auto_20190721_0121.py

## Dynamic content in activites.html template

The following code in activities.html allows for dynamic content
```django
{% include "activities/group.html" with activities_list=tech_club only %}
```
## Sections

Different section number are given to arrange the different objects on the webpage
This is important to note for giving giving the proper value for section in the json file

For Technical Clubs Section is 1
For Cultural Clubs Section is 2
For Fests Section is 3
For Sports Section is 4
For Others Section is null

This is used to filter the objects in views.py
