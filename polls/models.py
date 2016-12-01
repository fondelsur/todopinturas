# -*- coding: utf-8 -*-
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    slug = models.CharField(max_length=10, unique=True,
                            default="question")

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Item(models.Model):
    article_id = models.CharField(max_length=200, verbose_name="Articulo")
    article_description = models.CharField(max_length=200, verbose_name="Descripcion del Articulo")
    article_PVP = models.DecimalField(max_digits=10, default=0,  decimal_places=2, verbose_name="Precio Minimo")
    article_line1 = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio Minimo")
    article_line2 = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="28+5")
    article_line3 = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="30+3")
    article_line4 = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Linea 4")

    def __str__(self):
        return self.article_description
