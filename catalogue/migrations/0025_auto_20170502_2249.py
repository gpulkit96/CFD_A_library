# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-02 17:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0024_remove_post_callnum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(blank=True, editable=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='hidden_date',
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
    ]