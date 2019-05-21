from django.shortcuts import render, redirect

# Create your views here.
from .models import Portfolio
def portfolio(request):
    portfolios = Portfolio.objects 
    return render(request, 'portfolio.html', {'portfolios': portfolios})

def create2(request):
    photo = Portfolio()
    photo.title = request.POST['title']
    photo.image = request.FILES['image']
    photo.description = request.POST['description']
    photo.save()
    return redirect('/portfolio')

def upload(request):
    return render(request, 'upload.html')