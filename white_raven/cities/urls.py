from django.contrib import admin
from .views import *
from django.urls import path,include

urlpatterns = [
    path('', CitiesListView.as_view(), name='home'),
    path('create/', CitiesCreateView.as_view(), name='create'),
    path('see/<int:pk>/', CitiesDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', CitesUpdateView.as_view(), name='detail'),
    path('delete/<int:pk>/', CitesDeleteView.as_view(), name='delete'),


]