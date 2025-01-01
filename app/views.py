from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Plant

class HomeViewPage(TemplateView):
    template_name = 'app/home.html'

class AboutViewPage(TemplateView):
        template_name = 'app/about.html'

class ContactViewPage(TemplateView):
    template_name = 'app/contact.html'

class PlantListView(ListView):
    model = Plant
    template_name = 'app/plant_list.html'
    context_object_name = 'plants'

class PlantDetailView(DetailView):
    model = Plant
    template_name = 'app/plant_detail.html'
    context_object_name = 'plant'

class PlantCreateView(CreateView):
    model = Plant
    template_name = 'app/plant_form.html'
    fields = ['Name', 'Description', 'Sunlight', 'Soil_type', 'Water_requirements']

class PlantUpdateView(UpdateView):
    model = Plant
    template_name = 'app/plant_form.html'
    fields = ['Name', 'Description', 'Sunlight', 'Soil_type', 'Water_requirements']

class PlantDeleteView(DeleteView):
    model = Plant
    template_name = 'app/plant_confirm_delete.html'
    success_url = reverse_lazy('plant-list')
