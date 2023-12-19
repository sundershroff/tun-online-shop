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
from django.urls import path
from TunShopApp import views
from userapp import user_views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    #admin
    path('admin/', admin.site.urls),
    path('login_admin/', views.login),
    path('logout/', views.logoutbutton),
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
    path('reviews/', views.reviews),
    path('invoice/', views.invoice),
    path('invoice_list/', views.invoice_list),
    path('add_product/', views.add_product),
    path('Product_Delete/<uid>', views.Product_Delete),
    path('edit_product/<uid>', views.edit_product),

#user app
    path('user_index/', user_views.user_index),
    path('logoutbutton/', user_views.logoutbutton),
    path('user_logged_index/', user_views.user_logged_index),
    path('about/', user_views.about),
    path('my-account/', user_views.my_account),
    path('wishlist/', user_views.wishlist),
    path('cart/', user_views.cart),
    path('delete/<id>',user_views.remove_from_cart),
    path('product-details/<uid>', user_views.product_details),
    path('checkout/', user_views.checkout),
    path('shop/', user_views.shop),
    path('contact/', user_views.contact),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
