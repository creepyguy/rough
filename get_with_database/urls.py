from django.urls import path

from . import views

urlpatterns = [
    path('api/', views.get_with_database, name='get_with_database'),
]
