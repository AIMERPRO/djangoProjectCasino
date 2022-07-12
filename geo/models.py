# -*- coding: utf-8 -*-
from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField

from decor.models import Theme

CURRENCY = (
    (None, None),
    ('€', '€'),
    ('$', '$'),
)

class Currency(models.Model):
    name = models.CharField(u'name', max_length=50, unique=True)
    acronym = models.CharField(u'acronym', max_length=5, null=True, default=None)
    symbol = models.CharField(u'symbol', max_length=5, blank=True, null=True, default=None)
    logo = ThumbnailerImageField(u'logo', upload_to="upload/img/currency/", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"Currency"
        verbose_name_plural = u"Currencies"

class Country(models.Model):
    name = models.CharField(u'Название', max_length=50, unique=True)
    slug = models.CharField(u'Обозначение (en)',max_length=255, unique=True)
    image = ThumbnailerImageField(u'Flag', upload_to="upload/img/flags/", blank=False)
    currency = models.ForeignKey(Currency, related_name='country_currency', blank=True, null=True, default=None, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"Country"
        verbose_name_plural = u"Countries"