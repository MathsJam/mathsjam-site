---
layout: default
title: MathsJam
body_class: home
---

**MathsJam** is a monthly opportunity for like-minded self-confessed maths enthusiasts to get together in a pub and share stuff they like. Puzzles, games, problems, or just anything they think is cool or interesting.

We meet on the second-to-last Tuesday of every month, from 7pm in the evening, in locations around the world.

For more details of local events, choose your region from the menu, or visit the [find a jam]({{site.url}}/find-a-jam) page. 

<div id="next-jam" class="content-block">
    <p>The next MathsJam evening is:</p>
    {% for date,cities in group_cities_by_jam_date(site.cities) %}
    <p>
        <strong>{{date|show_date}}</strong>
        in 
        <span class="cities">{% for city in cities %}<span><a href="{{site.url}}{{city.url}}">{{city.city_name}}</a></span>{% if not loop.last %}{% if loop.index == loop.length-1 %} and {% else %}, {% endif %}{% endif %}{% endfor %}</span>.
    </p>
    {% endfor %}
</div>


If there isn't an event in your area, and you'd like there to be one, please email <a href="mailto:{{site.new_jam_contact.email}}">{{site.new_jam_contact.email}}</a> for details of how you can set one up!

**MathsJam is not for children.** MathsJam is an event for adults to meet and socialise, which is why they are mainly held in licensed premises, where under-18s are not allowed. Do let us know via <a href="mailto:katie@mathsjam.com">katie@mathsjam.com</a> if you come across an event for children being called "MathsJam", or you see MathsJam being promoted to young students. MathsJam&trade; is a registered trademark of Stand-up Maths Limited.

MathsJam also runs an **annual gathering** which takes place every November. More information about the gatherings can be found [on the gathering pages]({{site.url}}/gathering).

**Privacy Policy**
Each individual local MathsJam runs a small mailing list to remind attendees about each month's Jam. If you email the address given on the city's individual page, you can be added to the list. You'll get an email around once a month, reminding you about the Jam and possibly including details of other relevant local events the organiser thinks you might be interested in. Your name and email address will be stored securely, and if you wish to be removed at any time you can reply to the email and request this. Your data will not be shared with any other organisation or used for any other purpose.
