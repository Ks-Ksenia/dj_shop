from .models import MainMenu, Menu, SubMenu, Cart, Customer
from django.conf import settings


def context_processors(request):
    cart = request.session.get(settings.CART_SESSION_ID)

    context = {
        'main_menu_context': MainMenu.objects.all(),
        'menu_context': Menu.objects.all(),
        'submenu_context': SubMenu.objects.all(),
        'cart': cart,
    }

    if request.user.is_authenticated:
        customer, created = Customer.objects.get_or_create(user=request.user)

        try:
            cart = Cart.objects.get(customer=customer)
        except:
            context
        else:
            context['cart'] = cart

    return context

