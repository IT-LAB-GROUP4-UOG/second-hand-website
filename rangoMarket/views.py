from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Item, ItemImage, User, Order
from .forms import ItemForm
from django.http import HttpResponse
from django.core.paginator import Paginator


def home(request):
    items_list = Item.objects.all()
    paginator = Paginator(items_list, 8)
    page = request.GET.get('page')
    items = paginator.get_page(page)
    return render(request, 'rangoMarket/home.html', {'items': items})


def home_old(request):
    return render(request, 'rangoMarket/home-old.html')




@login_required
def post(request):
    return render(request, 'rangoMarket/post.html')


@login_required
def purchase(request):
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



