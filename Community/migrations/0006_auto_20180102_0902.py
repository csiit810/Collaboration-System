# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-02 09:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Community', '0005_auto_20180102_0842'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SuggestCommunity',
            new_name='RequestCommunityCreation',
        ),
    ]
