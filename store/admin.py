from django.contrib import admin

from . import models

admin.site.register(models.ProductModel)
admin.site.register(models.CartModel)
admin.site.register(models.OneClickOrderModel)
admin.site.register(models.OrderModel)
admin.site.register(models.OrderItemsModel)
