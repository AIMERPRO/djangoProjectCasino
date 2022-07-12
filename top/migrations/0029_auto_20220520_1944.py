# Generated by Django 3.1.1 on 2022-05-20 19:44

from django.db import migrations, models
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('top', '0028_remove_nametop_bg_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='nametop',
            name='badge',
            field=easy_thumbnails.fields.ThumbnailerImageField(blank=True, null=True, upload_to='upload/img/site_badges/', verbose_name='Значок (справа от лого)'),
        ),
        migrations.AddField(
            model_name='nametop',
            name='bg_img',
            field=easy_thumbnails.fields.ThumbnailerImageField(null=True, upload_to='upload/img/custom/', verbose_name='Фоновое изображение (desktop 1280px)'),
        ),
        migrations.AddField(
            model_name='nametop',
            name='bg_mob_img',
            field=easy_thumbnails.fields.ThumbnailerImageField(blank=True, null=True, upload_to='upload/img/custom/', verbose_name='Фоновое изображение (mobile 480px)'),
        ),
        migrations.AddField(
            model_name='nametop',
            name='bg_tab_img',
            field=easy_thumbnails.fields.ThumbnailerImageField(blank=True, null=True, upload_to='upload/img/custom/', verbose_name='Фоновое изображение (tablet 992px)'),
        ),
        migrations.AddField(
            model_name='nametop',
            name='icon_to_top',
            field=models.BooleanField(blank=True, default=False, verbose_name='Иконка GO TO TOP'),
        ),
        migrations.AddField(
            model_name='nametop',
            name='logo',
            field=easy_thumbnails.fields.ThumbnailerImageField(blank=True, null=True, upload_to='upload/img/site_logos/', verbose_name='Логотип'),
        ),
    ]