# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Question, Choice

from django.contrib import admin

admin.site.register(Question)
admin.site.register(Choice)
