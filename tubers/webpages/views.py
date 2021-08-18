from django.db import models
from django.shortcuts import render
from .models import TopSlider, Team

# Create your views here.
def home(request):
    sliders = TopSlider.objects.all()
    teamMembers = Team.objects.all()

    data = {
        'sliders' : sliders,
        'team' : teamMembers,
    }
    return render(request, 'webpages/home.html', data)

def contact(request):
    return render(request, 'webpages/contact.html')


def about(request):
    return render(request, 'webpages/about.html')


def services(request):
    return render(request, 'webpages/services.html')
