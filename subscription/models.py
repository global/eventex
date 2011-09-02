# coding: utf-8

from django.db import models

class Subscription(models.Model):
    name = models.CharField('Name', max_length=100)
    cpf = models.CharField('CPF', max_length=11, unique=True)
    email = models.EmailField('E-Mail', unique=True)
    phone = models.CharField('Phone', max_length=20, blank=True)
    created_at = models.DateTimeField('Created at', auto_now_add=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['created_at']
        verbose_name = u'Subscription'
        verbose_name_plural =  u'Subscriptions'
