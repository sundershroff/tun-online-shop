from django.forms import ModelForm
from userapp import models


class UserRegisterForm(ModelForm):
    class Meta:
        model = models.userRegistrationModel
        fields = ['name', 'email', 'door_no', 'street', 'city', 'state', 'country', 'pin_code', 'near_land_mark',
                  'mobile', 'password']


class AdminRegistrationForm(ModelForm):
    class Meta:
        model = models.adminRegistrationModel
        fields = ['name', 'email', 'mobile', 'password', 'otp']


class ProductForm(ModelForm):
    class Meta:
        model = models.Product
        # fields = "__all__"
        fields = ['name', 'image', 'color', 'weight', 'quantity', 'original_price', 'selling_price','status','description','category']
