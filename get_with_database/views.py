from django.shortcuts import render

from .models import TheDatabase

def get_with_database(request):
    return render(request, 'get_with_database/get_with_database.html')
