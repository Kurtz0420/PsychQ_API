from django.contrib import admin

# Register your models here.
from jokes.models import Joke
from posts.models import Post
from userjokes.models import UserJoke


class UserJokeAdmin(admin.ModelAdmin):
    # following properties will be shown in admin panel
    list_display = ('id', 'username', 'email', 'type', 'build_up', 'thumbs_ups', 'thumbs_downs')
    search_fields = ('id', 'username', 'type', 'email', 'build_up')  # users can be searched through these fields
    readonly_fields = []  # fields shouldn't be changed manually

    # below are required but we can set it to nothing
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(UserJoke, UserJokeAdmin)
