# Generated by Django 5.0 on 2023-12-16 09:43

import TunShopApp.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='adminRegistrationModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('mobile', models.IntegerField()),
                ('password', models.CharField(max_length=50)),
                ('otp', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='HomeSliderScreen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=500, null=True)),
                ('sub_tittle', models.CharField(max_length=500, null=True)),
                ('slider_image', models.ImageField(blank=True, null=True, upload_to=TunShopApp.models.getFileName)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TunShopApp.category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField(null=True, unique=True)),
                ('name', models.CharField(max_length=150)),
                ('image', models.ImageField(blank=True, null=True, upload_to=TunShopApp.models.getFileName)),
                ('color', models.CharField(max_length=150, null=True)),
                ('weight', models.CharField(max_length=50, null=True)),
                ('size', models.CharField(max_length=50, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('original_price', models.FloatField()),
                ('selling_price', models.FloatField()),
                ('discount', models.IntegerField()),
                ('description', models.TextField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TunShopApp.category')),
            ],
        ),
        migrations.CreateModel(
            name='userRegistrationModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField(null=True, unique=True)),
                ('name', models.TextField(null=True)),
                ('email', models.EmailField(max_length=100, null=True)),
                ('door_no', models.TextField(null=True)),
                ('street', models.TextField(null=True)),
                ('city', models.TextField(null=True)),
                ('state', models.TextField(null=True)),
                ('country', models.TextField(null=True)),
                ('pin_code', models.TextField(null=True)),
                ('near_land_mark', models.TextField(null=True)),
                ('mobile', models.IntegerField(null=True)),
                ('password', models.CharField(max_length=50, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_uid', models.IntegerField(null=True, unique=True)),
                ('user_quantity', models.IntegerField(default=0)),
                ('order_date', models.DateField(auto_now_add=True, verbose_name='Date')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TunShopApp.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TunShopApp.userregistrationmodel')),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TunShopApp.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TunShopApp.userregistrationmodel')),
            ],
        ),
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TunShopApp.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TunShopApp.userregistrationmodel')),
            ],
        ),
    ]
