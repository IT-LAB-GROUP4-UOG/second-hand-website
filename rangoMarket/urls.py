from django.urls import path
from rangoMarket import views

app_name = 'rangoMarket'

urlpatterns = [
    path('', views.home, name='home'),
    path('post/', views.post, name='post'),
    path('purchase/', views.purchase, name='purchase'),
    path('postnew/', views.post_new, name='post_new')


]
