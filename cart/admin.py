from django.contrib import admin
from .models import *

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'items', 'start_date')
    list_filter = ('user')

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'ordered')
    list_filter = ('user')
admin.site.register(Order)
admin.site.register(OrderItem)


