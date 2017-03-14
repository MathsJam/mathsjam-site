# [The MathsJam website](https://www.checkmyworking.com/misc/new-mathsjam/)

This repository contains the source files to generate the MathsJam website.

## Changing something

* Find the file you want to edit, and click the `Edit` button. 
* Make your changes, then describe what you've done in the text field at the bottom and click "Propose file change".
* This will create a *pull request*, which one of the admins has to approve. They might request further changes or make their own edits.

## Organisation of the repository

Information about each city is stored in a file in the `cities` folder. 

Other pages are generated from `.md` files in the repository. The front page is generated from `index.md`.

### To add a city

Create a file `cities/cityname.md`, following this template:

```
---
layout: city                                           
city_name: CityName
jam_name: CityName MathsJam
email: cityname@mathsjam.com
organiser:
    name: Organiser's name
    email: cityname@mathsjam.com
location:
    group: england/rest-of-uk/north-america/rest-of-world
    pub_name: "Ye Pub"
    description: " on X Street"
    url: http://www.yepub.website
    lon: 1.00000000 (get the lat and long from google maps)
    lat: 50.0000000
hiatus: False (change to True if the Jam is not currently running)
---
```

All the data from this file will be used to create the page for the Jam, and all other references to the city throughout the site.

## Responsible people

* Christian Lawson-Perfect ([@christianp](http://github.com/christianp))
* Katie Steckles ([@katiesteckles](http://github.com/katiesteckles))
