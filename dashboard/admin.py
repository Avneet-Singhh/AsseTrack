from django.contrib import admin
from .models import Product, Order, Brand

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','category','quantity','brand','status')
    list_filter = ('category',)

admin.site.register(Product,ProductAdmin)
admin.site.register(Order)
admin.site.register(Brand)