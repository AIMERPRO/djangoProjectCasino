# Generated by Django 3.1.1 on 2022-05-20 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('top', '0025_auto_20220520_1914'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nametop',
            name='badge',
        ),
        migrations.RemoveField(
            model_name='nametop',
            name='bg_color',
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
            name='button_color',
        ),
        migrations.RemoveField(
            model_name='nametop',
            name='color',
        ),
        migrations.RemoveField(
            model_name='nametop',
            name='h_color',
        ),
        migrations.RemoveField(
            model_name='nametop',
            name='icon_to_top',
        ),
        migrations.RemoveField(
            model_name='nametop',
            name='logo',
        ),
    ]
