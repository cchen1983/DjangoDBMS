# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('phone', models.CharField(max_length=32)),
                ('address', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=16, choices=[(b'Male', b'Male'), (b'Female', b'Female'), (b'LGBT', b'LGBT')])),
                ('birthday', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Expenditure',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dtime', models.DateTimeField(auto_now_add=True)),
                ('payment', models.DecimalField(max_digits=19, decimal_places=4)),
                ('details', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('regDate', models.DateField(auto_now_add=True)),
                ('balance', models.DecimalField(max_digits=19, decimal_places=4)),
                ('passphrase', models.CharField(max_length=32)),
                ('customerNo', models.ForeignKey(related_name='membership', on_delete=django.db.models.deletion.SET_NULL, to='query.Customer', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('count', models.BigIntegerField(null=True)),
                ('price', models.DecimalField(max_digits=19, decimal_places=4)),
                ('details', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Purchasing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('count', models.BigIntegerField(null=True)),
                ('payment', models.DecimalField(max_digits=19, decimal_places=4)),
                ('dtime', models.DateTimeField(auto_now_add=True)),
                ('membershipNo', models.ForeignKey(related_name='purchasing', on_delete=django.db.models.deletion.SET_NULL, to='query.Membership', null=True)),
                ('productNo', models.ForeignKey(related_name='purchasing', on_delete=django.db.models.deletion.SET_NULL, to='query.Product', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='expenditure',
            name='productNo',
            field=models.ForeignKey(related_name='buyingIn', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='query.Product', null=True),
        ),
        migrations.AlterUniqueTogether(
            name='customer',
            unique_together=set([('name', 'phone')]),
        ),
    ]
