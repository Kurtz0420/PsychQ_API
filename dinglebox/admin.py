from django.contrib import admin

# Register your models here.
from dinglebox.models import Clip
from posts.models import Post


class ClipAdmin(admin.ModelAdmin):
    # following properties will be shown in admin panel
    list_display = ('id', 'title', 'description', 'audio_link', 'have_ad')
    search_fields = ('id', 'title', 'custom_ordering', 'have_ad')  # users can be searched through these fields
    readonly_fields = []  # fields shouldn't be changed manually

    # below are required but we can set it to nothing
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Clip, ClipAdmin)
