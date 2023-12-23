from django.shortcuts import render, redirect
from django.http import HttpResponse
from TunShopApp.models import Product, Category, adminRegistrationModel, OrderList, CartItem, HomeSliderScreen,userRegistrationModel
from TunShopApp.forms import ProductForm, AdminRegistrationForm, SliderImageForm
import random
import yagmail
from django.contrib.auth import logout
from django.views.decorators.cache import cache_control
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
import datetime
from TunShopApp.process_to_pdf import html_to_pdf
import locale
locale.setlocale(locale.LC_ALL, "")


# Create your views here.
@never_cache
def login(request):
    if request.user.is_authenticated:
        return redirect('/index/')
    else:
        error = ""
        error1 = ""
        if request.method=="POST":
            try:
                print(request.POST)
                email = request.POST['email']
                password1 = request.POST['password']
                #get email in auth user
                username = User.objects.get(email=email.lower()).username
                user = auth.authenticate(request,username = username,password = password1)
                if user is not None:
                    auth.login(request,user)
                    return redirect("/index/")
                else:
                    error = "Email Id Or Password is Wrong"
            
            except:
                error1 = "User Does'nt Exixts"

        context={
            'error' :error,
            'error1':error1
        }    
        return render(request,"login_index.html",context)


def logoutbutton(request):
    auth.logout(request)
    return redirect("/login_admin/")

@login_required(login_url="/login_admin/")
def index(request):
    x = datetime.datetime.now()
    all_Product = Product.objects.all()
    all_order = OrderList.objects.all()
    order_list = OrderList.objects.filter(order_date =str(datetime.datetime.now()).split()[0] )
    today_revenue = 0
    for i in order_list:
       print(i.total_amount)
       today_revenue += i.total_amount
    context = {
        'products':all_Product,
        'today_revenue':today_revenue,
        'today_sale':order_list,
        'all_order':all_order[::-1],
    }

    return render(request, "index.html",context)

@login_required(login_url="/login_admin/")
def order_status(request):
    order_list = OrderList.objects.all()
    context = {
        'order_list':order_list[::-1],
    }
    return render(request, "order_status.html",context)

@login_required(login_url="/login_admin/")
def email(request):
    return render(request, "email.html")

@login_required(login_url="/login_admin/")
def user_profile(request):
    return render(request, "user_profile.html")

@login_required(login_url="/login_admin/")
def lock_screen(request):
    return render(request, "lock_screen.html")

@login_required(login_url="/login_admin/")
def default_login(request):
    return render(request, "default_login.html")

@login_required(login_url="/login_admin/")
def product_list(request):
    data = Product.objects.all()
    context = {
        'products':data
    }
    return render(request, "product_list.html",context)

@login_required(login_url="/login_admin/")
def product_grid(request):
    data = Product.objects.all()
    context = {
        'products':data
    }

    return render(request, "product_grid.html",context)

@login_required(login_url="/login_admin/")
def product_detail(request,uid):
    data = Product.objects.get(uid=uid)
    context={
        'product':data
    }
    return render(request, "product_detail.html",context)

@login_required(login_url="/login_admin/")
def cancel_product(request):
    return render(request, "cancel_product.html")

@login_required(login_url="/login_admin/")
def return_product(request):
    return render(request, "return_product.html")

@login_required(login_url="/login_admin/")
def customer(request):
    all_customer = userRegistrationModel.objects.all()
    context = {
        'all_customer':all_customer
    }
    return render(request, "customer.html",context)

@login_required(login_url="/login_admin/")
def customer_delete(request,uid):
    customer = userRegistrationModel.objects.get(uid = uid)
    customer.delete()
    return redirect("/customer/")


@login_required(login_url="/login_admin/")
def reviews(request):
    return render(request, "reviews.html")

@login_required(login_url="/login_admin/")
def invoice(request,id):
    invoice_page = OrderList.objects.get(order_uid = id)
    context = {
        'invoice_page':invoice_page,

    }
    return render(request, "invoice.html",context)

@login_required(login_url="/login_admin/")
def invoice_list(request):
    order_list = OrderList.objects.all()
    context = {
        'order_list':order_list[::-1],
    }
    return render(request, "invoice_list.html",context)

@login_required(login_url="/login_admin/")
def add_product(request):
    categories = Category.objects.all()
    print(categories)
    context = {"categories": categories}
    if request.method == "POST":
            print(request.POST)
            print(request.FILES)
            category = request.POST['category']
            name = request.POST['name']
            image = request.FILES['image']
            color = request.POST['color']
            weight = request.POST['weight']
            quantity = request.POST['quantity']
            original_price = request.POST['original_price']
            selling_price = request.POST['selling_price']
            discount = request.POST['discount']
            description = request.POST['description']
            #weight
            if weight == "":
                weight1 = "empty"
            else:
                weight1 = request.POST['weight']
            #color
            if color == "":
                color1 = "empty"
            else:
                color1 = color
            #discount
            if discount == "":
                discount1 = 0
            else:
                discount1 = request.POST['discount']

            data = {
                "category": category,
                "name": name,
                # "image": image,
                "color": color1,
                "quantity": quantity,
                "original_price": original_price,
                "selling_price": selling_price,
                "discount": discount1,
                "description": description,
                "weight": weight1,
                'status':"on"
            }
            print(data)

            # forms = ProductForm(data=request.POST, files=request.FILES)
            forms = ProductForm(data,request.FILES)
            print(forms.is_valid())
            if forms.is_valid():
                # forms.save(commit=False)
                # forms.is_staff = True
                forms.save()
                print("valid data")
                return redirect("/product_list/")
    return render(request, "add_product.html",context)

@login_required(login_url="/login_admin/")
def Product_Delete(request, uid):
    data = Product.objects.get(uid=uid)
    data.delete()
    return redirect('/product_list/')

@login_required(login_url="/login_admin/")
def edit_product(request, uid):
    categories = Category.objects.all()
    updateData = Product.objects.get(uid=uid)
    context={
        'categories':categories,
        'edit':updateData,
    }
    if request.method == "POST":
        print(request.POST)
        print(request.FILES)
        if "status" in request.POST:
            status1 = request.POST['status']
        else:
            status1 = None
        if "image" in request.FILES:
            image1 = request.FILES['image']
        else:
            image1 = updateData.image
        updateData.name = request.POST.get('name', updateData.name)
        updateData.image = image1
        updateData.color = request.POST.get('color', updateData.color)
        updateData.weight = request.POST.get('weight', updateData.weight)
        updateData.quantity = request.POST.get('quantity', updateData.quantity)
        updateData.original_price = request.POST.get('original_price', updateData.original_price)
        updateData.selling_price = request.POST.get('selling_price', updateData.selling_price)
        updateData.discount = request.POST.get('discount', updateData.discount)
        updateData.description = request.POST.get('description', updateData.description)
        updateData.status = status1
        updateData.save()

        return redirect('/product_list/')
    return render(request,"edit_product.html",context)

@login_required(login_url="/login_admin/")
def slider(request):
    return render(request,"slider.html")



def get(request,id, *args, **kwargs):
        invoice_page = OrderList.objects.get(order_uid = id)

        # getting the template
        pdf = html_to_pdf('invoice.html',context_dict={'invoice_page':invoice_page})
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')