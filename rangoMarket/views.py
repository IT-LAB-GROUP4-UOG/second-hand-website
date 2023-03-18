from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Item, User, Order
from .forms import ItemForm




from django.http import HttpResponse


def home(request):
    return render(request, 'rangoMarket/home.html')


@login_required
def post(request):
    return HttpResponse(request, "My Post")


@login_required
def purchase(request):
    return HttpResponse(request, "My Purchase")


@login_required
def post_new(request):

    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.seller = request.user
            item.save()
            return redirect('item_detail', item_id=item.id)
    else:
        form = ItemForm()
    return render(request, 'rangoMarket/post_new.html', {'form': form})





