# Generated by Django 4.2.6 on 2023-12-18 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0004_alter_cartitem_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='total',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
