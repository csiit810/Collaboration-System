# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-22 14:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Group', '0002_auto_20171122_1432'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Community', '0002_auto_20171120_1202'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommunityGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='communitygroups', to='Community.Community')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='communitygroups', to='Group.Group')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='communitygroups', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
