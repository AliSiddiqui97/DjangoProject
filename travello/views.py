from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination
from .models import News
from .models import Testimonial
def index(request):
    testimonial = Testimonial.objects.all()
    dest = Destination.objects.all() 
    news = News.objects.all() 
    return render(request,'index.html',{'dest':dest,'news':news,'testimonial':testimonial})

