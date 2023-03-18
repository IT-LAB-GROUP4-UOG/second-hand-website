from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Item, User, Order
from .forms import ItemForm





from django.http import HttpResponse


def home(request):
    return render(request, 'rangoMarket/home.html')


@login_required
def post(request):
    return render(request, 'rangoMarket/post.html')


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


def item_detail(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    return render(request, 'rangoMarket/item_detail.html', {'item': item})



