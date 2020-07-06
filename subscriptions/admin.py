from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from subscriptions.models import Subscription

from django.contrib import admin
from django.contrib.auth.models import User


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_email', 'purchase_token', 'is_active', 'order_id', 'purchase_status', 'sku_product', 'is_acknowledged', 'purchase_time']
    search_fields = ['id', 'user_email', 'purchase_token', 'order_id', 'sku_product']
    readonly_fields = []

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

    def get_user_id(self, obj):
        return obj.account.uuid

    def get_product_id(self, obj):
        return obj.product.product_id


admin.site.register(Subscription, SubscriptionAdmin)
