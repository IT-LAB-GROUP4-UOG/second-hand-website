from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Item, ItemImage, User, Order
from .forms import ItemForm
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.http import JsonResponse


def home(request):
    items_list = Item.objects.all()
    paginator = Paginator(items_list, 8)
    page = request.GET.get('page')
    items = paginator.get_page(page)
    return render(request, 'rangoMarket/home.html', {'items': items})


def home_old(request):
    return render(request, 'rangoMarket/home-old.html')


def about(request):
    return render(request, 'rangoMarket/about.html')


@login_required
def my_post(request):
    items_list = Item.objects.filter(seller=request.user)
    paginator = Paginator(items_list, 8)
    page = request.GET.get('page')
    items = paginator.get_page(page)
    return render(request, 'rangoMarket/my_post.html', {'items': items})


@login_required
def my_sell(request):
    return


@login_required
def my_purchase(request):
    return HttpResponse(request, "My Purchase")


@login_required
def post_item(request):

    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.seller = request.user
            item.save()

            for image in request.FILES.getlist('images'):
                ItemImage.objects.create(item=item, image=image)

            return redirect(reverse('rangoMarket:item_detail', kwargs={'item_id': item.id}))
    else:
        form = ItemForm()
    return render(request, 'rangoMarket/post_item.html', {'form': form})


def item_detail(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    return render(request, 'rangoMarket/item_detail.html', {'item': item})


def order_detail(request, order_id):
    return render(request, 'rangoMarket/order_detail.html')


def buy_item(request, item_id):
    if request.method == 'POST':
        item = get_object_or_404(Item, id=item_id)
        if item.seller != request.user:
            order = Order.objects.create(buyer=request.user, seller=item.seller, item=item)
            return JsonResponse({'status': 'success', 'order_id': order.id})
        else:
            return JsonResponse({'status': 'error', 'message': "You can't buy your own item"})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request'})





