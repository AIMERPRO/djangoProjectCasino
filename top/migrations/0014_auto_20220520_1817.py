# Generated by Django 3.1.1 on 2022-05-20 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('top', '0013_auto_20220520_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nametop',
            name='icon_to_top',
            field=models.BooleanField(blank=True, default=True, null=True, verbose_name='Иконка GO TO TOP'),
        ),
    ]