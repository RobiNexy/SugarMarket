from django.shortcuts import render, redirect
from .models import Good, Customer, Order, OrderItem

# Create your views here.
orderItemIdList = []


def gotoHead(request):
    return render(request, 'head.html')


def getGoodByKind(request):
    waterList = Good.objects.filter(goodKind="水饮")
    milkList = Good.objects.filter(goodKind="奶类")
    wineList = Good.objects.filter(goodKind="酒类")
    snackList = Good.objects.filter(goodKind="速食")
    cakeList = Good.objects.filter(goodKind="饼干蛋糕")
    foodList = Good.objects.filter(goodKind="膨化食品")
    hardList = Good.objects.filter(goodKind="干果坚果")
    selfList = Good.objects.filter(goodKind="日用")
    product = dict()
    product["waterList"] = waterList
    product['milkList'] = milkList
    product['wineList'] = wineList
    product['snackList'] = snackList
    product['cakeList'] = cakeList
    product['foodList'] = foodList
    product['hardList'] = hardList
    product['selfList'] = selfList
    return render(request, 'index.html', product)


def sendName(request, name):
    return render(request, 'detail.html', {'name': name})


def detail(request, nameofGood):
    good = Good.objects.get(goodName=nameofGood)
    picPath = good.goodPicPath
    content = dict()
    content['good'] = good
    content['picPath'] = picPath
    return render(request, 'detail.html', content)


def addToCart(request, idofGood):
    rep = redirect('/sugarMarket/')
    good = Good.objects.get(id=idofGood)
    # 生成orderItem
    orderItem = OrderItem.objects.create(good=good)
    # 将生成的orderitem的id放到session传给购物车
    orderItemIdList.append(orderItem.id)
    request.session['orderItemIdList'] = orderItemIdList
    return rep


def shopcart(request):
    orderItemIdList = request.session.get('orderItemIdList', [])
    glist = []
    content = dict()
    for oiid in orderItemIdList:
        glist.append(OrderItem.objects.get(id=oiid).good)
    content['good'] = glist
    # request.session['orderItemIdList'] = orderItemIdList
    return render(request, 'shopcart.html', content)


def login(request):
    return render(request, 'login.html')


def gotoCheckOut(request):
    orderItemIdList = []
    orderItemIdList = request.session.get('orderItemIdList', None)
    content = dict()
    goodNameList = []
    goodNumberList = []
    goodTotalPriceList = []

    for oiid in orderItemIdList:
        oi = OrderItem.objects.get(id=oiid)
        goodNameList.append(oi.good.goodName)
        goodNumberList.append(oi.goodNumber)
        orderItemTotalPriceList.append(oi.goodTotalPrice)

    content['goodNameList'] = goodNameList
    content['goodNumberList'] = goodNumberList
    content['orderItemTotalPriceList'] = orderItemTotalPriceList#单项总价list
    request.session['goodLists'] = content
    return render(request, 'checkout.html', content)


# 房间号码作为订单号的一部分，因此需要确定长度为4
def setRoomNumerLength(request):
    customerRoomNumber = request.POST.get('customerRoomNumber', None)
    while len(customerRoomNumber) != 4:
        customerRoomNumber = '0' + customerRoomNumber
    return str(customerRoomNumber)

# 填写并返回Customer表


def setCustomerDetail(request):
    if request.POST:
        customerName = request.POST.get('customerName', None)
        customerPhoneNumber = request.POST.get('customerPhoneNumber', None)
        customerRoomNumber = setRoomNumerLength(request)
        # 向客户表中写入数据
        return Customer.objects.create(customerName=customerName,
                                       customerPhoneNumber=customerPhoneNumber,
                                       customerRoomNumber=customerRoomNumber)
    else:
        return render(request, 'checkout.html', {'msg': '请填写个人信息'})

# 填写并返回Order表


def setOrderDetail(request):
    if request.POST:
        # 订单表写入数据
        orderNumber = str(datetime.datetime.now().strftime(
            '%y%m%d%H%M%S')) + str(random.randint(10, 99)) + setRoomNumerLength(request)
        orderCompleted = False
        goodDict = dict()
        goodDict = request.session.get('goodList')
        orderItemTotalPriceList = goodDict['orderItemTotalPriceList']#单项总价表
        customer = setCustomerDetail(request)
        orderTotalPrice = 0.0#订单总价
        for total in orderItemTotalPriceList:
            orderTotalPrice = total+orderTotalPrice
        order = Order(orderNumber=orderNumber, customer=customer,
                      orderTotalPrice=int(orderTotalPrice), orderCompleted=orderCompleted)
        order.save()
        return order
    else:
        return render(request, 'checkout.html', {'msg': '订单确认失败'})


def setOrderItemDetail(request):
    # 订单详情表写入数据
	goodDict = dict()
    goodDict = request.session.get('goodList')
	

	goodNumberList = goodDict['goodNumberList']
    orderItemTotalPriceList = goodDict['orderItemTotalPriceList']
	goodNameList=goodDict('goodNameList')

    # 引用函数获取order（其中已写入了customer）
    order = setOrderDetail(request)

    # 根据传来的goodName获得good类
    goodName = request.session.get('goodName', None)
    good = Good.objects.get(goodName=goodName)

    orderItem = OrderItem(order=order, customer=order.customer,
                          good=good, goodNumber=goodNumber, goodTotalPrice=goodTotalPrice)
    orderItem.save()
    return orderItem
