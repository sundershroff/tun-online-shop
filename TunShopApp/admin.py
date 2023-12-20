from django.contrib import admin

# Register your models here.
from .models import userRegistrationModel
from django.contrib.auth.admin import UserAdmin



# admin.site.register(UserAdmin)
# admin.site.register(Group)
admin.site.register(userRegistrationModel)