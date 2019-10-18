from django.contrib import admin

# Register your models here.
from posts.models import Post


class PostAdmin(admin.ModelAdmin):
    # following properties will be shown in admin panel
    list_display = ('id', 'title', 'category', 'views', 'downloads')
    search_fields = ('id', 'title', 'category', 'tags')  # users can be searched through these fields
    readonly_fields = []  # fields shouldn't be changed manually

    # below are required but we can set it to nothing
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Post, PostAdmin)
