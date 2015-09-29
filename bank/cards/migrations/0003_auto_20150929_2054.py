# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_auto_20150929_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardserial',
            name='number',
            field=models.CharField(max_length=2, serialize=False, primary_key=True),
        ),
    ]
