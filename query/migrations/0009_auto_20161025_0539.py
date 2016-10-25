# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('query', '0008_auto_20161025_0535'),
    ]

    operations = [
        migrations.RenameField(
            model_name='discount',
            old_name='dct',
            new_name='discount',
        ),
    ]
