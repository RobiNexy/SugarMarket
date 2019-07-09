from django.db import models

# Create your models here.
# 货物表
class Good(models.Model):
    goodName=models.TextField(max_length=200)# 货物名称
    goodKind=models.TextField()# 货物种类
    goodNumberRemain=models.IntegerField(default=100)# 库存
    goodInPrice=models.FloatField()# 进价
    goodSalePrice=models.FloatField()# 售价
    goodPicPath=models.TextField(max_length=200,null=True,blank=True)# 图片地址（考虑用图床）
    goodTotalSale=models.IntegerField(default=0)#总销量
    def __str__(self):
        return self.goodName
    

# 收货人表
class Customer(models.Model):
    customerName=models.TextField(max_length=200,null=True,blank=True)#姓名
    customerPhoneNumber=models.TextField(max_length=200,null=True,blank=True)#手机号
    customerRoomNumber=models.TextField(max_length=200,null=True,blank=True)#房间号
    def __str__(self):
        return self.customerName
    

# 订单表
class Order(models.Model):
    orderNumber=models.TextField(max_length=200)# 订单号
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)#收货人ID
    orderCompleted=models.BooleanField(default=False)# 订单是否完成
    orderTotalPrice=models.FloatField(default=0)# 总价
    orderTime=models.DateTimeField(auto_now_add=True)# 生成时间
    

# 订单项目表
class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE,null=True,blank=True)# 订单ID
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True,blank=True)# 收货人ID
    good=models.ForeignKey(Good,on_delete=models.CASCADE,null=True,blank=True)# 商品ID
    goodNumber=models.IntegerField(default=1)# 单项商品数量
    goodTotalPrice=models.FloatField(default=0)# 单项总价   并不必要
    isInCart=models.BooleanField(default=True)



