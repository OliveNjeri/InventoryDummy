from django.contrib import admin
from .models import Product
from django.contrib.auth.models import Group


admin.site.site_header = 'Keline Inventory System'

class productAdmin(admin.ModelAdmin):
    list_display= ('name', 'category', 'quantity',)
    list_filter= ['category']

# Register your models here.
admin.site.register(Product, productAdmin)