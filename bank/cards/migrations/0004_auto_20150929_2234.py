# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0003_auto_20150929_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='expiration_date',
            field=models.DateTimeField(editable=False),
        ),
        migrations.AlterField(
            model_name='card',
            name='last_used_date',
            field=models.DateTimeField(editable=False, blank=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='number',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='card',
            name='start_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
