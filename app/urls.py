from django.urls import path
from .views import HomeViewPage, AboutViewPage, ContactViewPage, PlantListView, PlantDetailView, PlantCreateView, PlantUpdateView, PlantDeleteView

urlpatterns = [
    path('', HomeViewPage.as_view(), name='home'),
    path('about/', AboutViewPage.as_view(), name='about'),
    path('contact', ContactViewPage.as_view(), name='contact'),
     path('plants/', PlantListView.as_view(), name='plant-list'),
      path('plants/<int:pk>/', PlantDetailView.as_view(), name='plant-detail'),
    path('plants/create/', PlantCreateView.as_view(), name='plant-create'),
    path('plants/<int:pk>/update/', PlantUpdateView.as_view(), name='plant-update'),
    path('plants/<int:pk>/delete/', PlantDeleteView.as_view(), name='plant-delete'),
]
