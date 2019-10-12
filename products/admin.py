from django.contrib import admin

# Register your models here.
from products.models import Product
from django.contrib import admin
from django.contrib.auth.models import User


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'quantity_in_stock', 'sales', 'price']
    search_fields = ['id', 'name']
    readonly_fields = []

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

    # def get_user_id(self, obj):
    #     return obj.reviews.user_id
    #
    # def get_description(self, obj):
    #     return obj.reviews.description

    # get_user_id.admin_order_field = 'author'  # Allows column order sorting
    # get_description.short_description = 'Author Name'  # Renames column head

    # Filtering on side - for some reason, this works
    # list_filter = ['title', 'author__name']


# admin.site.unregister(User)


admin.site.register(Product, ProductAdmin)
