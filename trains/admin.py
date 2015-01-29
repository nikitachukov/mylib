from django.contrib import admin

# Register your models here.
from trains.models import *

class StationsAdmin(admin.ModelAdmin):
    ordering = ('order',)
    fields = ['code', 'name','order']


admin.site.register(Stations, StationsAdmin)
