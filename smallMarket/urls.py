from django.urls import path
from . import views
urlpatterns = [
    path('sugarMarket/', views.getGoodByKind, name='index'),
    path('sugarMarket/detail/<str:nameofGood>/', views.detail, name='details'),
    path('sugarMarket/addToCart/<int:idofGood>/',
         views.addToCart, name='sendToShopcart'),
    path('sugarMarket/shopcart/', views.shopcart, name='shopCart'),
    path('sugarMarket/login/', views.login, name='login'),
    path('sugarMarket/shopcart/gotoCheckOut/',
         views.gotoCheckOut, name='gotoCheckOut'),
    path('sugarMarket/shopcart/gotoSuccess/',
         views.gotoSuccess, name='gotoSuccess'),
    path('sugarMarket/shopcart/checkOut/', views.checkOut, name='checkOut'),
    path('orders/Update/<int:idnum>/', views.orderUpdate),
    path('orders/<int:idnum>/', views.SearchOrderItem),
    path('sugarMarket/orders/', views.OrderMessage),
#     path('sugarMarket/admin/', views.admin),
#     path('sugarMarket/goodlist/', views.goodlist),
#     path('sugarMarket/goodadd/', views.goodAdd),
#     path('sugarMarket/good/update/', views.goodUpdateById),
#     path('sugarMarket/goodlist/delbyid/<int:id>', views.goodDelById),
#     path('sugarMarket/goodlist/preupdate/<int:id>', views.preGoodUpdateById),
#     path('sugarMarket/historyorder/', views.historyOrder),
#     path('sugarMarket/historyorder/orderlist/<int:order>', views.orderListByNum),
#     path('sugarMarket/logout/', views.logout),

]
