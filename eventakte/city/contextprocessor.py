# -*- encoding: utf-8 -*-
import datetime

from city.models import Country, City

def cities(request):

    countries = Country.objects.all()

    return {'countries':countries,}
