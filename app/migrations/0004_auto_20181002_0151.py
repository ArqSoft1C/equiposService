# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-02 01:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20180922_0507'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='captain_id',
        ),
        migrations.RemoveField(
            model_name='team',
            name='squad',
        ),
        migrations.DeleteModel(
            name='Team',
        ),
    ]
