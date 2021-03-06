# Generated by Django 3.1.1 on 2022-04-23 08:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('top', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='link',
            options={'verbose_name': 'Ссылка', 'verbose_name_plural': 'Ссылки'},
        ),
        migrations.AlterModelOptions(
            name='mailtop',
            options={'verbose_name': 'Почта', 'verbose_name_plural': 'Почты'},
        ),
        migrations.AlterModelOptions(
            name='source',
            options={'verbose_name': 'Источник', 'verbose_name_plural': 'Источники'},
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.ManyToManyField(blank=True, default=None, related_name='profile_permission', to='top.Source')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
            },
        ),
    ]
