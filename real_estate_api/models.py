from django.contrib.gis.db import models
from core.models import CommonInfo
from django.db.models import JSONField


class Estate(CommonInfo):

    geom = models.PointField('Longitude, Latitude', blank=False, null=False)
    address = models.TextField('Address')
    area = models.IntegerField('Area', blank=False, null=False)
    rooms = models.IntegerField('Total rooms')
    garage = models.BooleanField('Garage', default=False)
    other = JSONField()

    class Meta:
        verbose_name = 'Estate'
        verbose_name_plural = 'Estates'
        ordering = ['-area']

        def __str__(self):
            return self.address
