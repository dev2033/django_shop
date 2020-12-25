from django.contrib import admin

from .models import CartProduct, Cart, Category, Customer, Order, Product


admin.site.register(Category)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Product)
