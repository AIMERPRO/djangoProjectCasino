# Generated by Django 3.1.1 on 2022-05-20 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('top', '0008_auto_20220520_1258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nametop',
            name='theme',
        ),
    ]
