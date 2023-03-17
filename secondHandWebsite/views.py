from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'index.html')


def signup(request):
    return render(request, 'signup.html')


def signin(request):
    return render(request, 'signin.html')


def myPost(request):
    return HttpResponse("My Post")


def myPurchase(request):
    return HttpResponse("My Purchase")


def mySell(request):
    return HttpResponse("My Sell")


# git test


