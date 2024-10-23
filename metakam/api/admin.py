from django.contrib import admin
from .models import Category, Product, Tag, Brand, Supplier, Inventory, Order, OrderItem, Review

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(Brand)
admin.site.register(Supplier)
admin.site.register(Inventory)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Review)
