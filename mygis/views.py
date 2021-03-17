from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from mygis.models import Articles


def home(request):
    #return HttpResponse("Hello world")
    #return render(request, 'mygis/home.html')
    articles = Articles.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'mygis/home.html', context)
