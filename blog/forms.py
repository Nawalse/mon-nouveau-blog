# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 08:50:15 2024

@author: figui
"""

from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)