# Generated by Django 3.1.1 on 2022-06-22 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('top', '0056_remove_link_top'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='top',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='link_top', to='top.nametop'),
        ),
    ]
