from random import randint

from django.db import transaction
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic import ListView, DetailView, CreateView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib import messages

from itertools import chain

from .models import *
from .forms import *
from .services import *


class index(View):
    def get(self, request):
        return redirect('main_menu_url')


class Search(ListView):
    paginate_by = 2
    template_name = 'base_list.html'

    def get_queryset(self):

        query = self.request.GET.get('q')

        if query != '' and query != ' ':
            filter = Q(model__icontains=query) | Q(type__icontains=query)

            search_drymachine = DryMachine.objects.filter(filter)
            search_washmachine = WashMachine.objects.filter(filter)
            search_iron = Iron.objects.filter(filter)
            search_fridge = Fridge.objects.filter(filter)
            search_stove = Stove.objects.filter(filter)
            search_microwave_oven = MicrowaveOven.objects.filter(filter)
            search_kettle = Kettle.objects.filter(filter)
            search_hairdryer = Hairdryer.objects.filter(filter)
            search_hair_clipper = HairClipper.objects.filter(filter)
            search_smartphone = Smartphone.objects.filter(filter)
            search_smart_watch = SmartWatch.objects.filter(filter)
            search_tablet = Tablet.objects.filter(filter)
            search_ebook = EBook.objects.filter(filter)
            search_TV = TV.objects.filter(filter)
            search_bracketTV = BracketTV.objects.filter(filter)
            search_column = Column.objects.filter(filter)
            search_headphones = Headphones.objects.filter(filter)
            search_notebook = Notebook.objects.filter(filter)
            search_system_unit = SystemUnit.objects.filter(filter)
            search_server = Server.objects.filter(filter)
            search_processor = Processor.objects.filter(filter)
            search_motherboard = Motherboard.objects.filter(filter)
            search_video_card = VideoCard.objects.filter(filter)
            search_RAMmemory = RAMMemory.objects.filter(filter)

            result = list(chain(search_drymachine, search_washmachine, search_iron))

        else:
            result = list()

        return result

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)

        context['q'] = f"q={self.request.GET.get('q')}&"

        return context


class AddReview(View):

    def post(self, request, *args, **kwargs):
        form = ReviewForm(request.POST)

        if form.is_valid():
            product, content_type, *kwargs = get_product(**kwargs)

            review = Review.objects.create(
                name=form.cleaned_data['name'],
                text=form.cleaned_data['text'],
                content_type=content_type,
                object_id=product.id,
                comment_for_product=product)

            return HttpResponseRedirect(request.path_info)

    def get(self, request, *args, **kwargs):
        form = ReviewForm()

        product, content_type, *kwargs = get_product(**kwargs)

        review = Review.objects.filter(content_type=content_type, object_id=product.id)

        product.review = review.count()
        product.save()

        context = {'form': form, 'review': review, 'object': product}
        return render(request, 'shop/review.html', context)


class Description(View):

    def get(self, request, *args, **kwargs):
        product, *kwargs = get_product(**kwargs)
        return render(request, 'shop/description.html', {'object': product})


class SingUp(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    template_name = 'shop/singup.html'


class MainMenuList(ListView):
    model = MainMenu
    template_name_suffix = '_menu'


class MenuView(View):

    # ?????????????????? ?????????? ???? ???? ?????????? ???????????? ?????????? ????????
    def __init__(self):
        self.URL_LIST = (
            'menu_home_appliances_url',
            'menu_smart_tablet_url',
            'menu_TV_audio_url',
            'menu_computer_url'

        )

    def get(self, request, url):
        url = url
        menu = Menu.objects.all()
        if url in self.URL_LIST:
            main_menu = MainMenu.objects.get(url=url)
        else:
            return HttpResponseRedirect('/shop/404.html')

        return render(request, 'shop/menu_menu.html', {'main_menu': main_menu, 'menu': menu})


class SubMenuView(View):

    def __init__(self):
        self.URL_LIST = (
            'kitchen_url',
            'house_url',
            'beautifil_health_url', # ?????????????????? ???????????????? ??????????!
            'smartphone_gadgets_url',
            'tablet_book_url',
            'TB_accessories_url',
            'audio_url',
            'computer_notebook_url',
            'PC_accessories_url'
        )

    def get(self, request, url):
        url = url
        submenu = SubMenu.objects.all()
        if url in self.URL_LIST:
            menu = Menu.objects.get(url=url)
        else:
            return HttpResponseRedirect('/shop/catalog/')

        return render(request, 'shop/submenu_menu.html', {'menu': menu, 'submenu': submenu})


class CartView(View):

    def get(self, request):
        cart, customer = cart_and_customer(request)
        cart.cart_sum()

        return render(request, 'shop/cart.html', {'customer': customer, 'cart': cart})


class AddToCartView(View):

    def get(self, request, *args, **kwargs):
        cart, customer = cart_and_customer(request)
        product, content_type, *kwargs = get_product(**kwargs)

        cart_product, created = CartProduct.objects.get_or_create(
            user=cart.customer,
            cart=cart,
            content_type=content_type,
            object_id=product.id,
            product_price=product.price
        )

        if created: cart.products.add(cart_product)

        cart.save()

        return HttpResponseRedirect('/shop/cart')


class DeleteToCartView(View):

    def get(self, request, *args, **kwargs):
        cart, customer = cart_and_customer(request)
        product, content_type, *kwargs = get_product(**kwargs)

        cart_product = CartProduct.objects.get(
            user=cart.customer,
            cart=cart,
            content_type=content_type,
            object_id=product.id,
        )

        cart.products.remove(cart_product)  # ?????????????? ?????????? ???? html ??????????????
        cart_product.delete()  # ?????????????? ?????????? ???? ???????? ????????????
        cart.save()

        return HttpResponseRedirect('/shop/cart/')


class ChangeQuantityView(View):

    def post(self, request, *args, **kwargs):
        cart, customer = cart_and_customer(request)
        product, content_type, *kwargs = get_product(**kwargs)

        cart_product = CartProduct.objects.get(
            user=customer,
            cart=cart,
            content_type=content_type,
            object_id=product.id,
        )
        quantity = int(request.POST.get('quantity'))

        add_quantity(request, quantity, cart_product, product)
        rm_quantity(request, quantity, cart_product, product, cart)

        cart.save()

        return HttpResponseRedirect('/shop/cart/')


class CartAnonView(View):

    def get(self, request):
        cart = init_cart(request)
        products, total_price = get_product_for_anon_cart(cart)

        context = {'cart': cart, 'products': products, 'total_price': total_price}

        return render(request, 'shop/cart_anon.html', context)


class AddToCartAnonView(View):

    def get(self, request, *args, **kwargs):
        product, _, product_url, model = get_product(**kwargs)

        cart = init_cart(request)

        if product.url not in cart:
            cart[product.url] = {'url': product_url,
                                 'model': model,
                                 'quantity': 1,
                                 'final_price': product.price
                                 }

        products, _ = get_product_for_anon_cart(cart)

        save_cart_anon(request, cart)

        return HttpResponseRedirect('/shop/cart_anon/')


class DelToCartAnonView(View):

    def get(self, request, *args, **kwargs):
        product_url = kwargs.get('url')
        cart = init_cart(request)

        del cart[product_url]

        save_cart_anon(request, cart)

        return HttpResponseRedirect('/shop/cart_anon/')


class ChangeQuantityCartAnonView(View):

    def post(self, request, *args, **kwargs):
        cart = init_cart(request)
        product, _, product_url, _ = get_product(**kwargs)

        add_quantity_anon_cart(request, cart, product, product_url)
        rm_quantity_anon_cart(request, cart, product, product_url)

        save_cart_anon(request, cart)

        return HttpResponseRedirect('/shop/cart_anon/')


class OrderRegistrationView(View):
    
    def get(self, request):
        if request.user.is_authenticated:
            cart, _ = cart_and_customer(request)
            order = Order.objects.all()

            form = OrderForm()

            context = {'cart': cart, 'order': order, 'form': form}
            return render(request, 'shop/order_registration.html', context)
        else:
            messages.add_message(request, messages.INFO, '??????????????, ?????????? ???????????????? ??????????')
            return HttpResponseRedirect('/accounts/login')


class MakeOrderView(View):

    @transaction.atomic
    def post(self, request):
        cart, customer = cart_and_customer(request)

        form = OrderForm(request.POST)

        if form.is_valid():

            number = randint(1, 9999)
            order = Order.objects.create(
                customer=customer,
                cart=cart,
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                phone=form.cleaned_data['phone'],
                address=form.cleaned_data['address'],
                buying_type=form.cleaned_data['buying_type'],
                number=number,
            )

            for cart_product in CartProduct.objects.filter(user=customer, cart=cart):
                order.products_for_order += f'{cart_product}\n'

            customer.order.add(order)
            order.save()

            return render(request, 'shop/order_end.html', context={'order': order})
        return HttpResponseRedirect('/shop/registration_order/')


class FridgeView(View):
    def get(self, request, *args, **kwargs):
        category = Fridge.objects.first().category

        object_list = Fridge.objects.all()

        form = FridgeForm(request.GET)

        if form.is_valid():

            if form.cleaned_data['min_price']:
                object_list = object_list.filter(price__gte=form.cleaned_data['min_price'])

            if form.cleaned_data['max_price']:
                object_list = object_list.filter(price__lte=form.cleaned_data['max_price'])

            if form.cleaned_data['cold_storage_system']:
                object_list = object_list.filter(cold_storage_system__in=form.cleaned_data['cold_storage_system'])

            if form.cleaned_data['location_freezer_NTO']:
                object_list = object_list.filter(location_freezer_NTO__in=form.cleaned_data['location_freezer_NTO'])

            if form.cleaned_data['ordering']:
                object_list = object_list.order_by(form.cleaned_data['ordering'])

        object_list, ordering_path, page_obj, paginator = pagination(request, object_list, 5)

        context = {'form': form,
                   'category': category,
                   'object_list': object_list,
                   'ordering_path': ordering_path,
                   'page_obj': page_obj,
                   'paginator': paginator}

        return render(request, 'shop/fridge_list.html', context)


class FridgeDetail(DetailView):
    model = Fridge
    slug_field = 'url'
    slug_url_kwarg = 'url'


class StoveView(View):
    def get(self, request, *args, **kwargs):
        category = Stove.objects.first().category

        object_list = Stove.objects.all()

        form = StoveForm(request.GET)

        if form.is_valid():

            if form.cleaned_data['min_price']:
                object_list = object_list.filter(price__gte=form.cleaned_data['min_price'])

            if form.cleaned_data['max_price']:
                object_list = object_list.filter(price__lte=form.cleaned_data['max_price'])

            if form.cleaned_data['material_cover_panel']:
                object_list = object_list.filter(material_cover_panel__in=form.cleaned_data['material_cover_panel'])

            if form.cleaned_data['total_number_burnets']:
                object_list = object_list.filter(total_number_burnets__in=form.cleaned_data['total_number_burnets'])

            if form.cleaned_data['grill']:
                object_list = object_list.filter(grill__in=form.cleaned_data['grill'])

            if form.cleaned_data['timer']:
                object_list = object_list.filter(timer__in=form.cleaned_data['timer'])

            if form.cleaned_data['ordering']:
                object_list = object_list.order_by(form.cleaned_data['ordering'])

        object_list, ordering_path, page_obj, paginator = pagination(request, object_list, 5)

        context = {'form': form,
                   'category': category,
                   'object_list': object_list,
                   'ordering_path': ordering_path,
                   'page_obj': page_obj,
                   'paginator': paginator}

        return render(request, 'shop/stove_list.html', context)


class StoveDetail(DetailView):
    model = Stove
    slug_field = 'url'
    slug_url_kwarg = 'url'


class MicrowaveOvenView(View):
    def get(self, request, *args, **kwargs):
        category = MicrowaveOven.objects.first().category

        object_list = MicrowaveOven.objects.all()

        form = MicrowaveOvenForm(request.GET)

        if form.is_valid():

            if form.cleaned_data['min_price']:
                object_list = object_list.filter(price__gte=form.cleaned_data['min_price'])

            if form.cleaned_data['max_price']:
                object_list = object_list.filter(price__lte=form.cleaned_data['max_price'])

            if form.cleaned_data['type_management']:
                object_list = object_list.filter(type_management__in=form.cleaned_data['type_management'])

            if form.cleaned_data['display']:
                object_list = object_list.filter(display__in=form.cleaned_data['display'])

            if form.cleaned_data['block_child']:
                object_list = object_list.filter(block_child__in=form.cleaned_data['block_child'])

            if form.cleaned_data['ordering']:
                object_list = object_list.order_by(form.cleaned_data['ordering'])

        object_list, ordering_path, page_obj, paginator = pagination(request, object_list, 5)

        context = {'form': form,
                   'category': category,
                   'object_list': object_list,
                   'ordering_path': ordering_path,
                   'page_obj': page_obj,
                   'paginator': paginator}

        return render(request, 'shop/microwaveoven_list.html', context)


class MicrowaveOvenDetail(DetailView):
    model = MicrowaveOven
    slug_field = 'url'
    slug_url_kwarg = 'url'



class KettleView(View):
    def get(self, request, *args, **kwargs):
        category = Kettle.objects.first().category

        object_list = Kettle.objects.all()

        form = KettleForm(request.GET)

        if form.is_valid():

            if form.cleaned_data['min_price']:
                object_list = object_list.filter(price__gte=form.cleaned_data['min_price'])

            if form.cleaned_data['max_price']:
                object_list = object_list.filter(price__lte=form.cleaned_data['max_price'])

            if form.cleaned_data['body_material']:
                object_list = object_list.filter(body_material__in=form.cleaned_data['body_material'])

            if form.cleaned_data['light']:
                object_list = object_list.filter(light__in=form.cleaned_data['light'])

            if form.cleaned_data['ordering']:
                object_list = object_list.order_by(form.cleaned_data['ordering'])

        object_list, ordering_path, page_obj, paginator = pagination(request, object_list, 5)

        context = {'form': form,
                   'category': category,
                   'object_list': object_list,
                   'ordering_path': ordering_path,
                   'page_obj': page_obj,
                   'paginator': paginator}

        return render(request, 'shop/kettle_list.html', context)



class KettleDetail(DetailView):
    model = Kettle
    slug_field = 'url'
    slug_url_kwarg = 'url'


class WashMachineView(View):
    def get(self, request, *args, **kwargs):
        category = WashMachine.objects.first().category

        object_list = WashMachine.objects.all()

        form = WashMachineForm(request.GET)

        if form.is_valid():

            if form.cleaned_data['min_price']:
                object_list = object_list.filter(price__gte=form.cleaned_data['min_price'])

            if form.cleaned_data['max_price']:
                object_list = object_list.filter(price__lte=form.cleaned_data['max_price'])

            if form.cleaned_data['upload_type']:
                object_list = object_list.filter(upload_type__in=form.cleaned_data['upload_type'])

            if form.cleaned_data['drive']:
                object_list = object_list.filter(drive__in=form.cleaned_data['drive'])

            if form.cleaned_data['leak']:
                object_list = object_list.filter(leak__in=form.cleaned_data['leak'])

            if form.cleaned_data['ordering']:
                object_list = object_list.order_by(form.cleaned_data['ordering'])

        object_list, ordering_path, page_obj, paginator = pagination(request, object_list, 5)

        context = {'form': form,
                   'category': category,
                   'object_list': object_list,
                   'ordering_path': ordering_path,
                   'page_obj': page_obj,
                   'paginator': paginator}

        return render(request, 'shop/washmachine_list.html', context)


class WashMachineDetail(DetailView):
    model = WashMachine
    slug_field = 'url'
    slug_url_kwarg = 'url'


class DryMachineView(View):
    def get(self, request, *args, **kwargs):
        category = DryMachine.objects.first().category

        object_list = DryMachine.objects.all()

        form = DryMachineForm(request.GET)

        if form.is_valid():

            if form.cleaned_data['min_price']:
                object_list = object_list.filter(price__gte=form.cleaned_data['min_price'])

            if form.cleaned_data['max_price']:
                object_list = object_list.filter(price__lte=form.cleaned_data['max_price'])


## ???????????????? ???????????? ???????????????????? ?? heat_pump ?? block_child

            if len(form.cleaned_data['heat_pump']) == 1:
                object_list = object_list.filter(heat_pump=form.cleaned_data['heat_pump'][0])

            if len(form.cleaned_data['block_child']) == 1:
                object_list = object_list.filter(block_child=form.cleaned_data['block_child'][0])

            # if 0 < len(form.cleaned_data['max_load']) < 5:
            #     object_list = object_list.filter(max_load__in=form.cleaned_data['max_load'])

            if form.cleaned_data['max_load']:
                object_list = object_list.filter(max_load__in=form.cleaned_data['max_load'])

            if form.cleaned_data['ordering']:
                object_list = object_list.order_by(form.cleaned_data['ordering'])

        object_list, ordering_path, page_obj, paginator = pagination(request, object_list, 5)

        context = {'form': form,
                   'category': category,
                   'object_list': object_list,
                   'ordering_path': ordering_path,
                   'page_obj': page_obj,
                   'paginator': paginator}

        return render(request, 'shop/drymachine_list.html', context)


class DryMachineDetail(DetailView):
    model = DryMachine
    slug_field = 'url'
    slug_url_kwarg = 'url'


class IronView(View):
    def get(self, request, *args, **kwargs):

        category = Iron.objects.first().category

        object_list = Iron.objects.all()

        form = IronForm(request.GET)

        if form.is_valid():

            if form.cleaned_data['min_price']:
                object_list = object_list.filter(price__gte=form.cleaned_data['min_price'])

            if form.cleaned_data['max_price']:
                object_list = object_list.filter(price__lte=form.cleaned_data['max_price'])

            if form.cleaned_data['auto_shutdown']:
                object_list = object_list.filter(auto_shutdown__in=form.cleaned_data['auto_shutdown'])

            if form.cleaned_data['descaling_protection']:
                object_list = object_list.filter(descaling_protection__in=form.cleaned_data['descaling_protection'])

            if form.cleaned_data['ordering']:
                object_list = object_list.order_by(form.cleaned_data['ordering'])

        object_list, ordering_path, page_obj, paginator = pagination(request, object_list, 5)

        context = {'form': form,
                   'category': category,
                   'object_list': object_list,
                   'ordering_path': ordering_path,
                   'page_obj': page_obj,
                   'paginator': paginator}

        return render(request, 'shop/iron_list.html', context)


class IronDetail(DetailView):
    model = Iron
    slug_field = 'url'
    slug_url_kwarg = 'url'


class HairdryerView(View):
    def get(self, request, *args, **kwargs):
        category = Hairdryer.objects.first().category

        object_list = Hairdryer.objects.all()

        form = HairdryerForm(request.GET)

        if form.is_valid():

            if form.cleaned_data['min_price']:
                object_list = object_list.filter(price__gte=form.cleaned_data['min_price'])

            if form.cleaned_data['max_price']:
                object_list = object_list.filter(price__lte=form.cleaned_data['max_price'])

            if form.cleaned_data['cold_air_supply']:
                object_list = object_list.filter(cold_air_supply__in=form.cleaned_data['cold_air_supply'])

            if form.cleaned_data['ionization']:
                object_list = object_list.filter(ionization__in=form.cleaned_data['ionization'])

            if form.cleaned_data['ordering']:
                object_list = object_list.order_by(form.cleaned_data['ordering'])

        object_list, ordering_path, page_obj, paginator = pagination(request, object_list, 5)

        context = {'form': form,
                   'category': category,
                   'object_list': object_list,
                   'ordering_path': ordering_path,
                   'page_obj': page_obj,
                   'paginator': paginator}

        return render(request, 'shop/hairdryer_list.html', context)


class HairdryerDetail(DetailView):
    model = Hairdryer
    slug_field = 'url'
    slug_url_kwarg = 'url'


class HairClipperView(View):
    def get(self, request, *args, **kwargs):
        category = HairClipper.objects.first().category

        object_list = HairClipper.objects.all()

        form = HairClipperForm(request.GET)

        if form.is_valid():

            if form.cleaned_data['min_price']:
                object_list = object_list.filter(price__gte=form.cleaned_data['min_price'])

            if form.cleaned_data['max_price']:
                object_list = object_list.filter(price__lte=form.cleaned_data['max_price'])

            if form.cleaned_data['type_engine']:
                object_list = object_list.filter(type_engine__in=form.cleaned_data['type_engine'])

            if form.cleaned_data['food']:
                object_list = object_list.filter(food__in=form.cleaned_data['food'])

            if form.cleaned_data['ordering']:
                object_list = object_list.order_by(form.cleaned_data['ordering'])

        object_list, ordering_path, page_obj, paginator = pagination(request, object_list, 5)

        context = {'form': form,
                   'category': category,
                   'object_list': object_list,
                   'ordering_path': ordering_path,
                   'page_obj': page_obj,
                   'paginator': paginator}

        return render(request, 'shop/hairclipper_list.html', context)


class HairClipperDetail(DetailView):
    model = HairClipper
    slug_field = 'url'
    slug_url_kwarg = 'url'


class SmartphoneView(View):
    def get(self, request, *args, **kwargs):
        category = Smartphone.objects.first().category

        object_list = Smartphone.objects.all()

        form = SmartphoneForm(request.GET)

        if form.is_valid():

            if form.cleaned_data['min_price']:
                object_list = object_list.filter(price__gte=form.cleaned_data['min_price'])

            if form.cleaned_data['max_price']:
                object_list = object_list.filter(price__lte=form.cleaned_data['max_price'])

            if form.cleaned_data['amount_RAM']:
                object_list = object_list.filter(amount_RAM__in=form.cleaned_data['amount_RAM'])

            if form.cleaned_data['amount_internal_memory']:
                object_list = object_list.filter(amount_internal_memory__in=form.cleaned_data['amount_internal_memory'])

            if form.cleaned_data['ordering']:
                object_list = object_list.order_by(form.cleaned_data['ordering'])

        object_list, ordering_path, page_obj, paginator = pagination(request, object_list, 5)

        context = {'form': form,
                   'category': category,
                   'object_list': object_list,
                   'ordering_path': ordering_path,
                   'page_obj': page_obj,
                   'paginator': paginator}

        return render(request, 'shop/smartphone_list.html', context)


class SmartphoneDetail(DetailView):
    model = Smartphone
    slug_field = 'url'
    slug_url_kwarg = 'url'


class SmartWatchView(View):
    def get(self, request, *args, **kwargs):
        category = SmartWatch.objects.first().category

        object_list = SmartWatch.objects.all()

        form = SmartWatchForm(request.GET)

        if form.is_valid():

            if form.cleaned_data['min_price']:
                object_list = object_list.filter(price__gte=form.cleaned_data['min_price'])

            if form.cleaned_data['max_price']:
                object_list = object_list.filter(price__lte=form.cleaned_data['max_price'])


            if form.cleaned_data['ordering']:
                object_list = object_list.order_by(form.cleaned_data['ordering'])

        object_list, ordering_path, page_obj, paginator = pagination(request, object_list, 5)

        context = {'form': form,
                   'category': category,
                   'object_list': object_list,
                   'ordering_path': ordering_path,
                   'page_obj': page_obj,
                   'paginator': paginator}

        return render(request, 'shop/smartwatch_list.html', context)


class SmartWatchDetail(DetailView):
    model = SmartWatch
    slug_field = 'url'
    slug_url_kwarg = 'url'


class TabletView(View):
    def get(self, request, *args, **kwargs):
        category = Tablet.objects.first().category

        object_list = Tablet.objects.all()

        form = TabletForm(request.GET)

        if form.is_valid():

            if form.cleaned_data['min_price']:
                object_list = object_list.filter(price__gte=form.cleaned_data['min_price'])

            if form.cleaned_data['max_price']:
                object_list = object_list.filter(price__lte=form.cleaned_data['max_price'])


            if form.cleaned_data['ordering']:
                object_list = object_list.order_by(form.cleaned_data['ordering'])

        object_list, ordering_path, page_obj, paginator = pagination(request, object_list, 5)

        context = {'form': form,
                   'category': category,
                   'object_list': object_list,
                   'ordering_path': ordering_path,
                   'page_obj': page_obj,
                   'paginator': paginator}

        return render(request, 'shop/tablet_list.html', context)


class TabletDetail(DetailView):
    model = Tablet
    slug_field = 'url'
    slug_url_kwarg = 'url'


class EBookView(View):
    def get(self, request, *args, **kwargs):
        category = EBook.objects.first().category

        object_list = EBook.objects.all()

        form = EBookForm(request.GET)

        if form.is_valid():

            if form.cleaned_data['min_price']:
                object_list = object_list.filter(price__gte=form.cleaned_data['min_price'])

            if form.cleaned_data['max_price']:
                object_list = object_list.filter(price__lte=form.cleaned_data['max_price'])


            if form.cleaned_data['ordering']:
                object_list = object_list.order_by(form.cleaned_data['ordering'])

        object_list, ordering_path, page_obj, paginator = pagination(request, object_list, 5)

        context = {'form': form,
                   'category': category,
                   'object_list': object_list,
                   'ordering_path': ordering_path,
                   'page_obj': page_obj,
                   'paginator': paginator}

        return render(request, 'shop/ebook_list.html', context)


class EBookDetail(DetailView):
    model = EBook
    slug_field = 'url'
    slug_url_kwarg = 'url'


class TVView(View):
    def get(self, request, *args, **kwargs):
        category = TV.objects.first().category

        object_list = TV.objects.all()

        form = TVForm(request.GET)

        if form.is_valid():

            if form.cleaned_data['min_price']:
                object_list = object_list.filter(price__gte=form.cleaned_data['min_price'])

            if form.cleaned_data['max_price']:
                object_list = object_list.filter(price__lte=form.cleaned_data['max_price'])


            if form.cleaned_data['ordering']:
                object_list = object_list.order_by(form.cleaned_data['ordering'])

        object_list, ordering_path, page_obj, paginator = pagination(request, object_list, 5)

        context = {'form': form,
                   'category': category,
                   'object_list': object_list,
                   'ordering_path': ordering_path,
                   'page_obj': page_obj,
                   'paginator': paginator}

        return render(request, 'shop/tv_list.html', context)


class TVDetail(DetailView):
    model = TV
    slug_field = 'url'
    slug_url_kwarg = 'url'



class BracketTVView(View):
    def get(self, request, *args, **kwargs):
        category = BracketTV.objects.first().category

        object_list = BracketTV.objects.all()

        form = BracketTVForm(request.GET)

        if form.is_valid():

            if form.cleaned_data['min_price']:
                object_list = object_list.filter(price__gte=form.cleaned_data['min_price'])

            if form.cleaned_data['max_price']:
                object_list = object_list.filter(price__lte=form.cleaned_data['max_price'])



            if form.cleaned_data['ordering']:
                object_list = object_list.order_by(form.cleaned_data['ordering'])

        object_list, ordering_path, page_obj, paginator = pagination(request, object_list, 5)

        context = {'form': form,
                   'category': category,
                   'object_list': object_list,
                   'ordering_path': ordering_path,
                   'page_obj': page_obj,
                   'paginator': paginator}

        return render(request, 'shop/brackettv_list.html', context)


class BracketTVDetail(DetailView):
    model = BracketTV
    slug_field = 'url'
    slug_url_kwarg = 'url'



class ColumnView(View):
    def get(self, request, *args, **kwargs):
        category = Column.objects.first().category

        object_list = Column.objects.all()

        form = ColumnForm(request.GET)

        if form.is_valid():

            if form.cleaned_data['min_price']:
                object_list = object_list.filter(price__gte=form.cleaned_data['min_price'])

            if form.cleaned_data['max_price']:
                object_list = object_list.filter(price__lte=form.cleaned_data['max_price'])


            if form.cleaned_data['ordering']:
                object_list = object_list.order_by(form.cleaned_data['ordering'])

        object_list, ordering_path, page_obj, paginator = pagination(request, object_list, 5)

        context = {'form': form,
                   'category': category,
                   'object_list': object_list,
                   'ordering_path': ordering_path,
                   'page_obj': page_obj,
                   'paginator': paginator}

        return render(request, 'shop/column_list.html', context)


class ColumnDetail(DetailView):
    model = Column
    slug_field = 'url'
    slug_url_kwarg = 'url'


class HeadphonesView(View):
    def get(self, request, *args, **kwargs):
        category = Headphones.objects.first().category

        object_list = Headphones.objects.all()

        form = HeadphonesForm(request.GET)

        if form.is_valid():

            if form.cleaned_data['min_price']:
                object_list = object_list.filter(price__gte=form.cleaned_data['min_price'])

            if form.cleaned_data['max_price']:
                object_list = object_list.filter(price__lte=form.cleaned_data['max_price'])



            if form.cleaned_data['ordering']:
                object_list = object_list.order_by(form.cleaned_data['ordering'])

        object_list, ordering_path, page_obj, paginator = pagination(request, object_list, 5)

        context = {'form': form,
                   'category': category,
                   'object_list': object_list,
                   'ordering_path': ordering_path,
                   'page_obj': page_obj,
                   'paginator': paginator}

        return render(request, 'shop/headphones_list.html', context)


class HeadphonesDetail(DetailView):
    model = Headphones
    slug_field = 'url'
    slug_url_kwarg = 'url'


class NotebookView(View):
    def get(self, request, *args, **kwargs):
        category = Notebook.objects.first().category

        object_list = Notebook.objects.all()

        form = NotebookForm(request.GET)

        if form.is_valid():

            if form.cleaned_data['min_price']:
                object_list = object_list.filter(price__gte=form.cleaned_data['min_price'])

            if form.cleaned_data['max_price']:
                object_list = object_list.filter(price__lte=form.cleaned_data['max_price'])



            if form.cleaned_data['ordering']:
                object_list = object_list.order_by(form.cleaned_data['ordering'])

        object_list, ordering_path, page_obj, paginator = pagination(request, object_list, 5)

        context = {'form': form,
                   'category': category,
                   'object_list': object_list,
                   'ordering_path': ordering_path,
                   'page_obj': page_obj,
                   'paginator': paginator}

        return render(request, 'shop/notebook_list.html', context)


class NotebookDetail(DetailView):
    model = Notebook
    slug_field = 'url'
    slug_url_kwarg = 'url'


class SystemUnitView(View):
    def get(self, request, *args, **kwargs):
        category = SystemUnit.objects.first().category

        object_list = SystemUnit.objects.all()

        form = SystemUnitForm(request.GET)

        if form.is_valid():

            if form.cleaned_data['min_price']:
                object_list = object_list.filter(price__gte=form.cleaned_data['min_price'])

            if form.cleaned_data['max_price']:
                object_list = object_list.filter(price__lte=form.cleaned_data['max_price'])



            if form.cleaned_data['ordering']:
                object_list = object_list.order_by(form.cleaned_data['ordering'])

        object_list, ordering_path, page_obj, paginator = pagination(request, object_list, 5)

        context = {'form': form,
                   'category': category,
                   'object_list': object_list,
                   'ordering_path': ordering_path,
                   'page_obj': page_obj,
                   'paginator': paginator}

        return render(request, 'shop/systemunit_list.html', context)


class SystemUnitDetail(DetailView):
    model = SystemUnit
    slug_field = 'url'
    slug_url_kwarg = 'url'


class ServerView(View):
    def get(self, request, *args, **kwargs):
        category = Server.objects.first().category

        object_list = Server.objects.all()

        form = ServerForm(request.GET)

        if form.is_valid():

            if form.cleaned_data['min_price']:
                object_list = object_list.filter(price__gte=form.cleaned_data['min_price'])

            if form.cleaned_data['max_price']:
                object_list = object_list.filter(price__lte=form.cleaned_data['max_price'])

            if form.cleaned_data['ordering']:
                object_list = object_list.order_by(form.cleaned_data['ordering'])

        object_list, ordering_path, page_obj, paginator = pagination(request, object_list, 5)

        context = {'form': form,
                   'category': category,
                   'object_list': object_list,
                   'ordering_path': ordering_path,
                   'page_obj': page_obj,
                   'paginator': paginator}

        return render(request, 'shop/server_list.html', context)


class ServerDetail(DetailView):
    model = Server
    slug_field = 'url'
    slug_url_kwarg = 'url'


class ProcessorView(View):
    def get(self, request, *args, **kwargs):
        category = Processor.objects.first().category

        object_list = Processor.objects.all()

        form = ProcessorForm(request.GET)

        if form.is_valid():

            if form.cleaned_data['min_price']:
                object_list = object_list.filter(price__gte=form.cleaned_data['min_price'])

            if form.cleaned_data['max_price']:
                object_list = object_list.filter(price__lte=form.cleaned_data['max_price'])



            if form.cleaned_data['ordering']:
                object_list = object_list.order_by(form.cleaned_data['ordering'])

        object_list, ordering_path, page_obj, paginator = pagination(request, object_list, 5)

        context = {'form': form,
                   'category': category,
                   'object_list': object_list,
                   'ordering_path': ordering_path,
                   'page_obj': page_obj,
                   'paginator': paginator}

        return render(request, 'shop/processor_list.html', context)


class ProcessorDetail(DetailView):
    model = Processor
    slug_field = 'url'
    slug_url_kwarg = 'url'



class MotherboardView(View):
    def get(self, request, *args, **kwargs):
        category = Motherboard.objects.first().category

        object_list = Motherboard.objects.all()

        form = MotherboardForm(request.GET)

        if form.is_valid():

            if form.cleaned_data['min_price']:
                object_list = object_list.filter(price__gte=form.cleaned_data['min_price'])

            if form.cleaned_data['max_price']:
                object_list = object_list.filter(price__lte=form.cleaned_data['max_price'])

            if form.cleaned_data['ordering']:
                object_list = object_list.order_by(form.cleaned_data['ordering'])

        object_list, ordering_path, page_obj, paginator = pagination(request, object_list, 5)

        context = {'form': form,
                   'category': category,
                   'object_list': object_list,
                   'ordering_path': ordering_path,
                   'page_obj': page_obj,
                   'paginator': paginator}
        return render(request, 'shop/motherboard_list.html', context)


class MotherboardDetail(DetailView):
    model = Motherboard
    slug_field = 'url'
    slug_url_kwarg = 'url'


class VideoCardView(View):
    def get(self, request, *args, **kwargs):
        category = VideoCard.objects.first().category

        object_list = VideoCard.objects.all()

        form = VideoCardForm(request.GET)

        if form.is_valid():

            if form.cleaned_data['min_price']:
                object_list = object_list.filter(price__gte=form.cleaned_data['min_price'])

            if form.cleaned_data['max_price']:
                object_list = object_list.filter(price__lte=form.cleaned_data['max_price'])


            if form.cleaned_data['ordering']:
                object_list = object_list.order_by(form.cleaned_data['ordering'])

        object_list, ordering_path, page_obj, paginator = pagination(request, object_list, 5)

        context = {'form': form,
                   'category': category,
                   'object_list': object_list,
                   'ordering_path': ordering_path,
                   'page_obj': page_obj,
                   'paginator': paginator}

        return render(request, 'shop/videocard_list.html', context)


class VideoCardDetail(DetailView):
    model = VideoCard
    slug_field = 'url'
    slug_url_kwarg = 'url'


class RAMMemoryView(View):
    def get(self, request, *args, **kwargs):
        category = RAMMemory.objects.first().category

        object_list = RAMMemory.objects.all()

        form = RAMMemoryForm(request.GET)

        if form.is_valid():

            if form.cleaned_data['min_price']:
                object_list = object_list.filter(price__gte=form.cleaned_data['min_price'])

            if form.cleaned_data['max_price']:
                object_list = object_list.filter(price__lte=form.cleaned_data['max_price'])




            if form.cleaned_data['ordering']:
                object_list = object_list.order_by(form.cleaned_data['ordering'])

        object_list, ordering_path, page_obj, paginator = pagination(request, object_list, 5)

        context = {'form': form,
                   'category': category,
                   'object_list': object_list,
                   'ordering_path': ordering_path,
                   'page_obj': page_obj,
                   'paginator': paginator}

        return render(request, 'shop/rammemory_list.html', context)


class RAMMemoryDetail(DetailView):
    model = RAMMemory
    slug_field = 'url'
    slug_url_kwarg = 'url'
