# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('query', '0005_expenditure_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('valid_from', models.DateTimeField(auto_now_add=True)),
                ('valid_to', models.DateTimeField(auto_now_add=True)),
                ('details', models.CharField(max_length=255)),
                ('target', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('activity_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='query.Activity')),
                ('discount', models.DecimalField(max_digits=19, decimal_places=2)),
            ],
            bases=('query.activity',),
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('activity_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='query.Activity')),
                ('n1', models.BigIntegerField(null=True)),
                ('productNo', models.ForeignKey(related_name='promotion', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='query.Product', null=True)),
            ],
            bases=('query.activity',),
        ),
    ]
