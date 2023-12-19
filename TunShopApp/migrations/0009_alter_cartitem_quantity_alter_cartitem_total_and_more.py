# Generated by Django 5.0 on 2023-12-19 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TunShopApp', '0008_alter_cartitem_quantity_alter_cartitem_total_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='total',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='selling_price',
            field=models.IntegerField(),
        ),
    ]
