from django.contrib import messages
from django.shortcuts import render, redirect
from store.models import Product


def home(request):
    products = Product.objects.all()

    return render(request, 'home.html',{'products':products})



