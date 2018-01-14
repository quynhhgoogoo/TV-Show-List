# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class JustinBieber(models.Model):
    date_of_birth = models.CharField(max_length=200)
    alternative_name = models.CharField(max_length=200)
    sibblings_name = models.CharField(max_length=200)
    mother_name = models.CharField(max_length=200)
	
    def __str__(self):
        return self.alternative_name

class EmmaWatson(models.Model):
    date_of_birth = models.CharField(max_length=200)
    nationality = models.IntegerField(default=0)

    def __str__(self):
		return self.date_of_birth


