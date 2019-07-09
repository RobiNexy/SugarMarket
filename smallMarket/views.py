from django.shortcuts import render, redirect
from .models import Good, Customer, Order, OrderItem
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime
import random

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
    return render(request, 'shopcart.html', content)


def gotoCheckOut(request):
    orderItemIdList = []
    orderItemIdList = request.session.get('orderItemIdList', [])
    content = dict()
    goodNameList = []
    goodNumberList = []
    goodPriceList = []
    orderItemList = []
    for oiid in orderItemIdList:
        oi = OrderItem.objects.get(id=oiid)
        goodNameList.append(oi.good.goodName)
        goodNumberList.append(oi.goodNumber)
        goodPriceList.append(oi.good.goodSalePrice)

    content['goodNameList'] = goodNameList
    content['goodNumberList'] = goodNumberList
    content['goodPriceList'] = goodPriceList
    content['orderItemList'] = orderItemList
# 生成数据库
    return render(request, 'checkout.html', content)


def gotoSuccess(request):
    return render(request, 'paypage.html')


def checkOut(request):
    if request.POST:
        # 将房号格式化为4位
        customerRoomNumber = request.POST.get('customerRoomNumber', None)
        while len(customerRoomNumber) != 4:
            customerRoomNumber = '0' + customerRoomNumber
        customerName = request.POST.get('customerName', None)
        customerPhoneNumber = request.POST.get('customerPhoneNumber', None)
        # 生成订单号
        orderNumber = str(datetime.datetime.now().strftime(
            '%y%m%d%H%M%S')) + str(random.randint(10, 99)) + customerRoomNumber
        # 生成订单
        order = Order.objects.create(orderNumber=orderNumber)
        # 生成顾客
        customer = Customer.objects.create(customerName=customerName,
                                           customerPhoneNumber=customerPhoneNumber,
                                           customerRoomNumber=customerRoomNumber)
        Order.objects.filter(orderNumber=orderNumber).update(customer=customer)
        # 补完整订单项目表
        orderItemIdList = request.session.get('orderItemIdList', [])
        for oiid in orderItemIdList:
            OrderItem.objects.filter(id=oiid).update(
                order=order, customer=customer, isInCart=False)
        request.session.flush()

        return render(request, 'success.html')
    else:
        return render(request, 'checkout.html', {'msg': '订单确认失败'})


# 配送页
def SearchOrderItem(request, idnum):
    orderItemlist = OrderItem.objects.filter(order=idnum)
    return render(request, 'items.html', {'orderItemlist': orderItemlist, 'orderID': idnum})


def OrderMessage(request):
    orderlist = Order.objects.filter(orderCompleted=False)  # get all false
    return render(request, 'orders.html', {'orderlist': orderlist})


def orderUpdate(request, idnum):
    # 修改数据
    Order.objects.filter(orderNumber=idnum).update(orderCompleted=True)
    # 更新库存
    orderItemlist = OrderItem.objects.filter(order=idnum)
    for order in orderItemlist:
        val = Good.objects.get(id=order.good_id).goodNumberRemain
        vbl = order.goodNum
        temp = val-vbl
        Good.objects.filter(id=order.good_id).update(goodNumberRemain=temp)
    # 返回未配送订单页
    return redirect('/orders/')

# 管理员页面
def admin(request):
    return render(request, 'admin.html')

def goodAdd(request):
    if request.POST:
        # 接收页面提交的数据
         # goodnumber = request.POST.get('goodnumber',None)
        goodName = request.POST.get('goodName', None)
        goodKind = request.POST.get('goodKind', None)
        goodNumberRemain = request.POST.get('goodNumberRemain', None)
        goodInPrice = request.POST.get('goodInPrice', None)
        goodSalePrice = request.POST.get('goodSalePrice', None)
        goodPicPath = request.POST.get('goodPicPath', None)
        # 创建模型对象
        if((goodName == '') or (goodKind == '') or (goodNumberRemain == '') or (goodInPrice == '') or (goodSalePrice == '') or (goodPicPath == '')):
            return render(request, 'goodadd.html', {'msg': '添加失败，请输入完整的信息'})
        else:
            Good.objects.create(goodName=goodName, goodKind=goodKind, goodNumberRemain=goodNumberRemain,
                                    goodInPrice=goodInPrice,  goodSalePrice=goodSalePrice, goodPicPath=goodPicPath)
            return render(request, 'goodadd.html', {'msg': '添加成功'})
    else:
        return render(request, 'goodadd.html')


def goodlist(request):
    # 查询全部商品信息
    dlist = Good.objects.all()
    # 创建分页器
    paginator = Paginator(dlist, 20)  # 每页显示20条
    # 接受客户端发送的页码
    page = request.GET.get('page', 1)
    # 首页尾页
    try:
        dlist = paginator.page(page)
    except EmptyPage:
        dlist = paginator.page(1)
    except PageNotAnInteger:
        dlist = paginator.page(paginator.num_pages)
    # 将商品集合传递到页面上
    return render(request, 'goodlist.html', {'dlist': dlist})


def goodDelById(request, id):
    Good.objects.filter(id=id).delete()
    return redirect('/sugarMarket/goodlist/')


def preGoodUpdateById(request, id):
    # 根据id查询数据
    obj = Good.objects.filter(id=id)
    return render(request, 'goodupdate.html', {'good': obj[0]})


def goodUpdateById(request):
    # 获取页面传递的数据
    id = request.POST.get('id')
    goodName = request.POST.get('goodName', None)
    goodKind = request.POST.get('goodKind', None)
    goodNumberRemain = request.POST.get('goodNumberRemain', None)
    goodInPrice = request.POST.get('goodInPrice', None)
    goodSalePrice = request.POST.get('goodSalePrice', None)
    goodPicPath = request.POST.get('goodPicPath', None)
    goodTotalSale = request.POST.get('goodTotalSale', None)
    # 修改数据
    if((goodName == '') or (goodKind == '') or (goodNumberRemain == '') or (goodInPrice == '') or (goodSalePrice == '') or (goodPicPath == '')):
        # if((goodName == '') or (goodKind == '') or (goodNumberRemain == '') or (goodInPrice == '') or (goodSalePrice == '') or (goodPicPath == '') or (goodTotalSale== '')):
        # 查询全部商品信息
        dlist = Good.objects.all()
        # 创建分页器
        paginator = Paginator(dlist, 20)  # 每页显示20条
        # 接受客户端发送的页码
        page = request.GET.get('page', 1)
        # 首页尾页
        try:
            dlist = paginator.page(page)
        except EmptyPage:
            dlist = paginator.page(1)
        except PageNotAnInteger:
            dlist = paginator.page(paginator.num_pages)
        # 将商品集合传递到页面上
        return render(request, 'goodlist.html', {'dlist': dlist, 'msg': '修改失败'})
    else:
        Good.objects.filter(id=id).update(goodName=goodName, goodKind=goodKind, goodNumberRemain=goodNumberRemain,
                                          goodInPrice=goodInPrice, goodSalePrice=goodSalePrice, goodPicPath=goodPicPath)
        # Good.objects.filter(id = id).update(goodName=goodName, goodKind=goodKind, goodNumberRemain=goodNumberRemain, goodInPrice=goodInPrice, goodSalePrice=goodSalePrice, goodPicPath=goodPicPath, goodTotalSale=goodTotalSale)
        return redirect('/sugarMarket/goodlist/')


def historyOrder(request):
    # 查询全部订单号
    orderlist = Order.objects.all()
    # 创建分页器
    paginator = Paginator(orderlist, 20)  # 每页显示20条
    # 接受客户端发送的页码
    page = request.GET.get('page', 1)
   # 首页尾页
    try:
        orderlist = paginator.page(page)
    except EmptyPage:
        orderlist = paginator.page(1)
    except PageNotAnInteger:
        orderlist = paginator.page(paginator.num_pages)
    # 将商品集合传递到页面上
    return render(request, 'historyorder.html', {'orderlist': orderlist})


def orderListByNum(request, order):
    # 查询一个订单的信息
    itemlist = OrderItem.objects.all()
    return render(request, 'orderdetails.html', {'itemlist': itemlist})


def login(request):
    if request.POST:
        # 获取账号密码
        name = request.POST.get('username', None)
        pwd = request.POST.get('userpwd', None)
        if name == 'delivery' and pwd == '123456':
            # 将账号信息加密存入cookie
            response = redirect('/sugarmarket/orders/')
            return response
        elif name == 'admin' and pwd == '123456':
            # 将账号信息加密存入cookie
            response = redirect('/sugarMarket/admin/')
            return response
        else:
            # 账号密码错误 
            return render(request, 'login.html',{'msg':'账号或密码错误'})
    else:
        return render(request, 'login.html')

def logout(request):
    return redirect('/sugarMarket/login/')