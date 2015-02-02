from django.db import models

# Create your models here.

class Stations(models.Model):
    class Meta():
        db_table = 'trains_stations'
        verbose_name = 'Станция'
        verbose_name_plural = 'Станции'

    def __str__(self):
        return self.name

    code = models.CharField(max_length=100,primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    order = models.IntegerField()