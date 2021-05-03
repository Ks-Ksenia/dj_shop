from django.urls import path

from .views import *


urlpatterns = [
   path('', index.as_view(), name='index_url'),
   path('catalog/17a8e9b716404e77/fridge/', FridgeView.as_view(), name='fridge_url'),
   path('product/17a8a01d16404e87/<str:url>/<str:category>/specifications/',
        FridgeDetail.as_view(), name='fridge_product_url'),

   path('catalog/e3d826d63bb17fd7/stove/', StoveView.as_view(), name='stove_url'),
   path('product/32b43e6addd53332/<str:url>/<str:category>/specifications/',
        StoveDetail.as_view(), name='stove_product_url'),

   path('catalog/89873d5539157fd7/microwave_oven/', MicrowaveOvenView.as_view(), name='microwave_oven_url'),
   path('product/89873d5539157fd2/<str:url>/<str:category>/specifications/',
        MicrowaveOvenDetail.as_view(), name='microwave_oven_product_url'),

   path('catalog/e239e04839157fd7/kettle/', KettleView.as_view(), name='kettle_url'),
   path('product/e239e04831157fd7/<str:url>/<str:category>/specifications/',
        KettleDetail.as_view(), name='kettle_product_url'),

   path('catalog/e239e09939157fd8/iron/', IronView.as_view(), name='iron_url'),
   path('product/e239e048a9157fd8/<str:url>/<str:category>/specifications/',
        IronDetail.as_view(), name='iron_product_url'),

   path('catalog/e239e06639157fd8/wash_machine/', WashMachineView.as_view(), name='wash_machine_url'),
   path('product/e239e048a2557fd8/<str:url>/<str:category>/specifications/',
        WashMachineDetail.as_view(), name='wash_machine_product_url'),

   path('catalog/17a8d5ad16a04e77/dry_machine/', DryMachineView.as_view(), name='dry_machine_url'),
   path('product/17a8d5ada6a04e77/<str:url>/<str:category>/specifications/',
        DryMachineDetail.as_view(), name='dry_product_url'),

   path('catalog/hairdryer/e239ej9939157fd8/', HairdryerView.as_view(), name='hairdryer_url'),
   path('product/e239e0d8a2557fd8/<str:url>/<str:category>/specifications/',
        HairdryerDetail.as_view(), name='hairdryer_product_url'),

   path('catalog/hairclipper/e239e099y9157fd8/', HairClipperView.as_view(), name='hair_clipper_url'),
   path('product/e239e04la2557fd8/<str:url>/<str:category>/specifications/',
        HairClipperDetail.as_view(), name='hair_clipper_product_url'),

   path('catalog/smartphonee/239e099k9157fd8/', SmartphoneView.as_view(), name='smartphone_url'),
   path('product/e239e048a2g57fd8/<str:url>/<str:category>/specifications/',
        SmartphoneDetail.as_view(), name='smartphone_product_url'),

   path('catalog/smartwatch/e239e0993w157fd8/', SmartWatchView.as_view(), name='smart_watch_url'),
   path('product/e239e048a255kfd8/<str:url>/<str:category>/specifications/',
        SmartWatchDetail.as_view(), name='smart_watch_product_url'),

   path('catalog/tablet/17a8d5ad16a04e70/', TabletView.as_view(), name='tablet_url'),
   path('product/e239e048ahg57fd8/<str:url>/<str:category>/specifications/',
        TabletDetail.as_view(), name='tablet_product_url'),

   path('catalog/ebook/17a8d5ad16a04eh7/', EBookView.as_view(), name='ebook_url'),
   path('product/eee9e048a9157fd8/<str:url>/<str:category>/specifications/',
        EBookDetail.as_view(), name='ebook_product_url'),

   path('catalog/tv/17a8d55d16a04e77/', TVView.as_view(), name='TV_url'),
   path('product/eee9e048ag157fd8/<str:url>/<str:category>/specifications/',
        TVDetail.as_view(), name='tv_product_url'),

   path('catalog/bracket_tv/17a8d5ado6a04e77/', BracketTVView.as_view(), name='bracket_tv_url'),
   path('product/eee9e058a9157fd8/<str:url>/<str:category>/specifications/',
        BracketTVDetail.as_view(), name='bracket_tv_product_url'),

   path('catalog/columns/17a8d5ad16a04e66/', ColumnView.as_view(), name='columns_url'),
   path('product/eee9e0l8a9157fd8/<str:url>/<str:category>/specifications/',
        ColumnDetail.as_view(), name='columns_product_url'),

   path('catalog/headphones/17a8d5ad16a04e99/', HeadphonesView.as_view(), name='headphones_url'),
   path('product/e0e9e048a9157fd8/<str:url>/<str:category>/specifications/',
        HeadphonesDetail.as_view(), name='headphones_product_url'),


   path('catalog/notebook/17a8d9ad06a04e77/', NotebookView.as_view(), name='notebook_url'),
   path('product/70f8eb1c25f93330/<str:url>/<str:category>/specifications/',
        NotebookDetail.as_view(), name='notebook_product_url'),

   path('catalog/system_unit/17a8d5ad10a04e77/', SystemUnitView.as_view(), name='system_unit_url'),
   path('product/e33ed1823ba77fd7/<str:url>/<str:category>/specifications/',
        SystemUnitDetail.as_view(), name='system_unit_product_url'),

   path('catalog/server/89873d5539157fd6/', ServerView.as_view(), name='server_url'),
   path('product/17a8932c16404e77/<str:url>/<str:category>/specifications/',
        ServerDetail.as_view(), name='server_product_url'),

   path('catalog/processor/89873d5539157fdk/', ProcessorView.as_view(), name='processor_url'),
   path('product/f0c209b4cbf43332/<str:url>/<str:category>/specifications/',
        ProcessorDetail.as_view(), name='processor_product_url'),

   path('catalog/motherboard/89873d5539157fdb/', MotherboardView.as_view(), name='motherboard_url'),
   path('product/801923443bad7fd7/<str:url>/<str:category>/specifications/',
        MotherboardDetail.as_view(), name='motherboard_product_url'),

   path('catalog/video_card/89873d5539157fdy/', VideoCardView.as_view(), name='video_card_url'),
   path('product/65f542ee3bbc7fd7/<str:url>/<str:category>/specifications/',
        VideoCardDetail.as_view(), name='videocard_product_url'),

   path('catalog/RAM_memory/89873d5539157fd0/', RAMMemoryView.as_view(), name='RAM_memory_url'),
   path('product/17a9da8816404e77/<str:url>/<str:category>/specifications/',
        RAMMemoryDetail.as_view(), name='rammemory_product_url'),

   path('search/', Search.as_view(), name='search'),
   path('product/<str:url>/<str:category>/review/', AddReview.as_view(), name='add_reviews_url'),
   path('product/<str:url>/<str:category>/description/', Description.as_view(), name='description_url'),
   path('singup/', SignUp.as_view(), name='singup_url'),
   path('catalog/17a9da8016404e77/', MainMenuList.as_view(), name='main_menu_url'),
   path('catalog/17a9da88j6404e77/<str:url>/', MenuView.as_view(), name='menu_url'),
   path('catalog/17a99a8816404e77/<str:url>/', SubMenuView.as_view(), name='submenu_url'),
   path('cart/', CartView.as_view(), name='cart_url'),
   path('add_cart/<str:url>/<str:category>/', AddToCartView.as_view(), name='add_product_to_cart_url'),
   path('delete_cart/<str:url>/<str:category>/', DeleteToCartView.as_view(), name='delete_product_from_cart_url'),
   path('change_quantity_cart/<str:url>/<str:category>/', ChangeQuantityView.as_view(),
        name='change_quantity_cart_url'),
   path('registration_order/', OrderRegistrationView.as_view(), name='register_order_url'),
   path('make_order/', MakeOrderView.as_view(), name='make_order_url'),
   path('end_order/<int:number>', EndOrderView.as_view(), name='end_order_url'),

   path('cart_anon/', CartAnonView.as_view(), name='cart_anon_url'),
   path('add_cart_anon/<str:url>/<str:category>/', AddToCartAnonView.as_view(), name='add_cart_anon_url'),
   path('del_cart_anon/<str:url>/<str:category>/', DelToCartAnonView.as_view(), name='del_cart_anon_url'),
   path('quantity_cart_anon/<str:url>/<str:category>/',
        ChangeQuantityCartAnonView.as_view(), name='quantity_cart_anon_url'),

]