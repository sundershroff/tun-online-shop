# Generated by Django 5.0 on 2023-12-19 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TunShopApp', '0005_alter_cartitem_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='total',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]