from colorfield.fields import ColorField
from django.db import models
from django.utils.text import slugify
from easy_thumbnails.fields import ThumbnailerImageField


class Domain(models.Model):
    name = models.CharField(max_length=50, blank=False, unique=True, verbose_name='Имя')
    group = models.ForeignKey('Group', related_name='domain_group', on_delete=models.CASCADE, verbose_name='Группа')
    certificate = models.OneToOneField('Certificate', related_name='domain_certificate', on_delete=models.CASCADE,
                                       verbose_name='Сертификат')

    search_console = models.BooleanField(default=False, verbose_name='Консоль')
    sitemap = models.BooleanField(default=False, verbose_name='Сайтмап')
    domain_type = models.CharField(max_length=100, blank=True, verbose_name='Вид домена')
    page_proofer = models.CharField(max_length=100, blank=True, verbose_name='Верстальщик')
    registrator = models.ForeignKey('Registrator', related_name='domain_registrator', on_delete=models.CASCADE,
                                    verbose_name='Регистратор')

    date_extended = models.DateTimeField(blank=True, verbose_name='Дата продления')
    server = models.ForeignKey('Server', related_name='domain_server', on_delete=models.CASCADE, verbose_name='Сервер')
    cloud_flare = models.ForeignKey('CloudFlare', related_name='domain_cloudflare', on_delete=models.CASCADE, verbose_name='CloudFlare')
    cloak = models.CharField(max_length=255, blank=False, verbose_name='Клоака')


class Group(models.Model):
    name = models.CharField(max_length=50, blank=False, unique=True, verbose_name='Имя')


class CloudFlare(models.Model):
    mail = models.ForeignKey('Mail', related_name='cloudflare_mail', on_delete=models.CASCADE, verbose_name='E-Mail')
    password = models.CharField(max_length=100, blank=True, verbose_name='Пароль')
    NS = models.CharField(max_length=100, blank=True, verbose_name='NS')


class Certificate(models.Model):
    name = models.CharField(max_length=50, blank=False, unique=True, verbose_name='Имя')


class Registrator(models.Model):
    site = models.CharField(max_length=255, blank=False, unique=True, verbose_name='Сайт')
    mail = models.CharField(max_length=255, blank=False, verbose_name='E-Mail')
    phone = models.CharField(max_length=255, blank=True, verbose_name='Телефон')
    password = models.CharField(max_length=100, blank=True, verbose_name='Пароль')


class Server(models.Model):
    registrator_site = models.CharField(max_length=100, blank=True, verbose_name='Сайт Регистратора')
    mail = models.ForeignKey('Mail', related_name='server_mail', on_delete=models.CASCADE, verbose_name='E-Mail')
    password = models.CharField(max_length=100, blank=True, verbose_name='Пароль')
    ip = models.CharField(max_length=100, blank=True, verbose_name='Ip адрес')
    ftp_password = models.CharField(max_length=100, blank=True, verbose_name='FTP Пароль')
    ftp_login = models.CharField(max_length=100, blank=True, verbose_name='FTP Логин')


class Mail(models.Model):
    site = models.CharField(max_length=255, blank=True, verbose_name='Сайт')
    mail = models.CharField(max_length=255, blank=False, verbose_name='E-Mail')
    phone = models.CharField(max_length=255, blank=True, verbose_name='Телефон')
    password = models.CharField(max_length=100, blank=True, verbose_name='Пароль')


class PC(models.Model):
    number = models.IntegerField(blank=False, verbose_name='Номер')
    anydesc = models.CharField(max_length=200, blank=True, verbose_name='Anydesc')
    country = models.CharField(max_length=100, blank=True, verbose_name='Страна')