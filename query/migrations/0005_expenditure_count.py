# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('query', '0004_auto_20160721_0458'),
    ]

    operations = [
        migrations.AddField(
            model_name='expenditure',
            name='count',
            field=models.BigIntegerField(null=True),
        ),
    ]
