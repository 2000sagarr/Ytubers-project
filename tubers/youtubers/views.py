from django.shortcuts import get_object_or_404, render
from .models import Youtuber

# Create your views here.
def youtubers(request):
    youtubers = Youtuber.objects.order_by('-created_date')
    data ={
        'youtubers' : youtubers,
    }
    return render(request, 'youtubers/youtubers.html', data)

def youtubers_detail(request, id):
    youtuber = get_object_or_404(Youtuber, pk=id)
    data ={
        'youtuber' : youtuber
    }
    return render(request, 'youtubers/youtuber_detail.html', data)

def search(request):
    pass