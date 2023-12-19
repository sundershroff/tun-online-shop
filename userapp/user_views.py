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
def my_account(request):
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
                        return redirect('/user_logged_index/')
        else:
            if request.method == 'POST':
                print(request.POST)
                email = request.POST['email']
                password = request.POST['password']
                if userRegistrationModel.objects.filter(email=email, password=password).exists():
                    return redirect('/user_logged_index/')
                else:
                    error = "Your email or password is Incorrect"
    context = {
                    'error':error,
                    'form': form,
                    'error1' : error1
    }
    return render(request,"my-account.html",context)

    # return render(request,"my-account.html", {'form': form})
def logoutbutton(request):
    auth.logout(request)
    return redirect("/user_index/")



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

def user_logged_index(request):
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

    return render(request,"user_logged_index.html")

def about(request):
    return render(request,"about.html")

def wishlist(request):
    return render(request,"wishlist.html")
def cart(request):
    data = CartItem.objects.filter(user='871786')
    # print(data)
    text=0
    for i in data:
        text += i.quantity * i.product.selling_price
    if request.method=="POST":
        print(request.POST)
    context = {
        'key':data,
        'total':text
    }
    return render(request,"cart.html",context)

def remove_from_cart(request, id):
    cart_item = CartItem.objects.get(id=id)
    cart_item.delete()
    return redirect("/cart/")

def product_details(request,uid):
    # category = Category.objects.filter()
    # user_id = userRegistrationModel.objects.first()
    # print(user_id.uid)
    # print(Category.objects.filter(name=cname))
    if Product.objects.filter(uid=uid):
            products = Product.objects.filter(uid=uid).first()
            print(products.selling_price)
    context = {
                "products": products,
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
def checkout(request):
    return render(request,"checkout.html")
def shop(request):
    return render(request,"shop.html")
def contact(request):
    return render(request,"contact.html")

