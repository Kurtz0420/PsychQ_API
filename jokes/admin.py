from django.contrib import admin

# Register your models here.
from jokes.models import Joke
from posts.models import Post


class JokeAdmin(admin.ModelAdmin):
    # following properties will be shown in admin panel
    list_display = ('id', 'custom_ordering', 'about', 'type', 'nsfw', 'political', 'religious')
    search_fields = ('id', 'about', 'type', 'nsfw', 'religious', 'political')  # users can be searched through these fields
    readonly_fields = []  # fields shouldn't be changed manually

    # below are required but we can set it to nothing
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Joke, JokeAdmin)
