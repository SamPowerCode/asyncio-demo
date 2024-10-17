from django.urls import path
from . import views

urlpatterns = [
    path('async/', views.async_view, name='async_view'),
]
