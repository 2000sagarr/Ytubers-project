from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from .models import Youtuber

# Create your views here.
def youtubers(request):
    youtubers = Youtuber.objects.order_by('-created_date')
    city_search = Youtuber.objects.values_list('city', flat=True).distinct()
    camera_search = Youtuber.objects.values_list('camera_type' , flat=True).distinct()
    category_search = Youtuber.objects.values_list('category' , flat=True).distinct()

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            youtubers = youtubers.filter(city__iexact = city)

    if 'camera_type' in request.GET:
        camera_type = request.GET['camera_type']
        if camera_type:
            youtubers = youtubers.filter(camera_type__iexact = city)

    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            youtubers = youtubers.filter(category__iexact = category)

    data ={
        'youtubers' : youtubers,
        'city_search' : city_search,
        'camera_search' : camera_search,
        'category_search' : category_search,
    }
    return render(request, 'youtubers/youtubers.html', data)

@login_required(login_url="login")
def youtubers_detail(request, id):
    youtuber = get_object_or_404(Youtuber, pk=id)
    data ={
        'youtuber' : youtuber
    }
    return render(request, 'youtubers/youtuber_detail.html', data)

def search(request):
    youtubers = Youtuber.objects.order_by('-created_date')
    # it will give the array of cities
    city_search = Youtuber.objects.values_list('city', flat=True).distinct()
    camera_search = Youtuber.objects.values_list('camera_type', flat=True).distinct()
    category_search = Youtuber.objects.values_list('category', flat=True).distinct()

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            youtubers = youtubers.filter(description__icontains = keyword)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            youtubers = youtubers.filter(city__iexact = city)

    if 'camera_type' in request.GET:
        camera_type = request.GET['camera_type']
        if camera_type:
            youtubers = youtubers.filter(camera_type__iexact = camera_type)
    
    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            youtubers = youtubers.filter(category__iexact = category)

    data = {
        'youtubers' : youtubers,
        'city_search' : city_search,
        'camera_search' : camera_search,
        'category_search' : category_search
    }
    return render(request, 'youtubers/search.html',data)
