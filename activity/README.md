# Team App

The team app contains files required for know-your-council page

# What it does

It displays the object from the Member model on the webpage.
Each object is displayed on the webpage based on the group field in the model.

## How to get data from json file into the model

The members.json file is located at members_list/members.json

1. When initially running migrate, a data migration will load the data from the json file into the model.
2. After that whenever you change the database, to update the model run the following.
```console
/NITK-SC-Portal$ python manage.py shell < ./team/members_list/sync_list.py 
```
Note: If you change the location of the members.json file please update the file location in
* ./team/members_list/sync_list.py 
* ./migration/0002_auto_20190617_1307.py

## Dynamic content in council.html template

The following code in council.html allows for dynamic content
```django
{% include "team/group.html" with group_title="Heading for each group of council memebers" member_list=name_of_query_set_from_views.py only %}
```
## Groups

Each Member model object has a group field which is one of the following
'core',  
'engineer',  
'incident',  
'cr-1',  
'cr-2',  
'cr-3',  
'cr-4',  
'cr-pg',  
'cr-phd',  
'phd-pg-advisory',  
'acadamic-advisory',  
'student-activites-advisory'  
'sports-advisory',  
'alumni-advisory',  
'hostel-advisory',  
'club-con',  
'sports-cap',  
'hostel-rep',  
'alumni-coordinator'

This is used to filter the objects in views.py
