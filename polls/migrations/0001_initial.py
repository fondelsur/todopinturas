# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-22 19:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_id', models.CharField(max_length=200, verbose_name=b'Articulo')),
                ('article_description', models.CharField(max_length=200, verbose_name=b'Descripcion del Articulo')),
                ('article_size', models.CharField(max_length=50, verbose_name=b'Tama\xc3\xb1o')),
                ('article_line1', models.DecimalField(decimal_places=2, max_digits=10, verbose_name=b'Precio Minimo')),
                ('article_line2', models.DecimalField(decimal_places=2, max_digits=10, verbose_name=b'28+5')),
                ('article_line3', models.DecimalField(decimal_places=2, max_digits=10, verbose_name=b'30+3')),
                ('article_line4', models.DecimalField(decimal_places=2, max_digits=10, verbose_name=b'Linea 4')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('slug', models.CharField(default=b'question', max_length=10, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Question'),
        ),
    ]
