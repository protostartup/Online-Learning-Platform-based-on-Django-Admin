# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-06-27 14:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0005_courseorg_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseorg',
            name='tags',
        ),
    ]
