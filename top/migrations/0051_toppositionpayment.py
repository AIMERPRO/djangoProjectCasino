# Generated by Django 3.1.1 on 2022-06-06 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('top', '0050_badge_color_hex'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopPositionPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField(blank=True, default=0, null=True, verbose_name='Position')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='Last change')),
                ('date_published', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('ccs', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tpp_ccs', to='top.countrycasinosetting')),
                ('payment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tpp_payment', to='top.payment')),
            ],
        ),
    ]
