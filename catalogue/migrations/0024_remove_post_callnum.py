# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-02 11:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0023_auto_20170316_1155'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='CallNum',
        ),
    ]