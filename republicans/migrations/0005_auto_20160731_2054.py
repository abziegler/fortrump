# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-07-31 20:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('republicans', '0004_auto_20160731_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='republican',
            name='gov_type',
            field=models.CharField(choices=[(b'S', b'Senator'), (b'R', b'Representative'), (b'G', b'Governor')], default=b'R', max_length=1),
        ),
    ]
