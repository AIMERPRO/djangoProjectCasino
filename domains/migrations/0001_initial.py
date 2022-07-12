# Generated by Django 3.1.1 on 2022-07-07 01:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='CloudFlare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(blank=True, max_length=100)),
                ('NS', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site', models.CharField(blank=True, max_length=255)),
                ('mail', models.CharField(max_length=255)),
                ('phone', models.CharField(blank=True, max_length=255)),
                ('password', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('anydesc', models.CharField(blank=True, max_length=200)),
                ('country', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Registrator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site', models.CharField(max_length=255, unique=True)),
                ('mail', models.CharField(max_length=255)),
                ('phone', models.CharField(blank=True, max_length=255)),
                ('password', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registrator_site', models.CharField(blank=True, max_length=100)),
                ('password', models.CharField(blank=True, max_length=100)),
                ('ip', models.CharField(blank=True, max_length=100)),
                ('ftp_password', models.CharField(blank=True, max_length=100)),
                ('ftp_login', models.CharField(blank=True, max_length=100)),
                ('mail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='server_mail', to='domains.mail')),
            ],
        ),
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Name')),
                ('search_console', models.BooleanField(default=False)),
                ('sitemap', models.BooleanField(default=False)),
                ('domain_type', models.CharField(blank=True, max_length=100)),
                ('page_proofer', models.CharField(blank=True, max_length=100)),
                ('date_extended', models.DateTimeField(blank=True)),
                ('cloak', models.CharField(max_length=255)),
                ('certificate', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='domain_certificate', to='domains.certificate')),
                ('cloud_flare', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='domain_cloudflare', to='domains.cloudflare')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='domain_group', to='domains.group')),
                ('registrator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='domain_registrator', to='domains.registrator')),
                ('server', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='domain_server', to='domains.server')),
            ],
        ),
        migrations.AddField(
            model_name='cloudflare',
            name='mail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cloudflare_mail', to='domains.mail'),
        ),
    ]