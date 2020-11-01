from decimal import Decimal
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.timezone import now


# Create your models here.
class ProductModel(models.Model):
    # types = (
    #     ('Спортивный костюм', 'Спортивный костюм')
    # )
    # type_product = models.CharField(max_length=14, choices=types)
    product_model = models.CharField(max_length=3)
    price = models.PositiveSmallIntegerField(default=600)
    colors = (
        ('Бежевый', 'Бежевый'),
        ('Темно-бежевый', 'Темно-бежевый'),
        ('Кэмел', 'Кэмел'),
        ('Фисташковый', 'Фисташковый'),
        ('Мята', 'Мята'),
        ('Розовый', 'Розовый'),
        ('Коррал', 'Коррал'),
        ('Черный', 'Черный')
    )
    color = models.CharField(max_length=13, choices=colors)
    size = models.CharField(max_length=40, default='XXS, XS, S, M, L, XL')
    fabric_structure = models.CharField(max_length=40, blank=True, default='80% cotton, 20% poly',
                                        verbose_name='Состав ткани')
    description = models.TextField()
    sale = models.PositiveSmallIntegerField(default=None, null=True, validators=[MaxValueValidator(600)],
                                            blank=True, verbose_name='Цена со скидкой')
    picture = models.ImageField(upload_to='products', verbose_name='Главная картинка')
    picture2 = models.ImageField(upload_to='products', blank=True, null=True)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = 'Товары'

    def __str__(self):
        return '{} {}'.format(self.product_model, self.color)


# class ImagesModel(models.Model):
#     product = models.ForeignKey(ProductModel, related_name='photos', on_delete=models.CASCADE)
#     picture = models.ImageField(upload_to='products')
#
#     class Meta:
#         verbose_name = "Картинка товара"
#         verbose_name_plural = 'Картинки товаров'
#
#     def __str__(self):
#         return '{} {}'.format(self.product, self.pk)


class CartModel(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, related_name='cart', on_delete=models.CASCADE)
    session_key = models.CharField(max_length=40)
    product_id = models.PositiveIntegerField()
    size = models.CharField(max_length=3, default='XXX')

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = 'Корзина'

    # def __str__(self):
    #     customer = self.user
    #     if customer is None:
    #         customer = 'Аноним'
    #     return '{}, {}'.format(customer, )


class OneClickOrderModel(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    phone = models.PositiveSmallIntegerField()
    date = models.DateTimeField(default=now)

    class Meta:
        verbose_name = "OneClick Заказ"
        verbose_name_plural = 'OneClick Заказы'

    def __str__(self):
        return '{}, дата заявки: {} '.format(self.product, self.date)


class OrderModel(models.Model):
    customer = models.CharField(max_length=50)
    phone = models.PositiveIntegerField()
    email = models.EmailField(default=None, null=True, blank=True)
    shipping_by = models.CharField(max_length=11)
    address = models.CharField(max_length=100)
    details = models.CharField(max_length=200, null=True, blank=True)
    price = models.PositiveIntegerField()
    date = models.DateTimeField(default=now)

    def __str__(self):
        return '{}, {}, {}, {}'.format(self.customer, self.shipping_by, self.address, self.date)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = 'Заказы'


class OrderItemsModel(models.Model):
    order = models.ForeignKey(OrderModel, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return '{}, {} шт. - {}'.format(self.product, self.quantity, self.price)

    class Meta:
        verbose_name = "Заказанный товар"
        verbose_name_plural = 'Заказанные товары'
