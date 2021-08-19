from django.db import models
from django.shortcuts import render
from .models import TopSlider, Team
from youtubers.models import Youtuber

# Create your views here.
def home(request):
    sliders = TopSlider.objects.all()
    teamMembers = Team.objects.all()
    featured_youtubers = Youtuber.objects.order_by('-created_date').filter(is_featured = True)
    youtubers = Youtuber.objects.order_by('-subs_count')
    data = {
        'sliders' : sliders,
        'team' : teamMembers,
        'featured_youtubers' : featured_youtubers,
        'youtubers' : youtubers[:6],
    }
    return render(request, 'webpages/home.html', data)

def contact(request):
    return render(request, 'webpages/contact.html')


def about(request):
    return render(request, 'webpages/about.html')


def services(request):
    return render(request, 'webpages/services.html')
