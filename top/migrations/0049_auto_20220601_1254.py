# Generated by Django 3.1.1 on 2022-06-01 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('top', '0048_auto_20220601_1139'),
    ]

    operations = [
        migrations.AddField(
            model_name='countrycasinosetting',
            name='pay_left',
            field=models.ForeignKey(blank=True, help_text='для нового топа и беттинга', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='payment_left', to='top.payment', verbose_name='выделить платежку слева'),
        ),
        migrations.AddField(
            model_name='countrycasinosetting',
            name='pay_right',
            field=models.ForeignKey(blank=True, help_text='для нового топа и беттинга', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='payment_right', to='top.payment', verbose_name='выделить платежку справа'),
        ),
        migrations.AlterField(
            model_name='nametop',
            name='design',
            field=models.CharField(choices=[('new', 'New'), ('old', 'Old'), ('betting', 'Betting'), ('top3', 'Top3'), ('top3-light', 'Top3-Light'), ('top4', 'Top4')], default='new', max_length=50, verbose_name='Design'),
        ),
    ]
