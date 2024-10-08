from django.urls import path
from .views import HomeViewPage, AboutViewPage, ContactViewPage

urlpatterns = [
    path('', HomeViewPage.as_view(), name='home'),
    path('about/', AboutViewPage.as_view(), name='about'),
    path('contact', ContactViewPage.as_view(), name='contact'),
]
