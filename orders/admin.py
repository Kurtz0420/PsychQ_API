from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from orders.models import Order

from django.contrib import admin
from django.contrib.auth.models import User


class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'product_id', 'user_id', 'timestamp']
    search_fields = ['user_id', 'product_id', 'order_id']
    readonly_fields = []

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

    def get_user_id(self, obj):
        return obj.account.uuid

    def get_product_id(self, obj):
        return obj.product.product_id


admin.site.register(Order, OrderAdmin)
