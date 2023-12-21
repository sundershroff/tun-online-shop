# Generated by Django 5.0 on 2023-12-21 11:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TunShopApp', '0010_alter_wishlist_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlist',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='product',
            field=models.ForeignKey(db_column='product', null=True, on_delete=django.db.models.deletion.CASCADE, to='TunShopApp.product'),
        ),
    ]
