# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Idol, Tvshow

admin.site.register(Idol)
admin.site.register(Tvshow)
