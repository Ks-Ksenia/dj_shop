from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings

from .models import Cart, Customer


def context_processors(request):
    cart = request.session.get(settings.CART_SESSION_ID)
    q = request.session.get('q', 0)

    context = {
        'cart': cart,
        'total_q': q
    }

    if request.user.is_authenticated:
        customer, created = Customer.objects.get_or_create(user=request.user)

        try:
            cart = Cart.objects.get(customer=customer)
        except ObjectDoesNotExist:
            context
        else:
            context['cart'] = cart

    return context

