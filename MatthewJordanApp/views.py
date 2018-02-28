# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Work

def index(request):
    works = Work.objects.order_by('created_date').reverse()
    return render(request, 'index.html', {"works":works})
