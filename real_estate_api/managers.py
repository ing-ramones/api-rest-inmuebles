
from time import strptime
import datetime

from django.db import models


class CompanyManager(models.Manager):

    def get_company_by_created(self, date):
        date = strptime(date, '%Y-%m-%d')
        queryset = self.get_queryset()
        return queryset.filter(created_at__year=date.tm_year,
                               created_at__month=date.tm_mon,
                               created_at__day=date.tm_mday).order_by('created_at')


class EstateManager(models.Manager):

    def get_estate_by_created(self, date):
        date = strptime(date, '%Y-%m-%d')
        queryset = self.get_queryset()
        return queryset.filter(created_at__year=date.tm_year,
                               created_at__month=date.tm_mon,
                               created_at__day=date.tm_mday).order_by('created_at')
