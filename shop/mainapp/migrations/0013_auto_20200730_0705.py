# Generated by Django 3.0.8 on 2020-07-30 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0012_auto_20200729_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(blank=True, related_name='related_cart', to='mainapp.CartProduct'),
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
