# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-10-22 17:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zigzag_app', '0004_auto_20191022_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs_uploaded', to='zigzag_app.User'),
        ),
    ]
