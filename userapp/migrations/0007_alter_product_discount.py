# Generated by Django 5.0 on 2023-12-26 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0006_alter_product_original_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.IntegerField(null=True),
        ),
    ]
