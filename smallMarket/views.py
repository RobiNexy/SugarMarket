from django.shortcuts import render,redirect
from .models import Good,Customer,Order,OrderItem

# Create your views here.
idofGoodList=list()
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

def setSession(request,idofGood):
    rep = redirect ('/sugarMarket/')
    # idofGoodList=list()
    idofGoodList.append(idofGood)
    request.session['idofGoodList']=idofGoodList
    # rep.set_cookie('idofGoodList',idofGoodList)
    return rep
# def addToCart(request,idofGood):

def shopcart(request):
    idofGoodList=request.session.get('idofGoodList')
    idod=idofGoodList
    # looo=[1,1,2,5,6]
    glist=[]
    content=dict()
    for index in range(len(idod)):
        glist.append(Good.objects.get(id=idod[index]))
    content['good']=glist
    return render(request, 'shopcart.html', content)


def login(request):
        return render(request, 'login.html')