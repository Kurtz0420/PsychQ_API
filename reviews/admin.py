from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.

from django.contrib import admin
from django.contrib.auth.models import User

from reviews.models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_id', 'user_id']
    search_fields = ['user_id', 'product_id', 'id']
    readonly_fields = ['user_id', 'product_id', 'id']

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

    def get_user_id(self, obj):
        return obj.account.uuid

    def get_product_id(self, obj):
        return obj.product.product_id


admin.site.register(Review, ReviewAdmin)
