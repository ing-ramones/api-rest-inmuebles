from core.models import CommonInfo

from django.contrib.gis.db import models
from django.db.models import JSONField

from real_estate_api.managers import CompanyManager, EstateManager


class Company(CommonInfo):
    name = models.TextField('Name', max_length=255, unique=True)
    nif = models.IntegerField('Tax identification code', unique=True)

    objects = CompanyManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
        ordering = ['-name']

        def __str__(self):
            return self.name


class Estate(CommonInfo):

    geom = models.PointField('Longitude, Latitude', blank=False, null=False)
    address = models.TextField('Address', blank=True, null=True)
    area = models.IntegerField('Area', blank=False, null=False)
    rooms = models.IntegerField('Total rooms', blank=True, null=True)
    garage = models.BooleanField('Garage', default=False)
    other = JSONField(blank=True, null=True)
    company = models.ForeignKey(
        Company, related_name='estates', on_delete=models.CASCADE)

    objects = EstateManager()

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'Estate'
        verbose_name_plural = 'Estates'
        ordering = ['-id']

        def __str__(self):
            return self.address
