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
    offer_1 = models.CharField(max_length=50, verbose_name="Oferta A", blank=True, null=True)
    net_1 = models.DecimalField(max_digits=10, decimal_places=3, verbose_name="Neto A", blank=True, null=True)
    offer_2 = models.CharField(max_length=50, verbose_name="Oferta B", blank=True, null=True)
    net_2 = models.DecimalField(max_digits=10, decimal_places=3, verbose_name="Neto B", blank=True, null=True)
    offer_3 = models.CharField(max_length=50, verbose_name="Oferta C", blank=True, null=True)
    net_3 = models.DecimalField(max_digits=10, decimal_places=3, verbose_name="Neto C", blank=True, null=True)

    def __str__(self):
        return self.article_description
