# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-10-22 18:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zigzag_app', '0005_auto_20191022_1744'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='description',
            field=models.CharField(default=None, max_length=255),
        ),
    ]
