# Generated by Django 5.0 on 2023-12-26 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0005_cartitem_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='original_price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='selling_price',
            field=models.IntegerField(),
        ),
    ]