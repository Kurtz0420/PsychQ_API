from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from accounts.models import Account


class AccountAdmin(UserAdmin):
    # following properties will be shown in admin panel
    list_display = ('clean_uuid', 'email', 'username', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('username', 'email', 'uuid')  # users can be searched through these fields
    readonly_fields = ('date_joined', 'is_superuser')  # fields shouldnt be changed manually

    # below are required but we can set it to nothing
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)
