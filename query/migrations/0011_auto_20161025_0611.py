# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('query', '0010_auto_20161025_0544'),
    ]

    operations = [
        migrations.RenameField(
            model_name='discount',
            old_name='disc',
            new_name='discount',
        ),
    ]
