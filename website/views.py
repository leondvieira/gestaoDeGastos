from django import template
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

register = template.Library()

@register.tag(name='static')
class HomePageView(TemplateView):
    template_name = 'home.html'