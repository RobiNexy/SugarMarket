from django.contrib import admin
from .models import Good,Order,OrderItem,Customer
# Register your models here.

admin.site.register(Good)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Customer)
