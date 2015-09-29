# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardserial',
            name='number',
            field=models.IntegerField(max_length=2, serialize=False, primary_key=True),
        ),
    ]
