# Generated by Django 3.1.1 on 2022-05-28 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('top', '0041_auto_20220525_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='nametop',
            name='tr_bottom_2',
            field=models.TextField(blank=True, help_text='для беттинга', null=True, verbose_name='Текст ВНИЗУ СТРАНИЦЫ'),
        ),
    ]
