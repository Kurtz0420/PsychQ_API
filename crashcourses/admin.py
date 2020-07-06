from django.contrib import admin

# Register your models here.

# Register your models here.
from categories.models import Category
from crashcourses.models import CrashCourse


class CrashCourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'source', 'author_name', 'is_finished', 'total_articles_count', 'description']
    search_fields = ['id', 'title']
    readonly_fields = []

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(CrashCourse, CrashCourseAdmin)
