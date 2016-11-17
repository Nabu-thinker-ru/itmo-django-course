# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import City

import logging
logger = logging.getLogger(__name__)

def change_city_1(request, slug):
    try:
        city = City.objects.get(slug = slug)
    except City.DoesNotExist:
        raise Http404
    html = 'changed'
    return HttpResponse('Holla! Your choice is %s' % city)


def change_city_2(request, slug):
    from django.shortcuts import get_object_or_404
    city = get_object_or_404(City, slug = slug)

    from django.template.loader import get_template
    template = get_template('city/holla.html')
    html = template.render({'city':city})

    return HttpResponse(html)


def change_city_3(request, slug):
    from django.shortcuts import get_object_or_404, render
    city = get_object_or_404(City, slug=slug)

    city_pk = request.session.get('city_pk', None)

    context = {
        'city': city,
        'city_pk':city_pk,
    }

    request.session['city_pk'] = city.pk

    return render(request, 'city/ses.html', context)


def change_city_4(request, slug):
    from django.shortcuts import get_object_or_404, render
    city = get_object_or_404(City, slug=slug)

    if not city.show:
        raise Http404

    request.session['city_pk'] = city.pk
    logger.debug('Holla!!!')

    return HttpResponseRedirect(reverse('mainpage'))