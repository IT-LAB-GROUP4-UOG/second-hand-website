from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'rangoMarket/home.html')


def signup(request):
    return render(request, 'signup.html')


def signin(request):
    return render(request, 'signin.html')


def myPost(request):
    return HttpResponse(request, "My Post")


def myPurchase(request):
    return HttpResponse(request, "My Purchase")


def mySell(request):
    return HttpResponse(request, "My Sell")

