import os.path
import random
import datetime
from django.db import models
from django.contrib.auth.models import User


class adminRegistrationModel(models.Model):

    name = models.TextField(max_length=50)
    email = models.EmailField(max_length=100)
    mobile = models.IntegerField()
    password = models.CharField(max_length=50)
    otp = models.IntegerField(null=True)


# class


class userRegistrationModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    uid = models.IntegerField(unique=True, null=True)

    def save(self, *args, **kwargs):
        if not self.uid:
            self.uid = generate_unique_uid()
        super().save(*args, **kwargs)

    name = models.TextField(null=True)
    email = models.EmailField(max_length=100, null=True)
    door_no = models.TextField(null=True)
    street = models.TextField(null=True)
    city = models.TextField(null=True)
    state = models.TextField(null=True)
    country = models.TextField(null=True)
    pin_code = models.TextField(null=True)
    near_land_mark = models.TextField(null=True)
    mobile = models.IntegerField(null=True)
    password = models.CharField(max_length=50, null=True)

    def __str__(self):
        if self.user:
            return str(self.user)
        else:
            return f"User Registration - {self.uid}"


def getFileName(request, filename):
    now_time = datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    new_filename = "%s%s" % (now_time, filename)
    return os.path.join('uploads/', new_filename)


class Category(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)


class HomeSliderScreen(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,)
    tittle = models.CharField(max_length=500,null=True)
    sub_tittle = models.CharField(max_length=500, null=True)
    slider_image = models.ImageField(upload_to=getFileName, null=True, blank=True)


def generate_unique_uid():
    return random.randint(100000, 999999)


class Product(models.Model):
    uid = models.IntegerField(unique=True, null=True)

    def save(self, *args, **kwargs):
        if not self.uid:
            self.uid = generate_unique_uid()
        super().save(*args, **kwargs)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, )
    name = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to=getFileName, null=True, blank=True)
    color = models.CharField(max_length=150, null=True, )
    weight = models.CharField(max_length=50, null=True, default="empty")
    size = models.CharField(max_length=50, null=True)
    quantity = models.IntegerField(null=True, blank=True)
    original_price = models.FloatField(null=False, blank=False, )
    selling_price = models.FloatField(null=False, blank=False)
    discount = models.IntegerField(null=False, blank=False)
    description = models.TextField(max_length=500, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.TextField(null=True)
    def __str__(self):
        return self.name


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0, null=True)
    user = models.ForeignKey(userRegistrationModel, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'


class WishList(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(userRegistrationModel, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name


class OrderList(models.Model):
    order_uid = models.IntegerField(unique=True, null=True)
    user_quantity = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.order_uid:
            self.order_uid = generate_unique_uid()
        super().save(*args, **kwargs)

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(userRegistrationModel, on_delete=models.CASCADE)
    order_date = models.DateField("Date", auto_now_add=True)
