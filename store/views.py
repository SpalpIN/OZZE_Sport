from smtplib import SMTPException

from django.core.mail import send_mail
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import TemplateView

from .models import CartModel, OneClickOrderModel, OrderItemsModel, OrderModel, ProductModel


def start(request):
    # request.session.save()
    # request.session.clear_expired()
    # request.session.set_expiry(None)
    if not request.session.session_key:
        request.session.save()
    context = {}
    return render(request, 'index.html', context)


class WriteUs(TemplateView):
    def post(self, request):
        user_msg = request.POST['user_msg']
        if user_msg:
            try:
                send_mail('Message from store page', user_msg, 'heyhowareu1221@gmail.com',
                          ['heyhowareu1221@gmail.com'], fail_silently=False)
            except SMTPException:
                pass
        return redirect('/')


def size_chart(request):
    context = {}
    return render(request, 'size_chart.html', context)


def return_and_change(request):
    context = {}
    return render(request, 'return_change.html', context)


def delivery_payment(request):
    context = {}
    return render(request, 'delivery_payment.html', context)


def wholesale_customers(request):
    context = {}
    return render(request, 'wholesale_customers.html', context)


def catalog(request, products=0):
    if products == 0:
        products = ProductModel.objects.all()
        catalog_filter = False
    else:
        products = CatalogFilter.products
        catalog_filter = True

    resent_products = []
    resent_ids = request.session.get('resent_products', [])
    if resent_ids:
        resent_ids = resent_ids[::-1]
        for i in resent_ids:
            resent_products.append(get_object_or_404(ProductModel, pk=i))

    ctx = {
        'products': products,
        'resent_products': resent_products,
        'filter': catalog_filter,
    }

    return render(request, 'catalog.html', ctx)


class CatalogFilter(TemplateView):
    products = 'Error!'
    template_name = '/catalog_filtered/'

    def post(self, request):
        CatalogFilter.products = ProductModel.objects.all()
        colors = request.POST.getlist("color", None)
        sizes = request.POST.getlist("size", None)

        color_set = ProductModel.objects.filter(color__in=colors).order_by('color')
        CatalogFilter.products = color_set

        res_set = ''
        for i in sizes:
            res_set = CatalogFilter.products.intersection(ProductModel.objects.filter(size__contains=i))
        CatalogFilter.products = res_set.order_by('color')

        return redirect(self.template_name)


def product_detail(request, pk):
    product = get_object_or_404(ProductModel, pk=pk)
    translate = {
        'Бежевый': 'Beige',
        'Темно-Бежевый': 'Dark Beige',
        'Кэмел': 'Camel',
        'Фисташковый': 'Pistachio',
        'Мята': 'Mint',
        'Коррал': 'Coral',
        'Розовый': 'Pink',
        'Черный': 'Black'
    }
    if product.color in translate.keys():
        english_name = translate[product.color]
    else:
        english_name = 'Awesome Suit'

    sizes = product.size.replace(' ', '')
    sizes = sizes.split(',')

    if 'resent_products' not in request.session:
        request.session['resent_products'] = []
    if product.pk not in request.session['resent_products']:
        if len(request.session['resent_products']) == 3:
            del request.session['resent_products'][0]
        request.session['resent_products'].append(product.pk)
        request.session.modified = True
    ctx = {
        'product': product,
        'sizes': sizes,
        'english_name': english_name,
    }
    return render(request, 'product.html', ctx)


def cart_view(request):
    cart = CartModel.objects.filter(session_key=request.session.session_key)
    products = []
    empty = False
    for i in cart:
        product = ProductModel.objects.get(pk=i.product_id)
        product.size = i.size
        products.append(product)
    if not products:
        empty = True
    context = {
        'products': products,
        'empty': empty
    }
    return render(request, 'cart.html', context)


def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST['AddToCart']
        product_size = request.POST['size']
        if request.user.is_authenticated:
            cart, created = CartModel.objects.update_or_create(
                user=request.user, product_id=product_id, size=product_size,
                defaults={'session_key': request.session.session_key}
            )
        else:
            cart, created = CartModel.objects.get_or_create(
                session_key=request.session.session_key, product_id=product_id,
                size=product_size, defaults={'user': None}
            )
        try:
            cart.save()
        except IntegrityError:
            pass
        return redirect(reverse('product_detail', kwargs={'pk': product_id}))
    return HttpResponse('Somethings go wrong :(')


def del_from_cart(request):
    if request.method == 'POST':
        product = request.POST['del_from_cart'].split()
        product_id = product[0]
        product_size = product[1]
        if request.user.is_authenticated:
            CartModel.objects.filter(
                user=request.user,
                product_id=product_id,
                size=product_size
            ).delete()
        else:
            CartModel.objects.filter(
                session_key=request.session.session_key,
                product_id=product_id,
                size=product_size
            ).delete()
    return redirect('/cart/')


def one_click_buing(request):
    if request.method == 'POST':
        phone = request.POST['one_click_phone']
        pk = request.POST['product_pk']
        try:
            int(phone)
            one_click_order = OneClickOrderModel.objects.create(
                product_id=pk, phone=phone)
            one_click_order.save()
        except ValueError:
            pass
        return redirect("/{}/".format(pk))


class CheckOut(TemplateView):
    def get(self, request, *args, **kwargs):
        products = []
        cart = CartModel.objects.filter(session_key=request.session.session_key)
        for i in cart:
            product = ProductModel.objects.get(pk=i.product_id)
            product.size = i.size
            products.append(product)

        context = {
            'products': products
        }
        return render(request, 'checkout.html', context)

    def post(self, request):
        customer = request.POST['full_name']
        phone = request.POST['number']
        email = request.POST['email']
        shipping_by = request.POST['shiping_variant']
        address = ''
        addresses = [
            'addressNp1', 'addressNp2',
            'addressAl1', 'addressAl2',
            'addressUk1', 'addressUk2', 'addressUk3', 'addressUk4'
        ]

        for i in range(len(addresses)):
            temp = request.POST[addresses[i]]
            if temp != '':
                if i == 0:
                    address = '{}, отделение № {}'.format(request.POST[addresses[i]],
                                                          request.POST[addresses[i + 1]])
                    break
                if i == 2:
                    address = '{}, отделениe: {}'.format(request.POST[addresses[i]],
                                                         request.POST[addresses[i + 1]])
                    break
                if i == 4:
                    address = 'Область: {}, {}, {}, индекс: {}' \
                              ''.format(request.POST[addresses[i]], request.POST[addresses[i + 1]],
                                        request.POST[addresses[i + 2]], request.POST[addresses[i + 3]])
                    break

        details = request.POST['details']
        price = request.POST['totalPrice']
        order, created = OrderModel.objects.update_or_create(
            customer=customer, phone=phone, email=email, shipping_by=shipping_by,
            address=address, details=details, price=price)
        order.save()
        date = order.date.strftime("%Y-%m-%d")
        products, quantities, order_products = [], [], []
        cart = CartModel.objects.filter(session_key=request.session.session_key)
        for i in range(len(cart)):
            product = ProductModel.objects.get(pk=cart[i].product_id)
            product.size = cart[i].size
            products.append(product)
            quantity = int(request.POST['quan{}'.format(i)])
            quantities.append(quantity)
            item_price = quantity * product.price
            order_item, created = OrderItemsModel.objects.update_or_create(
                order=order, product=product, quantity=quantity, price=item_price)
            order_item.save()
            order_products.append(order_item.price)
            cart[i].delete()
        context = {
            'products': products,
            'quantities': quantities,
            'order_products': order_products,
            'date': date,
            'order': order
        }
        return render(request, 'thanks_for_buying.html', context)
