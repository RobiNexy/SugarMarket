from django.shortcuts import render,redirect
import sugarMarket.models

# Create your views here.

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

def sendName(request,name):
    return render(request,'detail.html',{'name':name})


def detail(request,nameofGood):
    good = Good.objects.get(goodName=nameofGood)
    picPath=good.goodPicPath
    content = dict()
    content['good']=good
    content['picPath']=picPath
    return render(request, 'detail.html',content)

def setCookie(request,idofGood):
    rep = redirect ('/sugarMarket/')
    rep.set_cookie('idofGood'+str(idofGood),idofGood)
    return rep

def shopcart(request):
    content=dict()
    vals=request.session.get('goods', None)
    for value in vals.values():
        content['id']=vals.idofGood
    return render(request, 'shopcart.html', {'content':content})