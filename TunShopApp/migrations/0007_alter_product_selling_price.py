# Generated by Django 5.0 on 2023-12-19 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TunShopApp', '0006_alter_cartitem_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='selling_price',
            field=models.IntegerField(),
        ),
    ]