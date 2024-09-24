from django.shortcuts import render
from django.http import HttpResponse
from .models import FruitsAndVeg

def home(request):
    Fruits_and_veg = FruitsAndVeg.objects.all()
    return render(request,'home.html',{'fruits_and_veg': Fruits_and_veg})

# Create your views here.
