from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.ProductModel)
admin.site.register(models.CartModel)
admin.site.register(models.OneClickOrderModel)
admin.site.register(models.OrderModel)
admin.site.register(models.OrderItemsModel)

# admin.site.register(models.ImagesModel)
