# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-28 22:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('playgame', '0003_auto_20180326_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batterorder',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playgame.TeamMember'),
        ),
    ]