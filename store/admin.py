from django.contrib import admin
from .models import Customer, Product, Order, OrderItem, ShippingAddress
from django.utils.html import mark_safe


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'user')
    search_fields = ('name', 'email')
    list_filter = ('name',)
    ordering = ('-id',)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1  # number of empty rows to show by default


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'complete', 'date_ordered', 'transaction_id')
    list_filter = ('complete', 'date_ordered')
    search_fields = ('transaction_id', 'customer')
    inlines = [OrderItemInline]
    ordering = ('-date_ordered',)

  

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'digital', 'image')
    list_filter = ('digital',)
    search_fields = ('name',)
    ordering = ('name',)

    


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'order', 'quantity', 'date_added')
    list_filter = ('date_added',)
    search_fields = ('product__name', 'order__id')


@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'order', 'address', 'city', 'state', 'zipcode', 'date_added')
    list_filter = ('city', 'state')
    search_fields = ('address', 'city', 'state', 'zipcode')
