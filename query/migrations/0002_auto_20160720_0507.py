# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('query', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasing',
            name='membershipNo',
            field=models.ForeignKey(related_name='pur_member', on_delete=django.db.models.deletion.SET_NULL, to='query.Membership', null=True),
        ),
        migrations.AlterField(
            model_name='purchasing',
            name='productNo',
            field=models.ForeignKey(related_name='pur_prod', on_delete=django.db.models.deletion.SET_NULL, to='query.Product', null=True),
        ),
    ]
