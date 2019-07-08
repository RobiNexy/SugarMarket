from django.urls import path
from . import views
urlpatterns = [
path('sugarMarket/', views.getGoodByKind, name='index'),
path('sugarMarket/detail/<str:nameofGood>/',views.detail,name='details'),
path('sugarMarket/setCookie/<int:idofGood>/',views.setCookie,name='sendToShopcart'),
path('sugarMarket/shopcart',views.shopcart,name='shopCart'),
]