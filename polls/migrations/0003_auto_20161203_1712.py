# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-03 17:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20161127_1811'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='article_line1',
        ),
        migrations.RemoveField(
            model_name='item',
            name='article_line2',
        ),
        migrations.RemoveField(
            model_name='item',
            name='article_line3',
        ),
        migrations.RemoveField(
            model_name='item',
            name='article_line4',
        ),
        migrations.AddField(
            model_name='item',
            name='discount_l2',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True, verbose_name=b'Descuento L2'),
        ),
        migrations.AddField(
            model_name='item',
            name='discount_l4',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True, verbose_name=b'Descuento L4'),
        ),
        migrations.AddField(
            model_name='item',
            name='net_1',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True, verbose_name=b'Neto A'),
        ),
        migrations.AddField(
            model_name='item',
            name='net_2',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True, verbose_name=b'Neto B'),
        ),
        migrations.AddField(
            model_name='item',
            name='net_3',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True, verbose_name=b'Neto C'),
        ),
        migrations.AddField(
            model_name='item',
            name='net_l2',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True, verbose_name=b'Neto L2'),
        ),
        migrations.AddField(
            model_name='item',
            name='net_l4',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True, verbose_name=b'Neto L4'),
        ),
        migrations.AddField(
            model_name='item',
            name='offer_1',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name=b'Oferta A'),
        ),
        migrations.AddField(
            model_name='item',
            name='offer_2',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name=b'Oferta B'),
        ),
        migrations.AddField(
            model_name='item',
            name='offer_3',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name=b'Oferta C'),
        ),
        migrations.AlterField(
            model_name='item',
            name='article_PVP',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=10, verbose_name=b'PVP'),
        ),
        migrations.AlterField(
            model_name='item',
            name='article_description',
            field=models.CharField(max_length=200, verbose_name=b'Articulo'),
        ),
        migrations.AlterField(
            model_name='item',
            name='article_id',
            field=models.CharField(max_length=200, verbose_name=b'C\xc3\xb3digo'),
        ),
    ]
