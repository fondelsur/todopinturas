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
    article_id = models.CharField(max_length=200, verbose_name="Código")
    article_description = models.CharField(max_length=200, verbose_name="Articulo")
    article_PVP = models.DecimalField(max_digits=10, default=0,  decimal_places=3, verbose_name="PVP")
    discount_l2 = models.DecimalField(max_digits=10, decimal_places=3, verbose_name="Descuento L2", blank=True, null=True)
    net_l2 = models.DecimalField(max_digits=10, decimal_places=3, verbose_name="Neto L2", blank=True, null=True)
    discount_l4 = models.DecimalField(max_digits=10, decimal_places=3, verbose_name="Descuento L4", blank=True, null=True)
    net_l4 = models.DecimalField(max_digits=10, decimal_places=3, verbose_name="Neto L4", blank=True, null=True)
    offer_303 = models.DecimalField(max_digits=10, decimal_places=3, verbose_name="Oferta 30+3", blank=True, null=True)
    offer_294 = models.DecimalField(max_digits=10, decimal_places=3, verbose_name="Oferta 29+4", blank=True, null=True)
    offer_285 = models.DecimalField(max_digits=10, decimal_places=3, verbose_name="Oferta 28+5", blank=True, null=True)

    def __str__(self):
        return self.article_description
