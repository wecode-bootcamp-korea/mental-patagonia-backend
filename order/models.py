from django.db import models

from member.models  import AddressBook
from member.models  import Member
from product.models import Product
from product.models import Size
from product.models import Color

class Order(models.Model):
    address_book    = models.ForeignKey('member.AddressBook', on_delete=models.SET_NULL, null=True)
    gift_message    = models.CharField(max_length=2000)
    shipping_method = models.ForeignKey('ShippingMethod', on_delete=models.SET_NULL, null=True)
    member          = models.ForeignKey('member.Member', on_delete=models.SET_NULL, null=True)
    order_status    = models.ForeignKey('OrderStatus', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'orders'

class OrderDetail(models.Model):
    product = models.ForeignKey('product.Product', on_delete=models.SET_NULL, null=True)
    color   = models.ForeignKey('product.Color', on_delete=models.SET_NULL, null=True)
    size    = models.ForeignKey('product.Size', on_delete=models.SET_NULL, null=True)
    order   = models.ForeignKey('Order', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'order_details'

class OrderStatus(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'order_status'

class ShippingMethod(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'shipping_methods'
