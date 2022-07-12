# Generated by Django 3.1.1 on 2022-05-23 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('top', '0033_nametop_button_text_color'),
    ]

    operations = [
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
    ]