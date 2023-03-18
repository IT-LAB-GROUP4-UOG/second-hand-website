from django.urls import path
from rangoMarket import views

app_name = 'rangoMarket'

urlpatterns = [
    path('', views.home, name='home'),
    path('post/', views.post, name='post'),
    path('purchase/', views.purchase, name='purchase'),
    path('post_new/', views.post_new, name='post_new'),
    path('item_detal/<int:item_id>', views.item_detail, name='item_detail'),


]
