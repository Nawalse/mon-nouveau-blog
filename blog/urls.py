# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 15:20:48 2024

@author: figui
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]