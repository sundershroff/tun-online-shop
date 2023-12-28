import os.path
import random
import datetime
from django.db import models


class adminRegistrationModel(models.Model):
    name = models.TextField(max_length=50)
    email = models.EmailField(max_length=100)
    mobile = models.IntegerField()
    password = models.CharField(max_length=50)
    otp = models.IntegerField(null=True)


class userRegistrationModel(models.Model):
    uid = models.IntegerField(unique=True, null=True)

    def save(self, *args, **kwargs):
        if not self.uid:
            self.uid = generate_unique_uid()
        super().save(*args, **kwargs)
    name = models.TextField(null=True)
    email = models.EmailField(max_length=100,null=True)
    door_no = models.TextField(null=True)
    street = models.TextField(null=True)
    city = models.TextField(null=True)
    state = models.TextField(null=True)
    country = models.TextField(null=True)
    pin_code = models.TextField(null=True)
    near_land_mark = models.TextField(null=True)
    add_to_cart = models.TextField(null=True)
    wish_list = models.TextField(null=True)
    my_orders = models.TextField(null=True)
    mobile = models.IntegerField(null=True)
    password = models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.name












def getFileName(request, filename):
    now_time = datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    new_filename = "%s%s" % (now_time, filename)
    return os.path.join('uploads/', new_filename)


class Category(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    # image = models.ImageField(upload_to=getFileName, null=True, blank=True)
    # description = models.TextField(max_length=500, null=False, blank=False)
    # created_at = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.name


def generate_unique_uid():
    return random.randint(100000, 999999)


class Product(models.Model):
    uid = models.IntegerField(unique=True, null=True)

    def save(self, *args, **kwargs):
        if not self.uid:
            self.uid = generate_unique_uid()
        super().save(*args, **kwargs)

    category = models.ForeignKey(Category, on_delete=models.CASCADE,)
    name = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to=getFileName, null=True, blank=True)
    color = models.CharField(max_length=150, null=True,)
    weight = models.CharField(max_length=50, null=True,)
    size = models.CharField(max_length=50, null=True)
    quantity = models.IntegerField(null=True, blank=True)
    original_price = models.IntegerField(null=False, blank=False, )
    selling_price = models.IntegerField(null=False, blank=False)
    discount = models.IntegerField(null=True, blank=False)
    description = models.TextField(max_length=500, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class CartItem(models.Model):
    product = models.ForeignKey(Product,to_field='id',db_column="product", on_delete=models.CASCADE,null=True)
    quantity = models.PositiveIntegerField(default=0)
    # user = models.ForeignKey(userRegistrationModel, on_delete=models.CASCADE)
    user=models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    total=models.IntegerField()

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'
