# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-10-21 18:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zigzag_app', '0002_wish_granted_wish'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wish',
            old_name='granted_wish',
            new_name='is_granted',
        ),
        migrations.RemoveField(
            model_name='user',
            name='confirm_pw',
        ),
        migrations.AddField(
            model_name='wish',
            name='liked_by',
            field=models.ManyToManyField(related_name='liked_wishes', to='zigzag_app.User'),
        ),
    ]