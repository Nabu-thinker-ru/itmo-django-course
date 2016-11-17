# -*- encoding: utf-8 -*-
import datetime

from city.models import Country, City

def cities(request):

    countries = Country.objects.filter(show = True)
    objects = {}
    for country in countries:
        objects[country] = country.cities.filter(show = True)

    return {'countries': objects,}
