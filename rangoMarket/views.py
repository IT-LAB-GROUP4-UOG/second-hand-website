from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'rangoMarket/home.html')


def post(request):
    return HttpResponse(request, "My Post")


def purchase(request):
    return HttpResponse(request, "My Purchase")


def post_new(request):
    return HttpResponse(request, "Post New item")

