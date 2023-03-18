from django.urls import path
from rangoMarket import views

app_name = 'rangoMarket'

urlpatterns = [
    path('', views.home, name='home'),
    path('post/', views.myPost, name='post'),
    path('purchase/', views.myPurchase, name='purchase'),

]
