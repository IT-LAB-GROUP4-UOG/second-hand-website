from django.urls import path
from rangoMarket import views

app_name = 'rangoMarket'

urlpatterns = [
    path('', views.home, name='home'),
    path('my-post/', views.my_post, name='my_post'),
    path('purchase/', views.purchase, name='purchase'),
    path('post_item/', views.post_item, name='post_item'),
    path('about/', views.about, name='about'),
    path('item_detail/<int:item_id>', views.item_detail, name='item_detail'),
    path('home_old', views.home_old)


]
