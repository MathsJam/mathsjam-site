---
layout: default
title: MathsJam
body_class: home
---
<style>
#next-jam .cities {
    list-style: none;
    padding: 0;
    display: inline;
}
#next-jam .cities > li {
    display: inline;
}
</style>

**MathsJam** is a monthly opportunity for like-minded self-confessed maths enthusiasts to get together in a pub and share stuff they like. Puzzles, games, problems, or just anything they think is cool or interesting.

We meet on the second to last Tuesday of every month, from 7pm in the evening. Events happen simultaneously in locations around the UK (and the world!) For more details of local events, click the links above, or visit the [map of current and potential MathsJams](http://maps.google.co.uk/maps/ms?msid=214012769649505046179.0004b5d8a1a1ec562c2f2&amp;msa=0&amp;ll=53.304621,-2.384033&amp;spn=5.561865,16.907959). You can follow our activity by looking at the [@MathsJam](http://www.twitter.com/mathsjam) twitter feed.

<div id="next-jam" class="content-block">
    <p>The next MathsJam evening is <span class="date">Tuesday 13<sup>th</sup> December</span> in</p>
    <ol class="cities">{% for city in site.cities %}{% if not city.hiatus %}<li><a href="{{site.url}}{{city.url}}">{{city.city_name}}</a></li>{% if not loop.last %}{% if loop.index == loop.length-1 %} and {% else %}, {% endif %}{% endif %}{% endif %}{% endfor %}</ol>.
</div>

Please note, the information on this website is not guaranteed to be correct - the individual MathsJams are organised locally, and details/meetings can change from month to month. If you're not sure, check the local page using the menu above, and contact your local MathsJam organiser by emailing <u>[city name]@mathsjam.com</u> for a reminder and updates. If any of the MathsJams stop running, please let us know by emailing [katie@mathsjam.com](mailto:katie@mathsjam.com) as soon as possible.

If there isn't an event in your area, and you'd like there to be one, please email [**katie@mathsjam.com**](katie@mathsjam.com) for details of how you can set one up!

MathsJam also runs an **annual gathering** which takes place every November. More information about the gatherings can be found [on the gathering pages]({{site.url}}gathering).
