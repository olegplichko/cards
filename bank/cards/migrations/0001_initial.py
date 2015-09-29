# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateTimeField(auto_created=True)),
                ('number', models.UUIDField()),
                ('expiration_date', models.DateTimeField()),
                ('last_used_date', models.DateTimeField(blank=True)),
                ('balance', models.IntegerField(default=0, blank=True)),
                ('status', models.CharField(default=b'IA', max_length=2, choices=[(b'IA', b'Inactive'), (b'AC', b'Active'), (b'EX', b'Expired')])),
            ],
        ),
        migrations.CreateModel(
            name='CardSerial',
            fields=[
                ('number', models.UUIDField(serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_created=True)),
                ('amount', models.IntegerField()),
                ('card', models.ForeignKey(to='cards.Card')),
            ],
        ),
        migrations.AddField(
            model_name='card',
            name='serial',
            field=models.ForeignKey(to='cards.CardSerial'),
        ),
    ]
