# Generated by Django 3.1.1 on 2022-05-20 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('top', '0017_auto_20220520_1824'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nametop',
            name='badge',
        ),
        migrations.RemoveField(
            model_name='nametop',
            name='bg_img',
        ),
        migrations.RemoveField(
            model_name='nametop',
            name='bg_mob_img',
        ),
        migrations.RemoveField(
            model_name='nametop',
            name='bg_tab_img',
        ),
        migrations.RemoveField(
            model_name='nametop',
            name='logo',
        ),
    ]
