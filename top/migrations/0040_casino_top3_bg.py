# Generated by Django 3.1.1 on 2022-05-25 15:33

from django.db import migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('top', '0039_remove_casino_top3_bg'),
    ]

    operations = [
        migrations.AddField(
            model_name='casino',
            name='top3_bg',
            field=easy_thumbnails.fields.ThumbnailerImageField(default='upload/img/top3_bg/skycrown_bg.png', help_text='Фон для дизайна Top3', upload_to='upload/img/top3_bg/', verbose_name='Фон на карточке'),
        ),
    ]
