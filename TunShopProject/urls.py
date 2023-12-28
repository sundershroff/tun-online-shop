"""TunShopProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from TunShopApp import views
from userapp import user_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    #admin
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login_admin/', views.login),
    path('logoutbutton/', views.logoutbutton),
    path('index/', views.index),
    path('order_status/', views.order_status),
    path('email/', views.email),
    path('user_profile/', views.user_profile),
    path('lock_screen/', views.lock_screen),
    path('default_login/', views.default_login),
    path('product_list/', views.product_list),
    path('product_grid/', views.product_grid),
    path('product_detail/<uid>', views.product_detail),
    path('cancel_product/', views.cancel_product),
    path('return_product/', views.return_product),
    path('customer/', views.customer),
    path('customer_delete/<uid>', views.customer_delete),
    path('reviews/', views.reviews),
    path('invoice/<id>', views.invoice),
    path('invoice_list/', views.invoice_list),
    path('add_product/', views.add_product),
    path('Product_Delete/<uid>', views.Product_Delete),
    path('edit_product/<uid>', views.edit_product),
    path('slider/', views.sliderr),
    path('pdf/<id>', views.get), 


#user app
    path('foods/<uid>', user_views.index),
    path('user_index/', user_views.Restaurant),
    path('logout/', user_views.logoutbutton),
    path('about/<uid>', user_views.about),
    path('fruits_vegetables/<uid>', user_views.index_fruits_vegetables),
    path('product-details/<uid>/<id>', user_views.product_details),
    path('cart/<uid>', user_views.cart),
    path('remove-cart/<id>/<uid>',user_views.remove_cart),
    path('checkout/<uid>', user_views.checkout),
    path('Grocery/<uid>', user_views.Grocery),
    path('wishlist/<uid>', user_views.wishlistt),
    path('remove_wish/<id>/<uid>',user_views.remove_wish),
    
    path('contact/<uid>', user_views.contact),
    path('my-account/', user_views.my_account),
    path('shop/<uid>/<num>', user_views.shop),
    path('product_details_grocery/<uid>', user_views.product_details_grocery),
    path('product_details_fruits/<uid>', user_views.product_details_fruits),
    path('select_payment/<uid>', user_views.select_payment),
    path('user_order_status/<uid>', user_views.user_order_status),

    

    path('user_logged_index/<uid>', user_views.user_logged_index),
    path('user_logged_my_account/<uid>', user_views.user_logged_my_account),





]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
