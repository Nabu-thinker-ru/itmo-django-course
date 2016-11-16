from django.contrib import admin

from city.models import Country, City

admin.site.register(Country)


class CityAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'show', 'order')
    list_filter = ('show',)
    search_fields = ('name',)

admin.site.register(City, CityAdmin)