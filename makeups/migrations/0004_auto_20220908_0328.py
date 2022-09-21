# Generated by Django 3.2.15 on 2022-09-08 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('makeups', '0003_makeup_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='makeup',
            name='product',
        ),
        migrations.AddField(
            model_name='makeup',
            name='products',
            field=models.ManyToManyField(related_name='product', to='products.Product'),
        ),
    ]
