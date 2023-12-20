from TunShopApp.models import Product, Category, userRegistrationModel, CartItem
from TunShopApp.forms import UserRegisterForm
# from django.contrib import messages
# from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache




# Create your views here.

def user_index(request):
    if request.method == "POST":
        print(request.POST)
        if Category.objects.filter(id=request.POST['menu']):
            product = Product.objects.filter(category_id=request.POST['menu'])
            print(f"this my{product}")
            return render(request, 'shop.html',
                      {"product": product})
        else:
            return redirect('/user_index/')
    else:
        pass

    return render(request,"user_index.html")

@login_required(login_url="/my-account/")
def user_logged_index(request,id):
    my_data = userRegistrationModel.objects.filter(uid = id).values()[0]
    global uiddd
    uiddd = my_data['uid']
    print(uiddd)
    context={
        'my_data':my_data,
    }
    if request.method == "POST":
        print(request.POST)
        if Category.objects.filter(id=request.POST['menu']):
            product = Product.objects.filter(category_id=request.POST['menu'])
            print(f"this my{product}")
            return render(request, 'shop.html',
                      {"product": product,'my_data':my_data})
        else:
            return redirect('/user_index/')
    else:
        pass

    return render(request,"user_logged_index.html",context)

@never_cache
def my_account(request):
    if request.user.is_authenticated:
        # user_logged_index(request,id)
        print(uiddd)
        return redirect(f'/user_logged_index/{uiddd}')
    else:
        error=""
        error1 = ""
        form=""
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
                            return redirect(f'/user_logged_index/{uidd['uid']}')
            else:
                if request.method == 'POST':
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

        context = {
                        'error':error,
                        'form': form,
                        'error1' : error1
        }
        return render(request,"my-account.html",context)


@login_required(login_url="/my-account/")
def user_logged_my_account(request,id):   
    updateData = userRegistrationModel.objects.get(uid = id)
    my_data = userRegistrationModel.objects.filter(uid = id).values()[0]
    context={
        'my_data':my_data,
    }
    if request.method == "POST":
        print(request.POST)
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
        return redirect(f"/user_logged_index/{id}")

    return render(request,"user_logged_my_account.html",context)


def logoutbutton(request):
    auth.logout(request)
    return redirect("/user_index/")




@login_required(login_url="/my-account/")
def about(request,id):
    my_data = userRegistrationModel.objects.filter(uid = id).values()[0]
    context={
        'my_data':my_data,
    }
    return render(request,"about.html",context)

@login_required(login_url="/my-account/")
def wishlist(request,id):
    my_data = userRegistrationModel.objects.filter(uid = id).values()[0]
    context={
        'my_data':my_data,
    }
    return render(request,"wishlist.html",context)

@login_required(login_url="/my-account/")
def cart(request,id):
    my_data = userRegistrationModel.objects.filter(uid = id).values()[0]
    data = CartItem.objects.filter(user='871786')
    # print(data)
    text=0
    for i in data:
        text += i.quantity * i.product.selling_price
    if request.method=="POST":
        print(request.POST)
    context = {
        'key':data,
        'total':text,
        'my_data':my_data,

    }
    return render(request,"cart.html",context)

@login_required(login_url="/my-account/")
def remove_from_cart(request, id):
    cart_item = CartItem.objects.get(id=id)
    cart_item.delete()
    return redirect("/cart/")

@login_required(login_url="/my-account/")
def product_details(request,id,uid):
    my_data = userRegistrationModel.objects.filter(uid = id).values()[0]
    # category = Category.objects.filter()
    # user_id = userRegistrationModel.objects.first()
    # print(user_id.uid)
    # print(Category.objects.filter(name=cname))
    if Product.objects.filter(uid=uid):
            products = Product.objects.filter(uid=uid).first()
            print(products.selling_price)
    context = {
                "products": products,
                'my_data':my_data,

            }
    if request.method == "POST":
        dict={}
        a=[]
        print(request.POST)
        print(request.POST["quantity"])
        list=Product.objects.get(uid=request.POST["product"])
        a.append(list)

        dict['Product']=a
        # user=userRegistrationModel.objects.get(uid='871786')
        user="871786"
        b=request.POST["quantity"]
        c=int(user)
        # d=int(products.selling_price) * int(b)
        # print(d)
        data=CartItem.objects.create(
            product=list,
            quantity=b,
            user=c,
            # total=d,
        )
        data.save()
        return redirect("/cart/")

    return render(request,"product-details.html",context)

@login_required(login_url="/my-account/")
def checkout(request,id):
    my_data = userRegistrationModel.objects.filter(uid = id).values()[0]
    context={
        'my_data':my_data,
    }

    return render(request,"checkout.html",context)

@login_required(login_url="/my-account/")
def shop(request,id):
    my_data = userRegistrationModel.objects.filter(uid = id).values()[0]
    context={
        'my_data':my_data,
    }

    return render(request,"shop.html",context)

@login_required(login_url="/my-account/")
def contact(request,id):
    my_data = userRegistrationModel.objects.filter(uid = id).values()[0]
    context={
        'my_data':my_data,
    }

    return render(request,"contact.html",context)

