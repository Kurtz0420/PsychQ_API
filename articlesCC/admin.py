from django.contrib import admin

# Register your models here.
from articlesCC.models import Article
from posts.models import Post


class ArticleAdmin(admin.ModelAdmin):
    # following properties will be shown in admin panel
    list_display = ('id', 'title', 'parent_course', 'source', 'reads', 'downloads')
    search_fields = ('id', 'title', 'parent_course', 'tags', 'source')  # users can be searched through these fields
    readonly_fields = []  # fields shouldn't be changed manually

    # below are required but we can set it to nothing
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Article, ArticleAdmin)
