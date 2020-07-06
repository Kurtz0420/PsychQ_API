from django.contrib import admin

# Register your models here.
from announcements.models import Announcement
from posts.models import Post


class AnnouncementAdmin(admin.ModelAdmin):
    # following properties will be shown in admin panel
    list_display = ('id', 'heading', 'message')
    search_fields = ('id', 'heading', 'message')  # users can be searched through these fields
    readonly_fields = []  # fields shouldn't be changed manually

    # below are required but we can set it to nothing
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Announcement, AnnouncementAdmin)
