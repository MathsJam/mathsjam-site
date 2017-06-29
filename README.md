# [The MathsJam website](https://mathsjam.com)

This repository contains the source files to generate the MathsJam website.

## Changing something

* You need a GitHub account to edit the site. If you don't have one, [sign up](https://github.com/join) first - it's free!
* Find the file you want to edit, and click the `Edit this file` button (it's a little pencil icon). The files for individual Jams are in the [`cities`](https://github.com/MathsJam/mathsjam-site/tree/master/cities) folder. Alternatively, each page on the site has an "edit this page" link at the bottom; clicking this will take you to the corresponding GitHub page.
* Make your changes, then describe what you've done in the text field at the bottom and click "Propose file change".
* This will allow you to create a *pull request*, which one of the admins has to approve. They might request further changes or make their own edits. When the pull request is approved, the change will be published to the site.

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
twitter: CityNameMathsJam
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
hiatus_months: (add this field if the Jam doesn't run for one or two months)
    - 2016-01
    - 2016-02
jam_date_rule: second-last tuesday
start_time: 7pm in the evening
---
```

All the data from this file will be used to create the page for the Jam, and all other references to the city throughout the site.

If your Jam doesn't meet on the second-last Tuesday of the month, you can add a line for 'jam_date_rule' and follow the convention of 'first/second/third/fourth(-last) Weekday', e.g. fourth Thursday, third-last Saturday. If you can't work out how to word it, do your best and we can fix it before merging.

If you need to put your MathsJam on hiatus for a single month, this is also possible - add the 'hiatus_months' field, and then on successible lines add the months for which you won't be meeting, in the format YYYY-MM, as in the example above. This will automatically add a note to the site and remove it again afterwards.

## Responsible people

* Christian Lawson-Perfect ([@christianp](http://github.com/christianp))
* Katie Steckles ([@katiesteckles](http://github.com/katiesteckles))
