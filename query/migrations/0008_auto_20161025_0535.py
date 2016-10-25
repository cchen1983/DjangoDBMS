# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('query', '0007_auto_20161025_0521'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discount',
            name='discount',
        ),
        migrations.AddField(
            model_name='discount',
            name='dct',
            field=models.DecimalField(default=1.0, max_digits=19, decimal_places=2),
            preserve_default=False,
        ),
    ]
