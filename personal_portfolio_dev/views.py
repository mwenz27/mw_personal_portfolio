from django.shortcuts import render
from .models import project

# Create your views here.
def personalportfolio_dev(request):
    projects = project.objects
    return render(request, 'personal_portfolio_dev/home.html', {'projects': projects})

