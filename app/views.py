from django.shortcuts import render
from django.views.generic import TemplateView

class HomeViewPage(TemplateView):
    template_name = 'app/home.html'

class AboutViewPage(TemplateView):
        template_name = 'app/about.html'

class ContactViewPage(TemplateView):
    template_name = 'app/contact.html'
