from django.urls import path
from . import views

urlpatterns = [
    path('med-check/', views.home, name='home'),
    path('checker/', views.checker_view, name='checker'),
]