from django.conf import settings
from django.contrib import messages
from django.core.paginator import Paginator

from .models import *


def get_product(**kwargs):
    product_url = kwargs.get('url')
    model = kwargs.get('category')

    content_type = ContentType.objects.get(model=model)
    product = content_type.model_class().objects.get(url=product_url)

    return product, content_type, product_url, model


def cart_and_customer(request):
    customer = Customer.objects.get(user=request.user)
    cart, _ = Cart.objects.get_or_create(customer=customer)

    return cart, customer


""" Изменение количества товара в корзине для авторизованного пользователя"""

def add_quantity(request, quantity, cart_product, product):
    add_quantity = bool(request.POST.get('add_quantity'))

    if add_quantity:
        q = quantity + 1
        cart_product.quantity = q
        cart_product.final_price = cart_product.final_price + product.price

        messages.add_message(request, messages.INFO, 'Количество товара изменено', fail_silently=False)
        cart_product.save()


def rm_quantity(request, quantity, cart_product, product, cart):
    remove_quantity = bool(request.POST.get('remove_quantity'))

    if remove_quantity:
        if quantity - 1 > 0:
            q = quantity - 1
            cart_product.quantity = q
            cart_product.final_price = cart_product.final_price - product.price

            msg = messages.add_message(request, messages.INFO, 'Количество товара изменено', fail_silently=False)
            cart_product.save()
        else:
            cart.products.remove(cart_product)
            cart_product.delete()


""" Корзина для анонимного покупателя """
def init_cart(request):
    session = request.session
    cart = session.get(settings.CART_SESSION_ID)

    if not cart: cart = session[settings.CART_SESSION_ID] = {}

    return cart


def save_cart_anon(request, cart):
    session = request.session
    session[settings.CART_SESSION_ID] = cart
    session.modified = True


def get_product_for_anon_cart(request, cart):
    products = []
    total_price = 0
    request.session['q'] = 0
    for i in cart:

        url = cart[i].get('url')
        model = cart[i].get('model')

        content_type = ContentType.objects.get(model=model)
        product = content_type.model_class().objects.get(url=url)

        products.append(product)

        total_price += cart[i]['final_price']


        request.session['q'] += int(cart[i].get('quantity'))

    return products, total_price


def add_quantity_anon_cart(request, cart, product, product_url):
    add_quantity = bool(request.POST.get('add_quantity'))

    if add_quantity:
        cart[product_url]['quantity'] += 1
        cart[product_url]['final_price'] = cart[product_url]['quantity'] * product.price

        messages.add_message(request, messages.INFO, 'Количество товара изменено', fail_silently=False)


def rm_quantity_anon_cart(request, cart, product, product_url):
    rm_quantity = bool(request.POST.get('remove_quantity'))

    if rm_quantity:
        if cart[product_url]['quantity'] != 1:
            cart[product_url]['quantity'] -= 1
            cart[product_url]['final_price'] = cart[product_url]['quantity'] * product.price

            messages.add_message(request, messages.INFO, 'Количество товара изменено', fail_silently=False)
        else:
            del cart[product_url]


def pagination(request, object_list, number_page):
    paginator = Paginator(object_list, number_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    object_list = page_obj.object_list

    full_path = request.get_full_path()
    start = full_path.find('?ordering')
    end = full_path.rfind('&page')

    ordering_path = ''

    if start != -1:
        ordering_path = full_path[start + 1:]
        if end != -1:
            ordering_path = full_path[start + 1: end]

    return object_list, ordering_path, page_obj, paginator

