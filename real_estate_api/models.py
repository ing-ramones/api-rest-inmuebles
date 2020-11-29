from django.contrib.gis.db import models
from core.models import CommonInfo
from django.db.models import JSONField


class Company(CommonInfo):
    name = models.TextField('Name', max_length=255, unique=True)
    nif = models.IntegerField('Tax identification code', unique=True)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
        ordering = ['-name']

        def __str__(self):
            return self.address


class Estate(CommonInfo):

    geom = models.PointField('Longitude, Latitude', blank=False, null=False)
    address = models.TextField('Address')
    area = models.IntegerField('Area', blank=False, null=False)
    rooms = models.IntegerField('Total rooms')
    garage = models.BooleanField('Garage', default=False)
    other = JSONField()
    company = models.ForeignKey(
        Company, related_name='estates', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Estate'
        verbose_name_plural = 'Estates'
        ordering = ['-area']

        def __str__(self):
            return self.address
