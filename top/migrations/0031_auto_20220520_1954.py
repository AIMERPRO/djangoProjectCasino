# Generated by Django 3.1.1 on 2022-05-20 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('top', '0030_auto_20220520_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nametop',
            name='bg_img',
            field=models.ImageField(null=True, upload_to='upload/img/custom/', verbose_name='Фоновое изображение (desktop 1280px)'),
        ),
    ]