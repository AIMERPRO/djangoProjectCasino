# Generated by Django 3.1.1 on 2022-05-20 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('top', '0021_auto_20220520_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nametop',
            name='badge',
            field=models.ImageField(blank=True, null=True, upload_to='upload/img/site_badges/', verbose_name='Значок (справа от лого)'),
        ),
        migrations.AlterField(
            model_name='nametop',
            name='bg_img',
            field=models.ImageField(null=True, upload_to='upload/img/custom/', verbose_name='Фоновое изображение (desktop 1280px)'),
        ),
        migrations.AlterField(
            model_name='nametop',
            name='bg_mob_img',
            field=models.ImageField(blank=True, null=True, upload_to='upload/img/custom/', verbose_name='Фоновое изображение (mobile 480px)'),
        ),
        migrations.AlterField(
            model_name='nametop',
            name='bg_tab_img',
            field=models.ImageField(blank=True, null=True, upload_to='upload/img/custom/', verbose_name='Фоновое изображение (tablet 992px)'),
        ),
        migrations.AlterField(
            model_name='nametop',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='upload/img/site_logos/', verbose_name='Логотип'),
        ),
    ]