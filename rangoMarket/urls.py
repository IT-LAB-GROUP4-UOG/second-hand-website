from django.urls import path
from rangoMarket import views

app_name = 'rangoMarket'

urlpatterns = [
    path('', views.home, name='home'),
    path('post/', views.post, name='post'),
    path('purchase/', views.purchase, name='purchase'),
    path('post_item/', views.post_item, name='post_item'),
    path('item_detail/<int:item_id>', views.item_detail, name='item_detail'),
    path('home_old', views.home_old)

]
