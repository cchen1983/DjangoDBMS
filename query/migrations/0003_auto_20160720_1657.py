# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('query', '0002_auto_20160720_0507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenditure',
            name='payment',
            field=models.DecimalField(max_digits=19, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='membership',
            name='balance',
            field=models.DecimalField(max_digits=19, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(max_digits=19, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='purchasing',
            name='payment',
            field=models.DecimalField(max_digits=19, decimal_places=2),
        ),
    ]
