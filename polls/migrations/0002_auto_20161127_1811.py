# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-27 18:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='article_size',
        ),
        migrations.AddField(
            model_name='item',
            name='article_PVP',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name=b'Precio Minimo'),
        ),
    ]
