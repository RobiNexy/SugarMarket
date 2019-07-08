from django.urls import path
from . import views
urlpatterns = [
path('sugarMarket/', views.getGoodByKind, name='index'),
path('sugarMarket/detail/<str:nameofGood>/',views.detail,name='details'),
path('sugarMarket/setSession/<int:idofGood>/',views.setSession,name='sendToShopcart'),
path('sugarMarket/shopcart/',views.shopcart,name='shopCart'),
path('sugarMarket/login/',views.login,name='login'),
path('sugarMarket/shopcart/',views.shopcart,name='shopcart')
]