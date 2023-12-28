from TunShopApp.models import Product, Category, userRegistrationModel, CartItem,WishList,OrderList
from TunShopApp.forms import UserRegisterForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

# Create your views here.
def user_logged_index(request,uid):
    my_data = userRegistrationModel.objects.filter(uid = uid).values()[0]
    breakfast = Product.objects.filter(category = 1)
    briyani = Product.objects.filter(category = 1)
    cart = CartItem.objects.filter(user=uid)
    text=0
    for i in cart:
        text += i.quantity * i.product.selling_price

    wishlist = WishList.objects.filter(user=uid)
    context = {
        'my_data':my_data,
        'breakfast':breakfast,
        'briyani':briyani,
        'cart':cart,
        'wishlist':wishlist,
        'text':text,
    }
    if request.method == "POST":
        print(request.POST)
    return render(request, "user_logged_index.html",context)

def user_logged_my_account(request,uid):
    my_data = userRegistrationModel.objects.filter(uid = uid).values()[0]
    cart = CartItem.objects.filter(user=uid)
    text=0
    for i in cart:
        text += i.quantity * i.product.selling_price

    wishlist = WishList.objects.filter(user=uid)
    context = {
        'my_data':my_data,
        'text':text,
        'cart':cart,
        'wishlist':wishlist,
    }
    if request.method == "POST":
        updateData = userRegistrationModel.objects.get(uid = uid)
        print(request.POST)
        if 'door_no' in request.POST:
            updateData.name = request.POST.get('name', updateData.name)
            updateData.email = request.POST.get('email', updateData.email)
            updateData.door_no = request.POST.get('door_no', updateData.door_no)
            updateData.street = request.POST.get('street', updateData.street)
            updateData.city = request.POST.get('city', updateData.city)
            updateData.state = request.POST.get('state', updateData.state)
            updateData.country = request.POST.get('country', updateData.country)
            updateData.pin_code = request.POST.get('pin_code', updateData.pin_code)
            updateData.near_land_mark = request.POST.get('near_land_mark', updateData.near_land_mark)
            updateData.mobile = request.POST.get('mobile', updateData.mobile)
            updateData.save()
            return redirect(f"/user_logged_index/{uid}")
        #Whislist
        elif "wishlist" in request.POST:
            print("whislist")
            dict={}
            a=[]
            print(request.POST)
            list=Product.objects.get(uid=request.POST["wishlist"])
            a.append(list)
            print(list)
            dict['Product']=a
            data1=WishList.objects.create(
                product=list,
                user=id,
            )
            print(data1)
            data1.save()
            return redirect(f"/wishlist/{id}")
        #cart
        elif 'cart' in request.POST:
            dict={}
            a=[]
            print(request.POST)
            list=Product.objects.get(uid=request.POST["cart"])
            a.append(list)

            dict['Product']=a
            # user=userRegistrationModel.objects.get(uid='871786')
            b=1
            # d=int(products.selling_price) * int(b)
            # print(d)
            data=CartItem.objects.create(
                product=list,
                quantity=b,
                user=id,
                # total=d,
            )
            data.save()
            return redirect(f"/cart/{id}")
        #buy
        elif "buy" in request.POST:
            return redirect(f'/checkout_buy/{id}/{request.POST['buy']}')
        
        else:
            if Category.objects.filter(id=request.POST['menu']):
                product = Product.objects.filter(category_id=request.POST['menu'])
                print(f"this my{product}")
                return render(request, 'shop.html',
                {"product": product,'my_data':my_data,'cart':cart,
                    'wishlist':wishlist,'text':text})

    return render(request, "user_logged_my_account.html",context)

def logoutbutton(request):
    auth.logout(request)
    return redirect("/user_index/")

def Restaurant(request):
    data=Product.objects.filter(category_id=1)
    grocery=Product.objects.filter(category_id=2)
    fruits_vegetables=Product.objects.filter(category_id=3)
    foodproducts=Product.objects.filter(category_id=4)
    cart = CartItem.objects.filter(user=uid)
    text=0
    for i in cart:
        text += i.quantity * i.product.selling_price

    wishlist = WishList.objects.filter(user=uid)
    context = {
        'key':data,
        'grocery':grocery,
        'fruits':fruits_vegetables,
        'food':foodproducts,
        'text':text,
        'cart':cart,
        'wishlist':wishlist,
    }
    if request.method == 'POST':
        print(request.POST)
        if Category.objects.filter(id=request.POST['menu']):
            product = Product.objects.filter(category_id=request.POST['menu'])
            print(f"this my{product}")
            return render(request, 'shop.html',
                          {"product": product})
        else:
            return redirect('/Restaurant/')

    return render(request, "index_Restaurant.html",context)

def my_account(request):
        error=""
        error1 = ""
        form=""
        success = ""
        category = Category.objects.filter()
        print(f'{category} this is all')
        if request.method == 'POST':
            if "door_no" in request.POST:
                print(request.POST)
                form = UserRegisterForm(request.POST)
                if userRegistrationModel.objects.filter(email=request.POST['email']).exists():
                    error1 = "Already Registered"
                else:
                    if request.POST['password'] != request.POST['confirm_password']:
                        print("Your password and confirmation password do not match.")

                    else:
                        if form.is_valid():
                            form.save(commit=False)
                            form.is_staff = True
                            form.save()
                            uidd = userRegistrationModel.objects.filter(email=request.POST['email']).values()[0]
                            success = "Account Created Succesfully Please Login and Continue"
            else:
                    print(request.POST)
                    email = request.POST['email']
                    password = request.POST['password']
                    username = "admin@123"
                    password1 = "!@#$%^&*"
                    # username = userRegistrationModel.objects.get(email=email.lower()).username
                    user = authenticate(request,username = username,password = password1)
                    if user is not None:
                        auth.login(request,user)
                        if userRegistrationModel.objects.filter(email=email, password=password).exists():
                            uidd = userRegistrationModel.objects.filter(email=email).values()[0]
                            return redirect(f'/user_logged_index/{uidd['uid']}')
                        else:
                            error = "Your email or password is Incorrect"
        context ={
                     'error':error,
                        'form': form,
                        'error1' : error1,
                        'success':success,

        }
        return render(request, 'my-account.html',context)

def index(request,uid):
    my_data = userRegistrationModel.objects.filter(uid = uid).values()[0]
    context = {
        'my_data':my_data,
    }
    return render(request, "index_foodproducts.html",context)

def about(request,uid):
    my_data = userRegistrationModel.objects.filter(uid = uid).values()[0]
    cart = CartItem.objects.filter(user=uid)
    text=0
    for i in cart:
        text += i.quantity * i.product.selling_price

    wishlist = WishList.objects.filter(user=uid)
    context = {
        'my_data':my_data,
        'text':text,
        'cart':cart,
        'wishlist':wishlist,
    }
    return render(request, "about.html",context)

def index_fruits_vegetables(request,uid):
    my_data = userRegistrationModel.objects.filter(uid = uid).values()[0]
    cart = CartItem.objects.filter(user=uid)
    text=0
    for i in cart:
        text += i.quantity * i.product.selling_price

    wishlist = WishList.objects.filter(user=uid)
    context = {
        'my_data':my_data,
        'text':text,
        'cart':cart,
        'wishlist':wishlist,
    }
    return render(request, "index_fruits_vegetables.html",context)

def product_details(request,uid,id):
    my_data = userRegistrationModel.objects.filter(uid = uid).values()[0]
    cart = CartItem.objects.filter(user=uid)
    text=0
    for i in cart:
        text += i.quantity * i.product.selling_price

    wishlist = WishList.objects.filter(user=uid)
    if Product.objects.filter(uid=id):
        products = Product.objects.filter(uid=id).first()
    context = {
                'products': products,
                'my_data':my_data,
                'text':text,
        'cart':cart,
        'wishlist':wishlist,
            }
    if request.method == "POST":
        if "cart" in request.POST:
            dict={}
            a=[]
            print(request.POST)
            print(request.POST["quantity"])
            list=Product.objects.get(uid=request.POST["product"])
            a.append(list)

            dict['Product']=a
            user=uid
            b=request.POST["quantity"]
            c=user
            d=int(products.selling_price)*int(b)

            data=CartItem.objects.create(
                product=list,
                quantity=b,
                user=c,
                total=d,
            )
            data.save()
            return redirect(f"/cart/{uid}")
        elif "wishlist" in request.POST:
            print("whislist")
            dict={}
            a=[]
            print(request.POST)
            list=Product.objects.get(uid=request.POST["wishlist"])
            a.append(list)
            print(list)
            dict['Product']=a
            data1=WishList.objects.create(
                product=list,
                user=uid,
            )
            print(data1)
            data1.save()
            return redirect(f"/wishlist/{uid}")
        #buy
        elif "buy" in request.POST:
            return redirect(f'/checkout_buy/{id}/{request.POST['buy']}')

    return render(request,"product-details.html",context)

def cart(request,uid):
    my_data = userRegistrationModel.objects.filter(uid = uid).values()[0]
    data = CartItem.objects.filter(user=uid)
    
    print(data)
    text=0
    for i in data:
        text += i.quantity * i.product.selling_price
    print(text)
    cart = CartItem.objects.filter(user=uid)
    text=0
    for i in cart:
        text += i.quantity * i.product.selling_price

    wishlist = WishList.objects.filter(user=uid)
    if request.method=="POST":
        print(request.POST)
    context = {
        'key':data,
        'total':text,
        'my_data':my_data,
        'text':text,
        'cart':cart,
        'wishlist':wishlist,
    }
    return render(request,"cart.html",context)


def remove_cart(request,id,uid):
    cart_item=CartItem.objects.get(id=id)
    cart_item.delete()
    return redirect(f'/cart/{uid}')

def checkout(request,uid):
    my_data = userRegistrationModel.objects.filter(uid = uid).values()[0]
    data = CartItem.objects.filter(user=uid)
    cart = CartItem.objects.filter(user=uid)
    text=0
    for i in cart:
        text += i.quantity * i.product.selling_price
    wishlist = WishList.objects.filter(user=uid)

    context={
        'my_data':my_data,
        'total':text,
        'cart':cart,
        'wishlist':wishlist,
        'text':text,

    }

    return render(request, "checkout.html",context)

def Grocery(request,uid):
    my_data = userRegistrationModel.objects.filter(uid = uid).values()[0]
    cart = CartItem.objects.filter(user=uid)
    text=0
    for i in cart:
        text += i.quantity * i.product.selling_price

    wishlist = WishList.objects.filter(user=uid)
    context = {
        'my_data':my_data,
        'text':text,
        'cart':cart,
        'wishlist':wishlist,
    }
    return render(request, "index_Grocery.html",context)

def wishlistt(request,uid):
    my_data = userRegistrationModel.objects.filter(uid = uid).values()[0]
    wishlist_list = WishList.objects.filter(user=uid)
    cart = CartItem.objects.filter(user=uid)
    text=0
    for i in cart:
        text += i.quantity * i.product.selling_price

    wishlist = WishList.objects.filter(user=uid)
    context = {
        'my_data':my_data,
        'wishlist_list':wishlist_list,
        'text':text,
        'cart':cart,
        'wishlist':wishlist,
    }
    if request.method == "POST":
        if 'cart' in request.POST:
            dict={}
            a=[]
            print(request.POST)
            list=Product.objects.get(uid=request.POST["cart"])
            a.append(list)

            dict['Product']=a
            # user=userRegistrationModel.objects.get(uid='871786')
            b=request.POST["quantity"]
            # d=int(products.selling_price) * int(b)
            # print(d)
            data=CartItem.objects.create(
                product=list,
                quantity=b,
                user=uid,
                # total=d,
            )
            data.save()
            return redirect(f"/cart/{uid}")
    return render(request, "wishlist.html",context)

def remove_wish(request,id,uid):
    cart_item=WishList.objects.get(id=id)
    cart_item.delete()
    return redirect(f'/wishlist/{uid}')

def contact(request,uid):
    my_data = userRegistrationModel.objects.filter(uid = uid).values()[0]
    cart = CartItem.objects.filter(user=uid)
    text=0
    for i in cart:
        text += i.quantity * i.product.selling_price

    wishlist = WishList.objects.filter(user=uid)
    context = {
        'my_data':my_data,
        'text':text,
        'cart':cart,
        'wishlist':wishlist,
    }
    return render(request, "contact.html",context)

def shop(request,uid,num):
    my_data = userRegistrationModel.objects.filter(uid = uid).values()[0]
    products = Product.objects.filter(category = num)
    cart = CartItem.objects.filter(user=uid)
    text=0
    for i in cart:
        text += i.quantity * i.product.selling_price

    wishlist = WishList.objects.filter(user=uid)
    context = {
        'my_data':my_data,
        'products':products,
        'text':text,
        'cart':cart,
        'wishlist':wishlist,
    }
    if request.method == "POST":
        if "wishlist" in request.POST:
            print("whislist")
            dict={}
            a=[]
            print(request.POST)
            list=Product.objects.get(uid=request.POST["wishlist"])
            a.append(list)
            print(list)
            dict['Product']=a
            data1=WishList.objects.create(
                product=list,
                user=uid,
            )
            print(data1)
            data1.save()
            return redirect(f"/wishlist/{uid}")
        #buy
        elif "buy" in request.POST:
            return redirect(f'/checkout_buy/{id}/{request.POST['buy']}')
        elif 'cart' in request.POST:
            dict={}
            a=[]
            print(request.POST)
            list=Product.objects.get(uid=request.POST["cart"])
            a.append(list)

            dict['Product']=a
            # user=userRegistrationModel.objects.get(uid='871786')
            b=request.POST["quantity"]
            # d=int(products.selling_price) * int(b)
            # print(d)
            data=CartItem.objects.create(
                product=list,
                quantity=b,
                user=uid,
                # total=d,
            )
            data.save()
            return redirect(f"/cart/{uid}")
    return render(request, "shop.html",context)

def product_details_grocery(request):
    return render(request, "product-details_grocery.html")
def product_details_fruits(request):
    return render(request, "product_details_fruits.html")

@login_required(login_url="/my-account/")
def select_payment(request,uid):
    my_data1 = userRegistrationModel.objects.get(uid = uid)
    my_data = userRegistrationModel.objects.filter(uid = uid).values()[0]
    cart = CartItem.objects.filter(user=uid)
    text=0
    for i in cart:
        text += i.quantity * i.product.selling_price

    context={
        'my_data':my_data,
        'text':text,
    }
    if request.method == "POST":
        
        print(request.POST)
        if  request.POST['payment-method'] == "cod":
            for i in cart:
                user_quantity = i.quantity
                product_id = i.product.id
                user_id = my_data1.id
                total_amount = i.quantity * i.product.selling_price
                ordered = OrderList.objects.create(
                    user_quantity = user_quantity,
                    product_id = product_id,
                    user_id =user_id,
                    total_amount = total_amount
                )
                ordered.save()
                print("valid data")
            return redirect(f"/user_order_status/{uid}")
    return render(request,"select_payment.html",context)

@login_required(login_url="/my-account/")
def user_order_status(request,uid):
    my_data = userRegistrationModel.objects.filter(uid = uid).values()[0]
    cart = CartItem.objects.filter(user=uid)
    wishlist = WishList.objects.filter(user=uid)
    text=0
    for i in cart:
        text += i.quantity * i.product.selling_price

    order_list = OrderList.objects.filter(user__uid = uid)
    context = {
        'order_list':order_list,
        'my_data':my_data,
        'text':text,
        'cart':cart,
        'wishlist':wishlist,
    }
    return render(request,"user_order_status.html",context)



